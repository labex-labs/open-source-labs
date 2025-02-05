# 调用 Config::build 并处理错误

为了处理错误情况并打印用户友好的消息，我们需要更新 `main` 函数来处理 `Config::build` 返回的 `Result`，如清单 12-10 所示。我们还将退出命令行工具并返回非零错误码的责任从 `panic!` 中移除，而是手动实现它。非零退出状态是一种约定，用于向调用我们程序的进程表明程序以错误状态退出。

文件名：`src/main.rs`

```rust
1 use std::process;

fn main() {
    let args: Vec<String> = env::args().collect();

  2 let config = Config::build(&args).3 unwrap_or_else(|4 err| {
      5 println!("Problem parsing arguments: {err}");
      6 process::exit(1);
    });

    --snip--
```

清单 12-10：如果构建 `Config` 失败则以错误码退出

在本清单中，我们使用了一个尚未详细介绍的方法：`unwrap_or_else`，它由标准库在 `Result<T, E>` 上定义 \[2\]。使用 `unwrap_or_else` 允许我们定义一些自定义的、非 `panic!` 的错误处理。如果 `Result` 是一个 `Ok` 值，此方法的行为类似于 `unwrap`：它返回 `Ok` 所包装的内部值。然而，如果值是一个 `Err` 值，此方法会调用闭包中的代码，闭包是我们定义并作为参数传递给 `unwrap_or_else` 的匿名函数 \[3\]。我们将在第 13 章更详细地介绍闭包。目前，你只需要知道 `unwrap_or_else` 会将 `Err` 的内部值（在这种情况下是我们在清单 12-9 中添加的静态字符串 `"not enough arguments"`）作为参数 `err` 传递给我们在竖线之间出现的闭包 \[4\]。闭包中的代码在运行时可以使用 `err` 值。

我们添加了一条新的 `use` 语句，将标准库中的 `process` 引入作用域 \[1\]。在错误情况下运行的闭包中的代码只有两行：我们打印 `err` 值 \[5\]，然后调用 `process::exit` \[6\]。`process::exit` 函数将立即停止程序并返回作为退出状态码传递的数字。这类似于我们在清单 12-8 中使用的基于 `panic!` 的处理方式，但我们不再得到所有额外的输出。让我们试试：

```bash
$ cargo run
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.48s
     Running `target/debug/minigrep`
Problem parsing arguments: not enough arguments
```

很好！这个输出对我们的用户来说友好得多。
