# 将错误信息打印到标准错误

我们将使用清单12 - 24中的代码来更改错误信息的打印方式。由于我们在本章前面进行了重构，所有打印错误信息的代码都在一个函数 `main` 中。标准库提供了 `eprintln!` 宏，它会打印到标准错误流，所以让我们将调用 `println!` 来打印错误的两个地方改为使用 `eprintln!`。

文件名：`src/main.rs`

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

    let config = Config::build(&args).unwrap_or_else(|err| {
        eprintln!("Problem parsing arguments: {err}");
        process::exit(1);
    });

    if let Err(e) = minigrep::run(config) {
        eprintln!("Application error: {e}");
        process::exit(1);
    }
}
```

清单12 - 24：使用 `eprintln!` 将错误信息写入标准错误而非标准输出

现在让我们再次以相同的方式运行程序，不传递任何参数，并使用 `>` 重定向标准输出：

```bash
$ cargo run > output.txt
Problem parsing arguments: not enough arguments
```

现在我们在屏幕上看到了错误，并且 `output.txt` 中没有任何内容，这是我们对命令行程序所期望的行为。

让我们再次使用不会导致错误但仍将标准输出重定向到文件的参数来运行程序，如下所示：

```bash
cargo run -- to poem.txt > output.txt
```

我们不会在终端看到任何输出，并且 `output.txt` 将包含我们的结果：

文件名：output.txt

```rust
Are you nobody, too?
How dreary to be somebody!
```

这表明我们现在已将标准输出用于成功输出，将标准错误用于错误输出，一切都恰到好处。
