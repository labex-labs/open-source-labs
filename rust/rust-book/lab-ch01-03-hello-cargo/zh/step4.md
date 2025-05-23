# 发布版本构建

当你的项目最终准备好发布时，可以使用`cargo build --release`来进行优化编译。

```bash
cargo build --release
```

此命令会在`target/release`目录中创建一个可执行文件，而不是在`target/debug`目录。优化会使你的 Rust 代码运行得更快，但开启优化会延长程序的编译时间。这就是为什么有两种不同的配置文件：一种用于开发，此时你希望快速且频繁地重新构建；另一种用于构建最终提供给用户的程序，该程序不会被反复重新构建，并且会尽可能快地运行。如果你正在对代码的运行时间进行基准测试，请务必运行`cargo build --release`并使用`target/release`目录中的可执行文件进行基准测试。
