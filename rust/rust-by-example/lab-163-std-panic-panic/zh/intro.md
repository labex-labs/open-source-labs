# 简介

在本实验中，我们将学习 Rust 中的 `panic!` 宏，它可用于引发恐慌并开始展开堆栈，导致程序报告恐慌消息并退出。运行时会通过调用对象的析构函数来释放线程拥有的所有资源。我们还将查看一个使用 `panic!` 宏处理除零错误的示例，并使用 Valgrind 验证它不会导致内存泄漏。

> **注意**：如果实验未指定文件名，你可以使用任何你想要的文件名。例如，你可以使用 `main.rs`，并通过 `rustc main.rs &&./main` 进行编译和运行。
