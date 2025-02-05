# `if` 表达式

`if` 表达式允许你根据条件来使代码分支。你提供一个条件，然后声明：“如果满足这个条件，就运行这段代码块。如果条件不满足，就不运行这段代码块。”

在你的 `project` 目录下创建一个名为 `branches` 的新项目，来探索 `if` 表达式。在 `src/main.rs` 文件中，输入以下内容：

```bash
cd ~/project
cargo new branches
```

文件名：`src/main.rs`

```rust
fn main() {
    let number = 3;

    if number < 5 {
        println!("条件为真");
    } else {
        println!("条件为假");
    }
}
```

所有的 `if` 表达式都以关键字 `if` 开头，后面跟着一个条件。在这个例子中，条件检查变量 `number` 的值是否小于 5。我们将在条件为 `true` 时要执行的代码块放在条件后面的花括号内。与 `if` 表达式中的条件相关联的代码块有时被称为 _分支_，就像我们在“将猜测与秘密数字进行比较”中讨论的 `match` 表达式中的分支一样。

可选地，我们也可以包含一个 `else` 表达式，我们在这里选择这样做，以便在条件计算为 `false` 时，给程序提供一个可执行的替代代码块。如果你不提供 `else` 表达式，并且条件为 `false`，程序将直接跳过 `if` 块，继续执行下一段代码。

尝试运行这段代码；你应该会看到以下输出：

```bash
$ cargo run
   正在编译 branches v0.1.0 (file:///projects/branches)
    已完成开发 [未优化 + 调试信息] 目标，耗时 0.31 秒
     正在运行 `target/debug/branches`
条件为真
```

让我们尝试将 `number` 的值更改为使条件为 `false` 的值，看看会发生什么：

```rust
    let number = 7;
```

再次运行程序，并查看输出：

```bash
$ cargo run
   正在编译 branches v0.1.0 (file:///projects/branches)
    已完成开发 [未优化 + 调试信息] 目标，耗时 0.31 秒
     正在运行 `target/debug/branches`
条件为假
```

还值得注意的是，这段代码中的条件 _必须_ 是一个 `bool` 类型。如果条件不是 `bool` 类型，我们将会得到一个错误。例如，尝试运行以下代码：

文件名：`src/main.rs`

```rust
fn main() {
    let number = 3;

    if number {
        println!("数字是三");
    }
}
```

这次 `if` 条件计算结果为 `3`，Rust 会抛出一个错误：

```bash
$ cargo run
   正在编译 branches v0.1.0 (file:///projects/branches)
错误[E0308]：类型不匹配
 --> src/main.rs:4:8
  |
4 |     if number {
  |        ^^^^^^ 期望 `bool`，找到整数
```

该错误表明 Rust 期望一个 `bool` 类型，但得到的是一个整数。与 Ruby 和 JavaScript 等语言不同，Rust 不会自动尝试将非布尔类型转换为布尔类型。你必须明确地始终为 `if` 提供一个布尔值作为其条件。例如，如果我们希望 `if` 代码块仅在数字不等于 `0` 时运行，我们可以将 `if` 表达式更改为以下内容：

文件名：`src/main.rs`

```rust
fn main() {
    let number = 3;

    if number!= 0 {
        println!("数字不是零");
    }
}
```

运行这段代码将打印出“数字不是零”。
