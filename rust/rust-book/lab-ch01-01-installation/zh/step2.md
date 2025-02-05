# 在 Linux 或 macOS 上安装 rustup

如果你使用的是 Linux 或 macOS，打开一个终端并输入以下命令：

```bash
curl --proto '=https' --tlsv1.3 https://sh.rustup.rs -sSf | sh
```

该命令会下载一个脚本并开始安装 `rustup` 工具，它会安装 Rust 的最新稳定版本。系统可能会提示你输入密码。如果安装成功，将会出现以下内容：

```rust
Rust is installed now. Great!
```

你还需要一个**链接器**，它是 Rust 用来将其编译输出合并为一个文件的程序。你可能已经有一个了。如果你遇到链接器错误，应该安装一个 C 编译器，它通常会包含一个链接器。C 编译器也很有用，因为一些常见的 Rust 包依赖于 C 代码，并且需要一个 C 编译器。

Linux 用户通常应根据其发行版的文档安装 GCC 或 Clang。例如，如果你使用的是 Ubuntu，可以安装 `build-essential` 包。
