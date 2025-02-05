# 创建工作区

一个 _工作区_ 是一组共享同一个 _Cargo.lock_ 文件和输出目录的包。让我们使用一个工作区来创建一个项目 —— 我们将使用简单的代码，这样就能专注于工作区的结构。构建工作区有多种方式，所以我们只展示一种常见的方式。我们将创建一个包含一个二进制包和两个库的工作区。这个二进制包将提供主要功能，并依赖于这两个库。一个库将提供一个 `add_one` 函数，另一个库提供一个 `add_two` 函数。这三个板条箱将属于同一个工作区。我们先为工作区创建一个新目录：

```bash
mkdir add
cd add
```

接下来，在 `add` 目录中，我们创建将配置整个工作区的 `Cargo.toml` 文件。这个文件不会有 `[package]` 部分。相反，它将以一个 `[workspace]` 部分开头，通过指定包含我们二进制板条箱的包的路径，我们可以将成员添加到工作区；在这种情况下，那个路径是 _adder_：

文件名：`Cargo.toml`

```toml
[workspace]

members = [
    "adder",
]
```

接下来，我们通过在 `add` 目录中运行 `cargo new` 来创建 `adder` 二进制板条箱：

```bash
$ cargo new adder
     Created binary (application) `adder` package
```

此时，我们可以通过运行 `cargo build` 来构建工作区。你 `add` 目录中的文件应该如下所示：

    ├── Cargo.lock
    ├── Cargo.toml
    ├── adder
    │   ├── Cargo.toml
    │   └── src
    │       └── main.rs
    └── target

工作区在顶层有一个 `target` 目录，编译后的工件将被放置到这个目录中；`adder` 包没有它自己的 `target` 目录。即使我们在 `adder` 目录中运行 `cargo build`，编译后的工件仍然会放在 _add/target_ 中，而不是 `add/adder/target`。Cargo 以这种方式构建工作区中的 `target` 目录，是因为工作区中的板条箱旨在相互依赖。如果每个板条箱都有自己的 `target` 目录，那么每个板条箱都必须重新编译工作区中的其他每个板条箱，以便将工件放在自己的 `target` 目录中。通过共享一个 `target` 目录，板条箱可以避免不必要的重新构建。
