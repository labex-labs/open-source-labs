# 简介

在本实验中，我们将探索在 Rust 的 `HashMap` 中使用替代/自定义键类型，这些类型可以包括实现 `Eq` 和 `Hash` 特性的类型，如 `bool`、`int`、`uint`、`String` 和 `&str`。此外，我们可以通过使用 `#[derive(PartialEq, Eq, Hash)]` 属性为自定义类型实现这些特性，从而允许它们在 `HashMap` 中用作键。

> **注意**：如果实验未指定文件名，你可以使用任何你想要的文件名。例如，你可以使用 `main.rs`，并通过 `rustc main.rs &&./main` 进行编译和运行。
