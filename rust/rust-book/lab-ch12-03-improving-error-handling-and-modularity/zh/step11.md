# 从 run 函数返回错误

随着程序的其余逻辑被分离到 `run` 函数中，我们可以改进错误处理，就像我们在清单 12-9 中对 `Config::build` 所做的那样。当出现问题时，`run` 函数将不再通过调用 `expect` 使程序恐慌，而是返回一个 `Result<T, E>`。这将使我们能够以用户友好的方式进一步将错误处理逻辑整合到 `main` 函数中。清单 12-12 展示了我们需要对 `run` 函数的签名和主体所做的更改。

文件名：`src/main.rs`

```rust
1 use std::error::Error;

--snip--

2 fn run(config: Config) -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string(config.file_path)3?;

    println!("With text:\n{contents}");

  4 Ok(())
}
```

清单 12-12：更改 `run` 函数以返回 `Result`

我们在这里做了三个重大更改。首先，我们将 `run` 函数的返回类型更改为 `Result<(), Box<dyn Error>>` \[2\]。这个函数之前返回单元类型 `()`，我们在 `Ok` 情况下仍然返回这个值。

对于错误类型，我们使用了 trait 对象 `Box<dyn Error>`（并且我们在顶部使用 `use` 语句将 `std::error::Error` 引入作用域 \[1\]）。我们将在第 17 章介绍 trait 对象。目前，只需知道 `Box<dyn Error>` 意味着该函数将返回一个实现 `Error` trait 的类型，但我们不必指定返回值将是哪种具体类型。这使我们能够灵活地在不同的错误情况下返回可能不同类型的错误值。`dyn` 关键字是 _dynamic_ 的缩写。

其次，我们删除了对 `expect` 的调用，转而使用 `?` 运算符 \[3\]，就像我们在第 9 章中讨论的那样。`?` 不会在错误时使程序恐慌，而是会从当前函数返回错误值供调用者处理。

第三，`run` 函数现在在成功情况下返回一个 `Ok` 值 \[4\]。我们在签名中将 `run` 函数的成功类型声明为 `()`，这意味着我们需要将单元类型值包装在 `Ok` 值中。这种 `Ok(())` 语法乍一看可能有点奇怪，但像这样使用 `()` 是表示我们调用 `run` 只是为了其副作用的惯用方式；它不会返回我们需要的值。

当你运行这段代码时，它会编译，但会显示一个警告：

    warning: unused `Result` that must be used
      --> src/main.rs:19:5
       |
    19 |     run(config);
       |     ^^^^^^^^^^^^
       |
       = note: `#[warn(unused_must_use)]` on by default
       = note: this `Result` may be an `Err` variant, which should be
    handled

Rust 告诉我们，我们的代码忽略了 `Result` 值，并且这个 `Result` 值可能表示发生了错误。但是我们没有检查是否发生了错误，编译器提醒我们这里可能应该有一些错误处理代码！现在让我们纠正这个问题。
