# 约定俗成的 Cargo

对于简单的项目，与仅使用`rustc`相比，Cargo 并没有提供太多价值，但随着你的程序变得更加复杂，它将证明其价值。一旦程序发展到多个文件或需要依赖项，让 Cargo 来协调构建就会容易得多。

尽管`hello_cargo`项目很简单，但它现在已经使用了你在 Rust 职业生涯中会用到的许多实际工具。实际上，要处理任何现有项目，你可以使用以下命令通过 Git 检出代码，切换到该项目的目录，然后进行构建：

```bash
git clone example.org/someproject
cd someproject
cargo build
```

有关 Cargo 的更多信息，请查看其文档：*https://doc.rust-lang.org/cargo* 。
