# 使用 cargo install 安装二进制文件

`cargo install` 命令允许你在本地安装和使用二进制 crate。这并非旨在替代系统软件包；它是 Rust 开发者安装其他人在 *https://crates.io* 上共享的工具的便捷方式。请注意，你只能安装具有二进制目标的软件包。_二进制目标_ 是指如果 crate 有一个 `src/main.rs` 文件或指定为二进制文件的其他文件时创建的可运行程序，与之相对的是库目标，库目标本身不可运行，但适合包含在其他程序中。通常，crate 在 _README_ 文件中会有关于它是库、有二进制目标还是两者皆有的信息。

所有使用 `cargo install` 安装的二进制文件都存储在安装根目录的 `bin` 文件夹中。如果你使用 `rustup.rs` 安装了 Rust 且没有任何自定义配置，这个目录将是 `$HOME/.cargo/bin`。确保该目录在你的 `$PATH` 中，以便能够运行你使用 `cargo install` 安装的程序。

例如，在第 12 章中我们提到有一个名为 `ripgrep` 的 `grep` 工具的 Rust 实现，用于搜索文件。要安装 `ripgrep`，我们可以运行以下命令：

```bash
$ cargo install ripgrep
    Updating crates.io index
  Downloaded ripgrep v13.0.0
  Downloaded 1 crate (243.3 KB) in 0.88s
  Installing ripgrep v13.0.0
   --snip--
   Compiling ripgrep v13.0.0
    Finished release [optimized + debuginfo] target(s) in 3m 10s
  Installing ~/.cargo/bin/rg
   Installed package `ripgrep v13.0.0` (executable `rg`)
```

输出的倒数第二行显示了已安装二进制文件的位置和名称，对于 `ripgrep` 来说是 `rg`。如前所述，只要安装目录在你的 `$PATH` 中，你就可以运行 `rg --help` 并开始使用一个更快、更具 Rust 风格的文件搜索工具！
