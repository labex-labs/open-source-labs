# 简介

在本实验中，我们将学习 Rust 中的 `#[derive]` 属性，它允许编译器为某些 trait（如 `Eq`、`PartialEq`、`Ord`、`PartialOrd`、`Clone`、`Copy`、`Hash`、`Default` 和 `Debug`）提供基本实现。如果需要更复杂的行为，也可以手动实现这些 trait。本实验提供了示例代码，展示了这些 trait 在不同元组结构体（如 `Centimeters`、`Inches` 和 `Seconds`）上的用法。

> **注意**：如果实验未指定文件名，你可以使用任何你想要的文件名。例如，你可以使用 `main.rs`，并通过 `rustc main.rs &&./main` 进行编译和运行。
