# 构建并运行一个 Cargo 项目

现在让我们看看使用 Cargo 构建和运行“你好，世界！”程序时有什么不同！在你的`hello_cargo`目录中，通过输入以下命令来构建你的项目：

```bash
$ cargo build
   Compiling hello_cargo v0.1.0 (file:///projects/hello_cargo)
    Finished dev [unoptimized + debuginfo] target(s) in 2.85 secs
```

此命令会在`target/debug/hello_cargo`中创建一个可执行文件，而不是在当前目录中。因为默认构建是调试构建，所以 Cargo 将二进制文件放在名为`debug`的目录中。你可以使用以下命令运行该可执行文件：

```bash
$./target/debug/hello_cargo
Hello, world!
```

如果一切顺利，“你好，世界！”应该会打印到终端。第一次运行`cargo build`时，Cargo 还会在顶级目录创建一个新文件：_Cargo.lock_。此文件会记录项目中依赖项的确切版本。这个项目没有依赖项，所以该文件内容有点少。你永远不需要手动更改此文件；Cargo 会为你管理其内容。

我们刚刚使用`cargo build`构建了一个项目，并使用`./target/debug/hello_cargo`运行了它，但我们也可以使用`cargo run`在一个命令中编译代码并运行生成的可执行文件：

```bash
$ cargo run
    Finished dev [unoptimized + debuginfo] target(s) in 0.0 secs
     Running `target/debug/hello_cargo`
Hello, world!
```

使用`cargo run`比必须记住先运行`cargo build`然后再使用二进制文件的完整路径更方便，所以大多数开发者使用`cargo run`。

注意，这次我们没有看到表明 Cargo 正在编译`hello_cargo`的输出。Cargo 发现文件没有更改，所以它没有重新构建，只是运行了二进制文件。如果你修改了源代码，Cargo 会在运行之前重新构建项目，你会看到如下输出：

```bash
$ cargo run
   Compiling hello_cargo v0.1.0 (file:///projects/hello_cargo)
    Finished dev [unoptimized + debuginfo] target(s) in 0.33 secs
     Running `target/debug/hello_cargo`
Hello, world!
```

Cargo 还提供了一个名为`cargo check`的命令。此命令会快速检查你的代码以确保它能编译，但不会生成可执行文件：

```bash
$ cargo check
   Checking hello_cargo v0.1.0 (file:///projects/hello_cargo)
    Finished dev [unoptimized + debuginfo] target(s) in 0.32 secs
```

为什么你可能不想要一个可执行文件呢？通常，`cargo check`比`cargo build`快得多，因为它跳过了生成可执行文件的步骤。如果你在编写代码时不断检查工作，使用`cargo check`会加快让你知道项目是否仍能编译的过程！因此，许多 Rust 开发者在编写程序时会定期运行`cargo check`以确保它能编译。然后当他们准备好使用可执行文件时，再运行`cargo build`。

让我们回顾一下到目前为止我们学到的关于 Cargo 的知识：

- 我们可以使用`cargo new`创建一个项目。
- 我们可以使用`cargo build`构建一个项目。
- 我们可以使用`cargo run`在一步中构建并运行一个项目。
- 我们可以使用`cargo check`构建一个项目而不生成二进制文件来检查错误。
- Cargo 不是将构建结果保存在与我们代码相同的目录中，而是将其存储在`target/debug`目录中。

使用 Cargo 的另一个优点是，无论你在哪个操作系统上工作，命令都是相同的。所以，从现在起，我们将不再针对 Linux、macOS 和 Windows 提供具体的操作说明。
