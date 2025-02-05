# 用于从属性生成代码的过程宏

宏的第二种形式是过程宏，它的行为更像一个函数（并且是一种过程）。**过程宏**接受一些代码作为输入，对该代码进行操作，并生成一些代码作为输出，而不像声明式宏那样与模式进行匹配并用其他代码替换该代码。三种过程宏分别是自定义 `derive`、类属性和类函数，它们的工作方式类似。

在创建过程宏时，定义必须位于具有特殊 crate 类型的自己的 crate 中。这是出于一些复杂的技术原因，我们希望在未来消除这些原因。在清单 19 - 29 中，我们展示了如何定义一个过程宏，其中 `some_attribute` 是使用特定宏类型的占位符。

文件名：`src/lib.rs`

```rust
use proc_macro::TokenStream;

#[some_attribute]
pub fn some_name(input: TokenStream) -> TokenStream {
}
```

清单 19 - 29：定义过程宏的示例

定义过程宏的函数以 `TokenStream` 作为输入并生成 `TokenStream` 作为输出。`TokenStream` 类型由 Rust 附带的 `proc_macro` crate 定义，表示一系列标记。这是宏的核心：宏所操作的源代码构成输入 `TokenStream`，宏生成的代码是输出 `TokenStream`。该函数还附加了一个属性，用于指定我们正在创建的过程宏的类型。我们可以在同一个 crate 中有多种过程宏。

让我们看看不同类型的过程宏。我们将从自定义 `derive` 宏开始，然后解释使其他形式不同的小差异。
