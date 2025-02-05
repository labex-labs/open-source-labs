# 变量与可变性

正如在“使用变量存储值”中提到的，默认情况下，变量是不可变的。这是 Rust 引导你以利用其提供的安全性和易于并发的方式编写代码的众多方式之一。不过，你仍然可以选择使变量可变。让我们来探讨一下 Rust 如何以及为何鼓励你倾向于使用不可变性，以及为何有时你可能想要选择可变。

当一个变量是不可变的时，一旦一个值绑定到一个名称，你就不能更改该值。为了说明这一点，通过使用 `cargo new variables` 在你的 `project` 目录中生成一个名为 `_variables_` 的新项目。

然后，在你新的 `variables` 目录中，打开 `src/main.rs` 并将其代码替换为以下代码，这段代码目前还无法编译：

文件名：`src/main.rs`

```rust
fn main() {
    let x = 5;
    println!("The value of x is: {x}");
    x = 6;
    println!("The value of x is: {x}");
}
```

保存并使用 `cargo run` 运行该程序。你应该会收到一条关于不可变性错误的错误消息，如下所示：

```bash
$ cargo run
   Compiling variables v0.1.0 (file:///projects/variables)
error[E0384]: cannot assign twice to immutable variable `x`
 --> src/main.rs:4:5
  |
2 |     let x = 5;
  |         -
  |         |
  |         first assignment to `x`
  |         help: consider making this binding mutable: `mut x`
3 |     println!("The value of x is: {x}");
4 |     x = 6;
  |     ^^^^^ cannot assign twice to immutable variable
```

这个例子展示了编译器如何帮助你在程序中发现错误。编译器错误可能会令人沮丧，但实际上它们仅仅意味着你的程序尚未安全地完成你想要它做的事情；它们并不意味着你不是一个好程序员！经验丰富的 Rust 开发者仍然会遇到编译器错误。

你收到错误消息“不能对不可变变量 `x` 进行两次赋值”，是因为你试图对不可变的 `x` 变量赋第二个值。

当我们尝试更改被指定为不可变的值时会得到编译时错误，这一点很重要，因为这种情况可能会导致错误。如果我们代码的一部分基于某个值永远不会改变的假设进行操作，而另一部分代码更改了该值，那么代码的第一部分可能无法按预期运行。这种错误的原因在事后可能很难追查，尤其是当第二部分代码只是有时更改该值时。Rust 编译器保证当你声明一个值不会改变时，它真的不会改变，所以你不必自己去跟踪它。因此，你的代码更易于理解。

但是可变性可能非常有用，并且可以使代码编写起来更方便。虽然变量默认是不可变的，但你可以像在第 2 章中那样，通过在变量名前添加 `mut` 使其可变。添加 `mut` 还通过表明代码的其他部分将更改此变量的值，向代码的未来读者传达了意图。

例如，让我们将 `src/main.rs` 更改为以下内容：

文件名：`src/main.rs`

```rust
fn main() {
    let mut x = 5;
    println!("The value of x is: {x}");
    x = 6;
    println!("The value of x is: {x}");
}
```

现在当我们运行程序时，会得到如下结果：

```bash
$ cargo run
   Compiling variables v0.1.0 (file:///projects/variables)
    Finished dev [unoptimized + debuginfo] target(s) in 0.30s
     Running `target/debug/variables`
The value of x is: 5
The value of x is: 6
```

当使用 `mut` 时，我们可以将绑定到 `x` 的值从 `5` 更改为 `6`。最终，决定是否使用可变性取决于你，并且取决于你认为在特定情况下哪种方式最清晰。
