# 简介

在本实验中，将解释在 Rust 中，变量拥有资源的所有权，并且只能有一个所有者，这可防止资源被多次释放。当通过值来赋值变量或传递函数参数时，资源的所有权会被转移，这称为移动。移动之后，先前的所有者不能再使用，以避免创建悬空指针。代码示例通过展示栈分配和堆分配变量的所有权如何转移，以及在变量所有权被移动后访问该变量如何导致错误，来演示这些概念。

> **注意**：如果实验未指定文件名，你可以使用任何你想要的文件名。例如，你可以使用 `main.rs`，并通过 `rustc main.rs &&./main` 来编译和运行它。
