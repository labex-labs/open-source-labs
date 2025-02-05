# 使用 `lines` 方法逐行遍历

Rust 有一个很有用的方法来处理字符串的逐行遍历，它的名字很方便记忆，叫做 `lines`，其工作方式如清单 12-17 所示。请注意，这段代码目前还无法编译。

文件名：`src/lib.rs`

```rust
pub fn search<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    for line in contents.lines() {
        // 对 line 进行某些操作
    }
}
```

清单 12-17：遍历 `contents` 中的每一行

`lines` 方法返回一个迭代器。我们将在第 13 章深入讨论迭代器，但回想一下，你在清单 3-5 中见过这种使用迭代器的方式，我们在那里使用了一个带有迭代器的 `for` 循环，以便对集合中的每个元素运行一些代码。
