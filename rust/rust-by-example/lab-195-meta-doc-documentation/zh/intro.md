# 简介

在本实验中，你可以使用 `cargo doc` 在 `target/doc` 中生成文档。你还可以使用 `cargo test` 运行所有测试，包括文档测试，以及使用 `cargo test --doc` 仅运行文档测试。由 `///` 表示的文档注释会被 `rustdoc` 编译为文档，并支持 Markdown 格式。这些注释对于在大型项目中记录代码很有用。文档属性，如 `inline`、`no_inline` 和 `hidden`，经常与 `rustdoc` 一起使用。Rustdoc 在社区中被广泛用于生成文档，包括标准库文档。

> **注意**：如果实验未指定文件名，你可以使用任何你想要的文件名。例如，你可以使用 `main.rs`，并通过 `rustc main.rs &&./main` 进行编译和运行。
