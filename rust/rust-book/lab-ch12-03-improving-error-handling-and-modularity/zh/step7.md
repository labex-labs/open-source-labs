# 改进错误信息

在清单 12-8 中，我们在 `new` 函数中添加了一个检查，在访问索引 1 和索引 2 之前，会先验证切片是否足够长。如果切片不够长，程序就会恐慌并显示一个更好的错误信息。

文件名：`src/main.rs`

```rust
--snip--
fn new(args: &[String]) -> Config {
    if args.len() < 3 {
        panic!("not enough arguments");
    }
    --snip--
```

清单 12-8：添加对参数数量的检查

这段代码与我们在清单 9-13 中编写的 `Guess::new` 函数类似，在那里当 `value` 参数超出有效值范围时，我们调用了 `panic!`。在这里，我们不是检查值的范围，而是检查 `args` 的长度是否至少为 `3`，并且函数的其余部分可以在假设这个条件已经满足的情况下运行。如果 `args` 的元素少于三个，这个条件将为 `true`，我们就调用 `panic!` 宏立即结束程序。

在 `new` 函数中添加了这几行额外的代码后，让我们再次在不传入任何参数的情况下运行程序，看看现在的错误是什么样的：

```bash
$ cargo run
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep`
thread 'main' panicked at 'not enough arguments',
src/main.rs:26:13
note: run with `RUST_BACKTRACE=1` environment variable to display
a backtrace
```

这个输出更好了：我们现在有了一个合理的错误信息。然而，我们也有一些不想给用户的额外信息。也许我们在清单 9-13 中使用的技术在这里不是最好的：正如第 9 章所讨论的，调用 `panic!` 对于编程问题比对于使用问题更合适。相反，我们将使用你在第 9 章中学到的另一种技术 —— 返回一个 `Result`，它表示成功或错误。
