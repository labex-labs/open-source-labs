# 简介

在本实验中，我们将探索 Rust 中 `TryFrom` 和 `TryInto` 的用法，它们是用于在类型之间进行可能失败的转换并返回 `Result` 类型的通用 trait。我们提供了一个示例代码片段，展示了如何实现 `TryFrom` 以将 `i32` 转换为自定义的 `EvenNumber` 结构体，然后展示如何使用 `TryFrom` 和 `TryInto` 来执行转换并处理可能的错误。

> **注意**：如果实验未指定文件名，你可以使用任何你想要的文件名。例如，你可以使用 `main.rs`，并通过 `rustc main.rs &&./main` 进行编译和运行。
