# 使用迭代器适配器使代码更清晰

我们还可以在 I/O 项目的 `search` 函数中利用迭代器，清单 13-21 重现了清单 12-19 中的 `search` 函数。

文件名：`src/lib.rs`

```rust
pub fn search<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    let mut results = Vec::new();

    for line in contents.lines() {
        if line.contains(query) {
            results.push(line);
        }
    }

    results
}
```

清单 13-21：清单 12-19 中 `search` 函数的实现

我们可以使用迭代器适配器方法以更简洁的方式编写这段代码。这样做还能让我们避免使用可变的中间 `results` 向量。函数式编程风格倾向于尽量减少可变状态的数量，以使代码更清晰。移除可变状态可能会为未来的增强功能提供便利，比如实现并行搜索，因为我们无需管理对 `results` 向量的并发访问。清单 13-22 展示了这一变化。

文件名：`src/lib.rs`

```rust
pub fn search<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    contents
     .lines()
     .filter(|line| line.contains(query))
     .collect()
}
```

清单 13-22：在 `search` 函数的实现中使用迭代器适配器方法

回想一下，`search` 函数的目的是返回 `contents` 中所有包含 `query` 的行。与清单 13-16 中的 `filter` 示例类似，这段代码使用 `filter` 适配器只保留那些 `line.contains(query)` 返回 `true` 的行。然后我们使用 `collect` 将匹配的行收集到另一个向量中。简单多了！你也可以对 `search_case_insensitive` 函数做同样的更改，以使用迭代器方法。
