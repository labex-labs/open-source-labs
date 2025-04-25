# 函数

函数在 Rust 代码中很常见。你已经见过该语言中最重要的函数之一：`main` 函数，它是许多程序的入口点。你也见过 `fn` 关键字，它允许你声明新函数。

创建一个名为 `functions` 的新项目：

```bash
cargo new functions
cd functions
```

Rust 代码使用**蛇形命名法**作为函数和变量名的传统风格，即所有字母均为小写，单词之间以下划线分隔。下面是一个包含示例函数定义的程序：

文件名：`src/main.rs`

```rust
fn main() {
    println!("Hello, world!");

    another_function();
}

fn another_function() {
    println!("Another function.");
}
```

我们通过输入 `fn` 后跟函数名和一组括号来在 Rust 中定义函数。花括号告诉编译器函数体从哪里开始和结束。

我们可以通过输入函数名后跟一组括号来调用我们定义的任何函数。因为 `another_function` 在程序中定义，所以可以在 `main` 函数内部调用它。请注意，我们在源代码中 `main` 函数**之后**定义了 `another_function`；我们也可以在之前定义它。Rust 并不关心你在哪里定义函数，只关心它们在调用者可见的某个作用域中被定义。

让我们启动一个名为 _functions_ 的新二进制项目，进一步探索函数。将 `another_function` 示例放入 `src/main.rs` 并运行它。你应该会看到以下输出：

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
    Finished dev [unoptimized + debuginfo] target(s) in 0.28s
     Running `target/debug/functions`
Hello, world!
Another function.
```

这些行按照它们在 `main` 函数中出现的顺序执行。首先打印“Hello, world!”消息，然后调用 `another_function` 并打印其消息。
