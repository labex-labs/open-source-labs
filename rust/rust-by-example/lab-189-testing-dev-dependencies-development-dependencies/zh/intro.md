# 简介

在本实验中，将解释开发依赖项的概念。开发依赖项添加在 `Cargo.toml` 文件的 `[dev-dependencies]` 部分中，用于测试、示例或基准测试。开发依赖项的一个示例是 `pretty_assertions`，它扩展了标准宏，如 `assert_eq!` 和 `assert_ne!`，以提供彩色差异。

> **注意**：如果实验未指定文件名，你可以使用任何你想要的文件名。例如，你可以使用 `main.rs`，并通过 `rustc main.rs &&./main` 进行编译和运行。
