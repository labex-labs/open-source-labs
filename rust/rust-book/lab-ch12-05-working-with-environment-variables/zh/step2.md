# 为不区分大小写的搜索功能编写失败的测试

我们首先添加一个新的 `search_case_insensitive` 函数，当环境变量有值时会调用该函数。我们将继续遵循测试驱动开发（TDD）流程，所以第一步还是编写一个会失败的测试。我们将为新的 `search_case_insensitive` 函数添加一个新测试，并将旧测试从 `one_result` 重命名为 `case_sensitive`，以明确这两个测试之间的差异，如清单12 - 20所示。

文件名：`src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn case_sensitive() {
        let query = "duct";
        let contents = "\
Rust:
safe, fast, productive.
Pick three.
Duct tape.";

        assert_eq!(
            vec!["safe, fast, productive."],
            search(query, contents)
        );
    }

    #[test]
    fn case_insensitive() {
        let query = "rUsT";
        let contents = "\
Rust:
safe, fast, productive.
Pick three.
Trust me.";

        assert_eq!(
            vec!["Rust:", "Trust me."],
            search_case_insensitive(query, contents)
        );
    }
}
```

清单12 - 20：为我们即将添加的不区分大小写的函数添加一个新的失败测试

注意，我们也编辑了旧测试的 `contents`。我们添加了一行文本 `"Duct tape."`，其中字母 _D_ 是大写的，当我们以区分大小写的方式进行搜索时，它不应与查询 `"duct"` 匹配。以这种方式更改旧测试有助于确保我们不会意外破坏已经实现的区分大小写的搜索功能。这个测试现在应该会通过，并且在我们处理不区分大小写的搜索时应该会继续通过。

针对不区分大小写搜索的新测试使用 `"rUsT"` 作为查询。在我们即将添加的 `search_case_insensitive` 函数中，查询 `"rUsT"` 应该与包含大写字母 _R_ 的 `"Rust:"` 行匹配，并且应该与 `"Trust me."` 行匹配，即使这两行的大小写与查询不同。这就是我们的失败测试，它将无法编译，因为我们尚未定义 `search_case_insensitive` 函数。你可以随意添加一个总是返回空向量的框架实现，类似于我们在清单12 - 16中为 `search` 函数所做的那样，看看测试编译并失败的情况。
