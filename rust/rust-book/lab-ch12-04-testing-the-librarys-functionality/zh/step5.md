# 在每一行中搜索查询字符串

接下来，我们将检查当前行是否包含我们的查询字符串。幸运的是，字符串有一个很有用的方法叫做 `contains`，它可以为我们完成这项工作！在 `search` 函数中添加对 `contains` 方法的调用，如清单 12-18 所示。请注意，这段代码仍然无法编译。

文件名：`src/lib.rs`

```rust
pub fn search<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    for line in contents.lines() {
        if line.contains(query) {
            // 对 line 进行某些操作
        }
    }
}
```

清单 12-18：添加功能以查看该行是否包含 `query` 中的字符串

目前，我们正在逐步构建功能。为了使代码能够编译，我们需要按照函数签名中的指示从函数体返回一个值。
