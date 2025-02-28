# 简介

在本实验中，我们将探索 Rust 编程语言使用 map-reduce 算法并行化数据处理的能力。示例代码通过将数据分成多个段，并在单独的线程中处理每个段，来计算一组数字中所有数字的总和。Rust 标准库提供了防止数据竞争并保证线程安全的线程原语。该程序还展示了 Rust 对跨线程边界传递只读引用的理解。此外，代码展示了如何使用闭包、迭代器和 join() 方法将每个线程的中间结果组合成最终的总和。为了确保效率，可以修改程序，将数据分块成有限数量的段，而不是依赖于可能导致过多线程的用户输入数据。

> **注意**：如果实验未指定文件名，你可以使用任何你想要的文件名。例如，你可以使用 `main.rs`，并通过 `rustc main.rs &&./main` 进行编译和运行。
