# 返回 Result 而非调用 panic!

我们可以改为返回一个 `Result` 值，在成功的情况下它将包含一个 `Config` 实例，在错误的情况下它将描述问题。我们还打算将函数名从 `new` 改为 `build`，因为许多程序员期望 `new` 函数永远不会失败。当 `Config::build` 与 `main` 通信时，我们可以使用 `Result` 类型来表明出现了问题。然后我们可以修改 `main` 函数，将 `Err` 变体转换为对用户来说更实用的错误信息，而不会出现调用 `panic!` 时产生的关于 `thread'main'` 和 `RUST_BACKTRACE` 的周围文本。

清单 12-9 展示了我们需要对现在称为 `Config::build` 的函数的返回值以及返回 `Result` 所需的函数体所做的更改。请注意，在我们更新 `main` 函数之前，这段代码不会编译，我们将在下一个清单中进行更新。

文件名：`src/main.rs`

```rust
impl Config {
    fn build(args: &[String]) -> Result<Config, &'static str> {
        if args.len() < 3 {
            return Err("not enough arguments");
        }

        let query = args[1].clone();
        let file_path = args[2].clone();

        Ok(Config { query, file_path })
    }
}
```

清单 12-9：从 `Config::build` 返回 `Result`

我们的 `build` 函数在成功的情况下返回一个包含 `Config` 实例的 `Result`，在错误的情况下返回一个 `&'static str`。我们的错误值将始终是具有 `'static` 生命周期的字符串字面量。

我们在函数体中做了两处更改：当用户传入的参数不足时，我们不再调用 `panic!`，而是返回一个 `Err` 值，并且我们将 `Config` 返回值包装在一个 `Ok` 中。这些更改使函数符合其新的类型签名。

从 `Config::build` 返回一个 `Err` 值允许 `main` 函数处理从 `build` 函数返回的 `Result` 值，并在错误情况下更干净地退出进程。
