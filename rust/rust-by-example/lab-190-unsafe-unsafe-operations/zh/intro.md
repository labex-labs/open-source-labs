# 简介

在本实验中，我们将探讨 Rust 中的不安全操作，这些操作用于绕过编译器保护，通常用于解引用原始指针、调用不安全函数、访问或修改静态可变变量以及实现不安全特性。在代码库中应尽量减少这些操作以确保安全性。

> **注意**：如果实验未指定文件名，你可以使用任何你想要的文件名。例如，你可以使用 `main.rs`，并通过 `rustc main.rs &&./main` 进行编译和运行。
