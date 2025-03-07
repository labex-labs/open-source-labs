# 简介

在本实验中，我们将探索 Rust 中的领域特定语言（DSL）概念，这些 DSL 是嵌入在 Rust 宏中的小型“语言”。这些宏会扩展为普通的 Rust 结构，但为特定功能提供了简洁直观的语法。通过一个计算器 API 展示了一个实际示例，其中将一个表达式提供给宏，并将输出打印到控制台。这允许创建更复杂的接口，就像在 `lazy_static` 或 `clap` 等库中找到的接口一样。

> **注意**：如果实验未指定文件名，你可以使用任何你想要的文件名。例如，你可以使用 `main.rs`，并通过 `rustc main.rs &&./main` 进行编译和运行。
