# 使用 Cargo 创建项目

让我们使用 Cargo 创建一个新项目，并看看它与我们最初的“你好，世界！”项目有何不同。导航回你的`project`目录（或者你决定存储代码的任何地方）。然后，在任何操作系统上，运行以下命令：

```bash
cd ~/project
cargo new hello_cargo
cd hello_cargo
```

第一个命令创建了一个名为*hello_cargo*的新目录和项目。我们将项目命名为*hello_cargo*，Cargo 会在同名目录中创建其文件。

进入`hello_cargo`目录并列出文件。你会看到 Cargo 为我们生成了两个文件和一个目录：一个`Cargo.toml`文件以及一个包含`main.rs`文件的`src`目录。

它还初始化了一个新的 Git 仓库以及一个*.gitignore*文件。如果你在现有 Git 仓库中运行`cargo new`，则不会生成 Git 文件；你可以使用`cargo new --vcs=git`覆盖此行为。

> 注意：Git 是一种常见的版本控制系统。你可以通过使用`--vcs`标志来更改`cargo new`以使用不同的版本控制系统或不使用版本控制系统。运行`cargo new --help`以查看可用选项。

在你选择的文本编辑器中打开`Cargo.toml`。它应该类似于清单 1-2 中的代码。

文件名：`Cargo.toml`

```toml
[package]
name = "hello_cargo"
version = "0.1.0"
edition = "2021"

[dependencies]
```

清单 1-2：`cargo new`生成的`Cargo.toml`的内容

此文件采用*TOML*（_Tom's Obvious, Minimal Language_）格式，这是 Cargo 的配置格式。

第一行`[package]`是一个节标题，表示以下语句正在配置一个包。随着我们向此文件中添加更多信息，我们将添加其他节。

接下来的三行设置了 Cargo 编译你的程序所需的配置信息：名称、版本以及要使用的 Rust 版本。我们将在附录 E 中讨论`edition`键。

最后一行`[dependencies]`是一个节的开始，供你列出项目的任何依赖项。在 Rust 中，代码包被称为*板条箱（crates）*。这个项目我们不需要任何其他板条箱，但在第 2 章的第一个项目中我们会需要，所以到时候我们会使用这个依赖项部分。

现在打开`src/main.rs`并看一看：

文件名：`src/main.rs`

```rust
fn main() {
    println!("Hello, world!");
}
```

Cargo 为你生成了一个“你好，世界！”程序，就像我们在清单 1-1 中编写的一样！到目前为止，我们的项目与 Cargo 生成的项目之间的区别在于，Cargo 将代码放在了`src`目录中，并且我们在顶级目录中有一个`Cargo.toml`配置文件。

Cargo 期望你的源文件位于`src`目录内。顶级项目目录仅用于 README 文件、许可信息、配置文件以及任何与你的代码无关的其他内容。使用 Cargo 有助于你组织项目。一切都有其位置，并且一切都在其应在的位置。

如果你启动了一个不使用 Cargo 的项目，就像我们对“你好，世界！”项目所做的那样，你可以将其转换为一个使用 Cargo 的项目。将项目代码移动到`src`目录中，并创建一个合适的`Cargo.toml`文件。
