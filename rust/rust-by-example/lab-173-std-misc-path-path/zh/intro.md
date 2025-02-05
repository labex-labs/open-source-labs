# 简介

在本实验中，我们将探索 Rust 中的 `Path` 结构体，它表示底层文件系统中的文件路径。它有两种类型：适用于类 UNIX 系统的 `posix::Path` 和适用于 Windows 的 `windows::Path`。`Path` 可以从 `OsStr` 创建，并提供各种方法来从路径指向的文件或目录中检索信息。需要注意的是，`Path` 是不可变的，其拥有的版本称为 `PathBuf`，可以在原地进行变异。`Path` 和 `PathBuf` 之间的关系类似于 `str` 和 `String` 之间的关系。

> **注意**：如果实验未指定文件名，你可以使用任何你想要的文件名。例如，你可以使用 `main.rs`，并通过 `rustc main.rs &&./main` 进行编译和运行。
