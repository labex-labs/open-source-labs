# 使用 `else if` 处理多个条件

你可以通过在 `else if` 表达式中组合 `if` 和 `else` 来使用多个条件。例如：

文件名：`src/main.rs`

```rust
fn main() {
    let number = 6;

    if number % 4 == 0 {
        println!("数字能被 4 整除");
    } else if number % 3 == 0 {
        println!("数字能被 3 整除");
    } else if number % 2 == 0 {
        println!("数字能被 2 整除");
    } else {
        println!("数字不能被 4、3 或 2 整除");
    }
}
```

这个程序有四种可能的执行路径。运行它之后，你应该会看到以下输出：

```bash
$ cargo run
   正在编译 branches v0.1.0 (file:///projects/branches)
    已完成开发 [未优化 + 调试信息] 目标，耗时 0.31 秒
     正在运行 `target/debug/branches`
数字能被 3 整除
```

当这个程序执行时，它会依次检查每个 `if` 表达式，并执行条件计算结果为 `true` 的第一个代码块。请注意，尽管 6 能被 2 整除，但我们没有看到输出“数字能被 2 整除”，也没有看到 `else` 块中的“数字不能被 4、3 或 2 整除”文本。这是因为 Rust 只执行第一个 `true` 条件的代码块，一旦找到一个，它甚至不会检查其余的条件。

使用过多的 `else if` 表达式会使你的代码变得杂乱，所以如果你有多个 `else if` 表达式，你可能需要重构你的代码。第 6 章介绍了一种强大的 Rust 分支结构，称为 `match`，适用于这些情况。
