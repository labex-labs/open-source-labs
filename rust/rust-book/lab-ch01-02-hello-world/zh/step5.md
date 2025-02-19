# 编译和运行是分开的步骤

你刚刚运行了一个新创建的程序，那么让我们来研究一下这个过程中的每一个步骤。

在运行 Rust 程序之前，你必须使用 Rust 编译器通过输入 `rustc` 命令并将源文件名传递给它来进行编译，如下所示：

```bash
rustc main.rs
```

如果你有 C 或 C++ 背景，你会注意到这与 `gcc` 或 `clang` 类似。成功编译后，Rust 会输出一个二进制可执行文件。

在 Linux、macOS 和 Windows 上的 PowerShell 中，你可以通过在 shell 中输入 `ls` 命令来查看可执行文件：

```bash
$ ls
main main.rs
```

从这里开始，你可以运行 `main` 文件，如下所示：

```bash
./main
```

如果你的 `main.rs` 是你的“你好，世界！”程序，这一行会在你的终端上打印“你好，世界！”。

如果你更熟悉动态语言，如 Ruby、Python 或 JavaScript，你可能不习惯将编译和运行程序作为分开的步骤。Rust 是一种**提前编译**的语言，这意味着你可以编译一个程序并将可执行文件交给其他人，即使他们没有安装 Rust，他们也可以运行它。如果你给某人一个 `.rb`、`.py` 或 `.js` 文件，他们需要分别安装 Ruby、Python 或 JavaScript 实现。但在那些语言中，你只需要一个命令来编译和运行你的程序。在语言设计中，一切都是权衡取舍。

对于简单的程序，仅使用 `rustc` 进行编译就可以了，但随着项目的发展，你会希望管理所有选项并便于共享你的代码。接下来，我们将向你介绍 Cargo 工具，它将帮助你编写实际的 Rust 程序。
