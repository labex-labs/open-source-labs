# 接受命令行参数

和往常一样，让我们使用 `cargo new` 创建一个新项目。我们将把项目命名为 `minigrep`，以便将它与你系统上可能已有的 `grep` 工具区分开来。

```bash
$ cargo new minigrep
     Created binary (application) `minigrep` project
$ cd minigrep
```

首要任务是让 `minigrep` 接受它的两个命令行参数：文件路径和要搜索的字符串。也就是说，我们希望能够使用 `cargo run` 运行程序，两个连字符表示接下来的参数是给我们的程序的，而不是给 `cargo` 的，一个要搜索的字符串，以及一个要在其中搜索的文件路径，如下所示：

```bash
cargo run -- searchstring example-filename.txt
```

目前，`cargo new` 生成的程序无法处理我们给它的参数。*https://crates.io* 上的一些现有库可以帮助编写接受命令行参数的程序，但由于你刚刚在学习这个概念，我们自己来实现这个功能。
