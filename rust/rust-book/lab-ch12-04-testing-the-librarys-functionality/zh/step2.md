# 编写一个会失败的测试

因为我们不再需要它们了，所以让我们从 `src/lib.rs` 和 `src/main.rs` 中删除我们之前用来检查程序行为的 `println!` 语句。然后，在 `src/lib.rs` 中，我们将像在第 11 章中那样添加一个带有测试函数的 `tests` 模块。这个测试函数指定了我们希望 `search` 函数具有的行为：它将接受一个查询和要搜索的文本，并只返回文本中包含该查询的行。清单 12-15 展示了这个测试，它目前还无法编译。

文件名：`src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn one_result() {
        let query = "duct";
        let contents = "\
Rust:
safe, fast, productive.
Pick three.";

        assert_eq!(
            vec!["safe, fast, productive."],
            search(query, contents)
        );
    }
}
```

清单 12-15：为我们期望拥有的 `search` 函数创建一个会失败的测试

这个测试搜索字符串 `"duct"`。我们正在搜索的文本有三行，其中只有一行包含 `"duct"`（注意，开头双引号后的反斜杠告诉 Rust 不要在这个字符串字面量的内容开头放置换行符）。我们断言从 `search` 函数返回的值只包含我们期望的那一行。

我们还不能运行这个测试并看到它失败，因为这个测试甚至都无法编译：`search` 函数还不存在！根据 TDD 原则，我们将添加足够的代码以使测试能够编译并运行，方法是添加一个总是返回空向量的 `search` 函数定义，如清单 12-16 所示。然后，测试应该能够编译并失败，因为空向量与包含 `"safe, fast, productive."` 这一行的向量不匹配。

文件名：`src/lib.rs`

```rust
pub fn search<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    vec![]
}
```

清单 12-16：定义足够的 `search` 函数以使我们的测试能够编译

注意，我们需要在 `search` 的签名中定义一个显式的生命周期 `'a`，并将该生命周期用于 `contents` 参数和返回值。回想一下第 10 章，生命周期参数指定了哪个参数的生命周期与返回值的生命周期相关联。在这种情况下，我们表明返回的向量应该包含引用 `contents` 参数切片的字符串切片（而不是 `query` 参数）。

换句话说，我们告诉 Rust，`search` 函数返回的数据将与通过 `contents` 参数传递给 `search` 函数的数据具有相同的生命周期。这很重要！切片所引用的数据需要是有效的，引用才是有效的；如果编译器假设我们是在对 `query` 而不是 `contents` 进行字符串切片，它将进行错误的安全检查。

如果我们忘记了生命周期注释并尝试编译这个函数，我们会得到这个错误：

```bash
error[E0106]: missing lifetime specifier
  --> src/lib.rs:31:10
   |
29 |     query: &str,
   |            ----
30 |     contents: &str,
   |               ----
31 | ) -> Vec<&str> {
   |          ^ expected named lifetime parameter
   |
   = help: this function's return type contains a borrowed value, but the
signature does not say whether it is borrowed from `query` or `contents`
help: consider introducing a named lifetime parameter
   |
28 ~ pub fn search<'a>(
29 ~     query: &'a str,
30 ~     contents: &'a str,
31 ~ ) -> Vec<&'a str> {
   |
```

Rust 不可能知道我们需要两个参数中的哪一个，所以我们需要明确地告诉它。因为 `contents` 是包含我们所有文本的参数，并且我们想要返回该文本中匹配的部分，所以我们知道 `contents` 是应该使用生命周期语法与返回值相关联的参数。

其他编程语言不要求在签名中连接参数和返回值，但随着时间的推移，这种做法会变得更容易。你可能想将这个例子与“使用生命周期验证引用”中的例子进行比较。

现在让我们运行测试：

```bash
[object Object]
```

很好，测试失败了，正如我们所期望的。让我们让测试通过！
