# 多个模式

在 `match` 表达式中，你可以使用 `|` 语法来匹配多个模式，`|` 是模式的“或”运算符。例如，在以下代码中，我们将 `x` 的值与 `match` 分支进行匹配，第一个分支具有“或”选项，这意味着如果 `x` 的值与该分支中的任何一个值匹配，该分支的代码就会运行：

文件名：`src/main.rs`

```rust
let x = 1;

match x {
    1 | 2 => println!("one or two"),
    3 => println!("three"),
    _ => println!("anything"),
}
```

这段代码会打印出 `one or two`。
