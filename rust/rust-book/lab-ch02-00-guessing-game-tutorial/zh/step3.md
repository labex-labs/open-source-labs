# 处理猜测

猜数字游戏程序的第一部分将要求用户输入，处理该输入，并检查输入是否符合预期格式。首先，我们将允许玩家输入猜测。将清单 2-1 中的代码输入到 `src/main.rs` 中。

文件名：`src/main.rs`

```rust
use std::io;

fn main() {
    println!("Guess the number!");

    println!("Please input your guess.");

    let mut guess = String::new();

    io::stdin()
     .read_line(&mut guess)
     .expect("Failed to read line");

    println!("You guessed: {guess}");
}
```

清单 2-1：从用户获取猜测并打印的代码

这段代码包含了很多信息，所以让我们逐行分析。为了获取用户输入并将结果作为输出打印出来，我们需要将 `io` 输入/输出库引入作用域。`io` 库来自标准库 `std`：

```rust
use std::io;
```

默认情况下，Rust 在标准库中定义了一组项，并将其引入每个程序的作用域。这组项被称为 _标准 prelude_，你可以在 *https://doc.rust-lang.org/std/prelude/index.html* 查看其中的所有内容。

如果你想要使用的类型不在 prelude 中，你必须使用 `use` 语句将该类型显式引入作用域。使用 `std::io` 库为你提供了许多有用的功能，包括接受用户输入的能力。

正如你在第一章中看到的，`main` 函数是程序的入口点：

```rust
fn main() {
```

`fn` 语法声明一个新函数；括号 `()` 表示没有参数；花括号 `{` 开始函数体。

同样在第一章中你学到，`println!` 是一个宏，用于将字符串打印到屏幕上：

```rust
println!("Guess the number!");

println!("Please input your guess.");
```

这段代码打印了一个提示，说明游戏是什么，并请求用户输入。
