# 包与板条箱

我们要介绍的模块系统的第一部分是包和板条箱。

一个「板条箱（crate）」是 Rust 编译器每次处理的最小代码单元。即使你运行 `rustc` 而不是 `cargo` 并传递单个源代码文件（就像我们在「编写并运行 Rust 程序」中所做的那样），编译器也会将该文件视为一个板条箱。板条箱可以包含模块，并且这些模块可能在与板条箱一起编译的其他文件中定义，我们将在后续章节中看到。

板条箱有两种形式：可执行板条箱或库板条箱。「可执行板条箱（Binary crates）」是你可以编译为可运行的可执行文件的程序，例如命令行程序或服务器。每个可执行板条箱都必须有一个名为 `main` 的函数，该函数定义了可执行文件运行时会发生什么。到目前为止我们创建的所有板条箱都是可执行板条箱。

「库板条箱（Library crates）」没有 `main` 函数，也不会编译为可执行文件。相反，它们定义了旨在与多个项目共享的功能。例如，我们在第 2 章中使用的 `rand` 板条箱提供了生成随机数的功能。大多数时候，Rust 开发者说「板条箱（crate）」时，他们指的是库板条箱，并且他们将「板条箱（crate）」与一般编程概念中的「库」互换使用。

「板条箱根（crate root）」是 Rust 编译器开始处理的源文件，它构成了你板条箱的根模块（我们将在「定义模块以控制作用域和隐私」中深入解释模块）。

一个「包（package）」是一个或多个板条箱的捆绑，提供一组功能。一个包包含一个 `Cargo.toml` 文件，该文件描述了如何构建这些板条箱。Cargo 实际上是一个包，它包含了你一直在使用的用于构建代码的命令行工具的可执行板条箱。Cargo 包还包含一个库板条箱，可执行板条箱依赖于该库板条箱。其他项目可以依赖于 Cargo 库板条箱来使用与 Cargo 命令行工具相同的逻辑。

板条箱有两种形式：可执行板条箱或库板条箱。一个包可以包含任意数量的可执行板条箱，但最多只能有一个库板条箱。一个包必须至少包含一个板条箱，无论是库板条箱还是可执行板条箱。

让我们来看看创建一个包时会发生什么。首先，我们输入命令 `cargo new my-project`：

```bash
$ cargo new my-project
     Created binary (application) `my-project` package
$ ls my-project
Cargo.toml
src
$ ls my-project/src
main.rs
```

运行 `cargo new my-project` 之后，我们使用 `ls` 来查看 Cargo 创建了什么。在项目目录中，有一个 `Cargo.toml` 文件，它给了我们一个包。还有一个 `src` 目录，其中包含 `main.rs`。在文本编辑器中打开 `Cargo.toml`，注意其中没有提到 `src/main.rs`。Cargo 遵循一个约定，即 `src/main.rs` 是与包同名的可执行板条箱的板条箱根。同样，Cargo 知道如果包目录包含 `src/lib.rs`，则该包包含一个与包同名的库板条箱，并且 `src/lib.rs` 是其板条箱根。Cargo 将板条箱根文件传递给 `rustc` 以构建库或可执行文件。

在这里，我们有一个只包含 `src/main.rs` 的包，这意味着它只包含一个名为 `my-project` 的可执行板条箱。如果一个包同时包含 `src/main.rs` 和 `src/lib.rs`，那么它有两个板条箱：一个可执行板条箱和一个库板条箱，两者都与包同名。通过将文件放在 `src/bin` 目录中，一个包可以有多个可执行板条箱：每个文件将是一个单独的可执行板条箱。

> **模块速查表**
>
> 在我们深入探讨模块和路径的细节之前，这里我们提供一个关于模块、路径、`use` 关键字和 `pub` 关键字在编译器中如何工作，以及大多数开发者如何组织他们代码的快速参考。在本章中，我们将详细介绍这些规则的示例，但这是一个很好的参考，可以提醒你模块是如何工作的。
>
> - **从板条箱根开始**：在编译一个板条箱时，编译器首先在板条箱根文件（通常对于库板条箱是 `src/lib.rs`，对于可执行板条箱是 `src/main.rs`）中查找要编译的代码。
> - **声明模块**：在板条箱根文件中，你可以声明新的模块；假设你使用 `mod garden;` 声明了一个「garden」模块。编译器将在以下位置查找该模块的代码：
> - 内联，在替换 `mod garden` 后面分号的花括号内
> - 在文件 `src/garden.rs` 中
> - 在文件 `src/garden/mod.rs` 中
> - **声明子模块**：在除板条箱根之外的任何文件中，你可以声明子模块。例如，你可能在 `src/garden.rs` 中声明 `mod vegetables;`。编译器将在以下位置的父模块命名的目录中查找子模块的代码：
> - 内联，直接在 `mod vegetables` 之后，在花括号内而不是分号处
> - 在文件 `src/garden/vegetables.rs` 中
> - 在文件 `src/garden/vegetables/mod.rs` 中
> - **模块中代码的路径**：一旦一个模块成为你板条箱的一部分，只要隐私规则允许，你就可以在同一个板条箱的其他任何地方使用代码的路径来引用该模块中的代码。例如，花园蔬菜模块中的 `Asparagus` 类型可以在 `crate::garden::vegetables::Asparagus` 找到。
> - **私有与公共**：默认情况下，模块内的代码对其父模块是私有的。要使一个模块公开，使用 `pub mod` 而不是 `mod` 来声明它。要使公共模块内的项也公开，在它们的声明之前使用 `pub`。
> - **`use` 关键字**：在一个作用域内，`use` 关键字为项创建快捷方式，以减少长路径的重复。在任何可以引用 `crate::garden::vegetables::Asparagus` 的作用域中，你可以使用 `use crate::garden::vegetables::Asparagus;` 创建一个快捷方式，从那时起，在该作用域中你只需要写 `Asparagus` 就可以使用该类型。
>
> 在这里，我们创建了一个名为「backyard」的可执行板条箱，它说明了这些规则。板条箱的目录也名为「backyard」，包含以下文件和目录：
>
> ```bash
> backyard
> ├── Cargo.lock
> ├── Cargo.toml
> └── src
> ├── garden
> │ └── vegetables.rs
> ├── garden.rs
> └── main.rs
> ```
>
> 在这种情况下，板条箱根文件是 `src/main.rs`，它包含：
>
> ```rust
> use crate::garden::vegetables::Asparagus;
>
> pub mod garden;
>
> fn main() {
>     let plant = Asparagus {};
>     println!("I'm growing {:?}!", plant);
> }
> ```
>
> `pub mod garden;` 这一行告诉编译器包含它在 `src/garden.rs` 中找到的代码，该代码是：
>
> ```rust
> pub mod vegetables;
> ```
>
> 在这里，`pub mod vegetables;` 意味着 `src/garden/vegetables.rs` 中的代码也会被包含。该代码是：
>
> ```rust
> #[derive(Debug)]
> pub struct Asparagus {}
> ```
>
> 现在让我们深入了解这些规则的细节并实际演示它们！
