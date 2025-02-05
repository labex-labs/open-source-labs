# 修复错误处理

现在我们来处理错误处理的问题。回想一下，如果 `args` 向量中的元素少于三个，尝试访问索引为 1 或 2 的 `args` 向量中的值会导致程序恐慌。试着在不传入任何参数的情况下运行程序；它会像这样：

```bash
$ cargo run
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep`
thread 'main' panicked at 'index out of bounds: the len is 1 but
the index is 1', src/main.rs:27:21
note: run with `RUST_BACKTRACE=1` environment variable to display
a backtrace
```

“索引越界：长度为 1 但索引为 1” 这一行是给程序员的错误信息。它无助于我们的终端用户理解他们应该做什么。现在让我们来修复这个问题。
