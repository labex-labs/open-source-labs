# 在 `run` 函数中使用 `search` 函数

既然 `search` 函数已经可以正常工作并通过了测试，我们需要在 `run` 函数中调用 `search`。我们需要将 `config.query` 的值以及 `run` 从文件中读取的 `contents` 传递给 `search` 函数。然后 `run` 将打印从 `search` 返回的每一行：

文件名：`src/lib.rs`

```rust
pub fn run(config: Config) -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string(config.file_path)?;

    for line in search(&config.query, &contents) {
        println!("{line}");
    }

    Ok(())
}
```

我们仍然使用 `for` 循环来返回 `search` 中的每一行并打印它。

现在整个程序应该可以正常工作了！让我们来测试一下，首先使用一个应该从艾米莉·狄金森的诗中精确返回一行的词：“frog”。

```bash
$ cargo run -- frog poem.txt
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.38s
     Running `target/debug/minigrep frog poem.txt`
How public, like a frog
```

很酷！现在让我们尝试一个会匹配多行的词，比如“body”：

```bash
$ cargo run -- body poem.txt
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep body poem.txt`
I'm nobody! Who are you?
Are you nobody, too?
How dreary to be somebody!
```

最后，让我们确保在搜索诗中不存在的词（比如“monomorphization”）时不会得到任何行：

```bash
$ cargo run -- monomorphization poem.txt
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep monomorphization poem.txt`
```

太棒了！我们构建了自己的经典工具的迷你版本，并学到了很多关于如何构建应用程序的知识。我们还学到了一些关于文件输入输出、生命周期、测试和命令行解析的知识。

为了完善这个项目，我们将简要演示如何使用环境变量以及如何打印到标准错误，这两者在编写命令行程序时都很有用。
