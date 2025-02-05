# 布尔类型

和大多数其他编程语言一样，Rust 中的布尔类型有两个可能的值：`true` 和 `false`。布尔值的大小为一个字节。Rust 中的布尔类型使用 `bool` 来指定。例如：

文件名：`src/main.rs`

```rust
fn main() {
    let t = true;

    let f: bool = false; // 带有显式类型标注
}
```

使用布尔值的主要方式是通过条件语句，比如 `if` 表达式。我们将在“控制流”一章中介绍 `if` 表达式在 Rust 中的工作方式。
