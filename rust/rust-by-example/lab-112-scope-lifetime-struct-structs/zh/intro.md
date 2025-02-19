# 简介

在这个实验中，我们有一些 Rust 代码展示了结构体中生命周期的用法。代码包含一个名为 `Borrowed` 的结构体，它持有一个指向 `i32` 的引用，并且该引用的生命周期必须长于结构体本身。还有一个名为 `NamedBorrowed` 的结构体，它有两个指向 `i32` 的引用，这两个引用的生命周期都必须长于结构体。此外，有一个名为 `Either` 的枚举，它可以是一个 `i32` 或者是一个指向 `i32` 的引用，并且该引用的生命周期必须长于枚举。最后，代码创建了这些结构体和枚举的实例，并打印它们的内容以展示 Rust 中生命周期的用法。

> **注意**：如果实验未指定文件名，你可以使用任何你想要的文件名。例如，你可以使用 `main.rs`，通过 `rustc main.rs &&./main` 来编译并运行它。
