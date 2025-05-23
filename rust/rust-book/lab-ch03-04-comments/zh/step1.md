# 注释

所有程序员都努力使自己的代码易于理解，但有时需要额外的解释。在这种情况下，程序员会在源代码中留下**注释**，编译器会忽略这些注释，但阅读源代码的人可能会觉得很有用。

下面是一个简单的注释：

```rust
// 你好，世界
```

在 Rust 中，惯用的注释风格是以两个斜杠开始注释，注释会一直延续到该行结束。对于跨行的注释，你需要在每行都加上 `//`，如下所示：

    // 所以我们在这里做一些复杂的事情，长到需要
    // 多行注释来完成！呼！希望这个注释能
    // 解释清楚发生了什么。

注释也可以放在包含代码的行尾：

文件名：`src/main.rs`

```rust
fn main() {
    let lucky_number = 7; // 我今天感觉很幸运
}
```

但你会更经常看到它们以这种格式使用，注释在它所注释的代码上方的单独一行：

文件名：`src/main.rs`

```rust
fn main() {
    // 我今天感觉很幸运
    let lucky_number = 7;
}
```

Rust 还有另一种注释，即文档注释，我们将在“将一个 Crate 发布到 Crates.io”中讨论。
