# 将模块分离到不同文件中

到目前为止，本章中的所有示例都在一个文件中定义了多个模块。当模块变得很大时，你可能希望将它们的定义移动到一个单独的文件中，以使代码更易于浏览。

例如，让我们从清单 7-17 中的代码开始，该代码有多个餐厅模块。我们将把模块提取到文件中，而不是在包根文件中定义所有模块。在这种情况下，包根文件是 `src/lib.rs`，但这个过程也适用于二进制包，其包根文件是 `src/main.rs`。

首先，我们将把 `front_of_house` 模块提取到它自己的文件中。删除 `front_of_house` 模块花括号内的代码，只保留 `mod front_of_house;` 声明，这样 `src/lib.rs` 就包含了清单 7-21 中所示的代码。请注意，在我们创建清单 7-22 中的 `src/front_of_house.rs` 文件之前，这不会编译。

文件名：`src/lib.rs`

```rust
mod front_of_house;

pub use crate::front_of_house::hosting;

pub fn eat_at_restaurant() {
    hosting::add_to_waitlist();
}
```

清单 7-21：声明 `front_of_house` 模块，其主体将在 `src/front_of_house.rs` 中

接下来，将花括号内的代码放入一个名为 `src/front_of_house.rs` 的新文件中，如清单 7-22 所示。编译器知道要在这个文件中查找，因为它在包根中遇到了名为 `front_of_house` 的模块声明。

文件名：`src/front_of_house.rs`

```rust
pub mod hosting {
    pub fn add_to_waitlist() {}
}
```

清单 7-22：`src/front_of_house.rs` 中 `front_of_house` 模块内的定义

请注意，在你的模块树中，你只需要使用 `mod` 声明加载一次文件。一旦编译器知道该文件是项目的一部分（并且由于你放置 `mod` 语句的位置而知道代码在模块树中的位置），项目中的其他文件应该使用到它声明位置的路径来引用已加载文件的代码，就像在“引用模块树中项的路径”中所介绍的那样。换句话说，`mod` 不是你可能在其他编程语言中看到的“包含”操作。

接下来，我们将把 `hosting` 模块提取到它自己的文件中。这个过程有点不同，因为 `hosting` 是 `front_of_house` 的子模块，而不是根模块的子模块。我们将把 `hosting` 的文件放在一个新目录中，该目录将以其在模块树中的祖先命名，在这种情况下是 `src/front_of_house`。

为了开始移动 `hosting`，我们将 `src/front_of_house.rs` 修改为只包含 `hosting` 模块的声明：

文件名：`src/front_of_house.rs`

```rust
pub mod hosting;
```

然后我们创建一个 `src/front_of_house` 目录和一个 `hosting.rs` 文件，以包含在 `hosting` 模块中所做的定义：

文件名：`src/front_of_house/hosting.rs`

```rust
pub fn add_to_waitlist() {}
```

如果我们将 `hosting.rs` 放在 `src` 目录中，编译器会期望 `hosting.rs` 代码在包根中声明的 `hosting` 模块中，而不是声明为 `front_of_house` 模块的子模块。编译器关于检查哪些文件以获取哪些模块代码的规则意味着目录和文件更紧密地匹配模块树。

> **备用文件路径**
>
> 到目前为止，我们已经介绍了 Rust 编译器使用的最符合习惯的文件路径，但 Rust 也支持一种较旧的文件路径样式。对于在包根中声明的名为 `front_of_house` 的模块，编译器将在以下位置查找该模块的代码：
>
> - `src/front_of_house.rs`（我们介绍的内容）
> - `src/front_of_house/mod.rs`（较旧的样式，仍然支持的路径）
>
> 对于作为 `front_of_house` 子模块的名为 `hosting` 的模块，编译器将在以下位置查找该模块的代码：
>
> - `src/front_of_house/hosting.rs`（我们介绍的内容）
> - `src/front_of_house/hosting/mod.rs`（较旧的样式，仍然支持的路径）
>
> 如果你对同一个模块同时使用这两种样式，将会得到一个编译器错误。在同一个项目中对不同模块混合使用这两种样式是允许的，但可能会让浏览你项目的人感到困惑。
>
> 使用名为 `mod.rs` 的文件样式的主要缺点是，你的项目最终可能会有许多名为 `mod.rs` 的文件，当你在编辑器中同时打开它们时，可能会感到困惑。

我们已经将每个模块的代码移动到了一个单独的文件中，并且模块树保持不变。`eat_at_restaurant` 中的函数调用将无需任何修改即可工作，即使定义位于不同的文件中。这种技术允许你在模块变大时将它们移动到新文件中。

请注意，`src/lib.rs` 中的 `pub use crate::front_of_house::hosting` 语句也没有改变，`use` 对作为包一部分编译的文件也没有任何影响。`mod` 关键字声明模块，Rust 会在与模块同名的文件中查找进入该模块的代码。
