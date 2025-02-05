# 如何编写自定义 derive 宏

让我们创建一个名为 `hello_macro` 的 crate，它定义了一个名为 `HelloMacro` 的 trait，以及一个名为 `hello_macro` 的关联函数。我们不会让用户为他们的每个类型实现 `HelloMacro` trait，而是提供一个过程宏，这样用户就可以用 `#[derive(HelloMacro)]` 来注释他们的类型，从而获得 `hello_macro` 函数的默认实现。默认实现将打印 `Hello, Macro! My name is TypeName!`，其中 `TypeName` 是定义该 trait 的类型的名称。换句话说，我们将编写一个 crate，使其他程序员能够使用我们的 crate 编写类似于清单 19 - 30 的代码。

文件名：`src/main.rs`

```rust
use hello_macro::HelloMacro;
use hello_macro_derive::HelloMacro;

#[derive(HelloMacro)]
struct Pancakes;

fn main() {
    Pancakes::hello_macro();
}
```

清单 19 - 30：使用我们的过程宏时，我们的 crate 用户能够编写的代码

当我们完成后，这段代码将打印 `Hello, Macro! My name is Pancakes!`。第一步是创建一个新的库 crate，如下所示：

```bash
cargo new hello_macro --lib
```

接下来，我们将定义 `HelloMacro` trait 及其关联函数：

文件名：`src/lib.rs`

```rust
pub trait HelloMacro {
    fn hello_macro();
}
```

我们有了一个 trait 及其函数。此时，我们的 crate 用户可以通过实现该 trait 来实现所需的功能，如下所示：

```rust
use hello_macro::HelloMacro;

struct Pancakes;

impl HelloMacro for Pancakes {
    fn hello_macro() {
        println!("Hello, Macro! My name is Pancakes!");
    }
}

fn main() {
    Pancakes::hello_macro();
}
```

然而，他们需要为每个想要与 `hello_macro` 一起使用的类型编写实现块；我们希望避免他们做这项工作。

此外，我们还不能为 `hello_macro` 函数提供默认实现，该实现将打印 trait 所实现的类型的名称：Rust 没有反射功能，因此它无法在运行时查找类型的名称。我们需要一个宏在编译时生成代码。

下一步是定义过程宏。在撰写本文时，过程宏需要在它们自己的 crate 中。最终，这个限制可能会被解除。构建 crate 和宏 crate 的约定如下：对于一个名为 `foo` 的 crate，一个自定义 `derive` 过程宏 crate 被称为 `foo_derive`。让我们在 `hello_macro` 项目中创建一个名为 `hello_macro_derive` 的新 crate：

```bash
cargo new hello_macro_derive --lib
```

我们的两个 crate 紧密相关，所以我们在 `hello_macro` crate 的目录中创建过程宏 crate。如果我们在 `hello_macro` 中更改 trait 定义，我们也必须在 `hello_macro_derive` 中更改过程宏的实现。这两个 crate 需要分别发布，使用这些 crate 的程序员需要将它们都作为依赖项添加并引入作用域。或者，我们可以让 `hello_macro` crate 使用 `hello_macro_derive` 作为依赖项，并重新导出过程宏代码。然而，我们构建项目的方式使得即使程序员不想要 `derive` 功能，也可以使用 `hello_macro`。

我们需要将 `hello_macro_derive` crate 声明为一个过程宏 crate。我们还需要 `syn` 和 `quote` crate 的功能，稍后你会看到，所以我们需要将它们作为依赖项添加。将以下内容添加到 `hello_macro_derive` 的 `Cargo.toml` 文件中：

文件名：`hello_macro_derive/Cargo.toml`

```toml
[lib]
proc-macro = true

[dependencies]
syn = "1.0"
quote = "1.0"
```

要开始定义过程宏，将清单 19 - 31 中的代码放入 `hello_macro_derive` crate 的 `src/lib.rs` 文件中。请注意，在我们为 `impl_hello_macro` 函数添加定义之前，这段代码不会编译。

文件名：`hello_macro_derive/src/lib.rs`

```rust
use proc_macro::TokenStream;
use quote::quote;
use syn;

#[proc_macro_derive(HelloMacro)]
pub fn hello_macro_derive(input: TokenStream) -> TokenStream {
    // 将 Rust 代码表示为一个语法树，以便我们可以操作
    let ast = syn::parse(input).unwrap();

    // 构建 trait 实现
    impl_hello_macro(&ast)
}
```

清单 19 - 31：大多数过程宏 crate 处理 Rust 代码所需的代码

请注意，我们将代码分成了 `hello_macro_derive` 函数和 `impl_hello_macro` 函数，前者负责解析 `TokenStream`，后者负责转换语法树：这使得编写过程宏更加方便。外部函数（在这种情况下是 `hello_macro_derive`）中的代码对于你看到或创建的几乎每个过程宏 crate 来说都是相同的。你在内部函数（在这种情况下是 `impl_hello_macro`）主体中指定的代码将根据你的过程宏的目的而有所不同。

我们引入了三个新的 crate：`proc_macro`、`syn`（可从 *https://crates.io/crates/syn* 获得）和 `quote`（可从 *https://crates.io/crates/quote* 获得）。`proc_macro` crate 随 Rust 一起提供，所以我们不需要将其添加到 `Cargo.toml` 的依赖项中。`proc_macro` crate 是编译器的 API，它允许我们从代码中读取和操作 Rust 代码。

`syn` crate 将 Rust 代码从字符串解析为一个我们可以对其执行操作的数据结构。`quote` crate 将 `syn` 数据结构转换回 Rust 代码。这些 crate 使解析我们可能想要处理的任何类型的 Rust 代码变得更加简单：编写一个完整的 Rust 代码解析器并非易事。

当我们库的用户在一个类型上指定 `#[derive(HelloMacro)]` 时，`hello_macro_derive` 函数将会被调用。这是可行的，因为我们在这里用 `proc_macro_derive` 注释了 `hello_macro_derive` 函数，并指定了名称 `HelloMacro`，它与我们的 trait 名称相匹配；这是大多数过程宏遵循的约定。

`hello_macro_derive` 函数首先将 `input` 从 `TokenStream` 转换为一个数据结构，然后我们可以对其进行解释和操作。这就是 `syn` 发挥作用的地方。`syn` 中的 `parse` 函数接受一个 `TokenStream`，并返回一个表示解析后的 Rust 代码的 `DeriveInput` 结构体。清单 19 - 32 展示了从解析 `struct Pancakes;` 字符串得到的 `DeriveInput` 结构体的相关部分。

    DeriveInput {
        --snip--

        ident: Ident {
            ident: "Pancakes",
            span: #0 bytes(95..103)
        },
        data: Struct(
            DataStruct {
                struct_token: Struct,
                fields: Unit,
                semi_token: Some(
                    Semi
                )
            }
        )
    }

清单 19 - 32：解析清单 19 - 30 中带有宏属性的代码时得到的 `DeriveInput` 实例

这个结构体的字段表明我们解析的 Rust 代码是一个单元结构体，其 `ident`（_标识符_，即名称）为 `Pancakes`。这个结构体还有更多字段用于描述各种 Rust 代码；有关 `DeriveInput` 的更多信息，请查看 *https://docs.rs/syn/1.0/syn/struct.DeriveInput.html* 上的 `syn` 文档。

很快我们将定义 `impl_hello_macro` 函数，在那里我们将构建我们想要包含的新 Rust 代码。但在我们这样做之前，请注意我们的 `derive` 宏的输出也是一个 `TokenStream`。返回的 `TokenStream` 会被添加到我们 crate 用户编写的代码中，所以当他们编译他们的 crate 时，他们将获得我们在修改后的 `TokenStream` 中提供的额外功能。

你可能已经注意到我们在这里调用 `unwrap`，以便如果对 `syn::parse` 函数的调用失败，`hello_macro_derive` 函数会 panic。我们的过程宏在出错时必须 panic，因为 `proc_macro_derive` 函数必须返回 `TokenStream` 而不是 `Result`，以符合过程宏 API。我们在这个例子中使用 `unwrap` 进行了简化；在生产代码中，你应该使用 `panic!` 或 `expect` 提供更具体的关于出错原因的错误消息。

现在我们有了将带注释的 Rust 代码从 `TokenStream` 转换为 `DeriveInput` 实例的代码，让我们生成在带注释的类型上实现 `HelloMacro` trait 的代码，如清单 19 - 33 所示。

文件名：`hello_macro_derive/src/lib.rs`

```rust
fn impl_hello_macro(ast: &syn::DeriveInput) -> TokenStream {
    let name = &ast.ident;
    let gen = quote! {
        impl HelloMacro for #name {
            fn hello_macro() {
                println!(
                    "Hello, Macro! My name is {}!",
                    stringify!(#name)
                );
            }
        }
    };
    gen.into()
}
```

清单 19 - 33：使用解析后的 Rust 代码实现 `HelloMacro` trait

我们使用 `ast.ident` 获取一个包含带注释类型的名称（标识符）的 `Ident` 结构体实例。清单 19 - 32 中的结构体表明，当我们对清单 19 - 30 中的代码运行 `impl_hello_macro` 函数时，我们得到的 `ident` 将具有一个 `ident` 字段，其值为 `"Pancakes"`。因此，清单 19 - 33 中的 `name` 变量将包含一个 `Ident` 结构体实例，打印时将是字符串 `"Pancakes"`，即清单 19 - 30 中结构体的名称。

`quote!` 宏让我们定义想要返回的 Rust 代码。编译器期望的与 `quote!` 宏执行的直接结果不同，所以我们需要将其转换为 `TokenStream`。我们通过调用 `into` 方法来做到这一点，该方法消耗这个中间表示并返回所需的 `TokenStream` 类型的值。

`quote!` 宏还提供了一些非常酷的模板机制：我们可以输入 `#name`，`quote!` 会将其替换为变量 `name` 中的值。你甚至可以进行一些类似于普通宏工作方式的重复操作。有关详细介绍，请查看 *https://docs.rs/quote* 上的 `quote` crate 文档。

我们希望我们的过程宏为用户注释的类型生成 `HelloMacro` trait 的实现，我们可以通过使用 `#name` 来实现。trait 实现有一个函数 `hello_macro`，其主体包含我们想要提供的功能：打印 `Hello, Macro! My name is`，然后是带注释类型的名称。

这里使用的 `stringify!` 宏是 Rust 内置的。它接受一个 Rust 表达式，例如 `1 + 2`，并在编译时将该表达式转换为一个字符串字面量，例如 `"1 + 2"`。这与 `format!` 或 `println!` 宏不同，后者会计算表达式，然后将结果转换为一个 `String`。`#name` 输入有可能是一个要按字面量打印的表达式，所以我们使用 `stringify!`。使用 `stringify!` 还通过在编译时将 `#name` 转换为字符串字面量节省了一次分配。

此时，`hello_macro` 和 `hello_macro_derive` 中的 `cargo build` 应该都能成功完成。让我们将这些 crate 与清单 19 - 30 中的代码连接起来，看看过程宏的实际运行情况！使用 `cargo new pancakes` 在你的 `project` 目录中创建一个新的二进制项目。我们需要在 `pancakes` crate 的 `Cargo.toml` 中将 `hello_macro` 和 `hello_macro_derive` 添加为依赖项。如果你要将你的 `hello_macro` 和 `hello_macro_derive` 版本发布到 *https://crates.io*，它们将是常规依赖项；如果不是，你可以如下指定它们为 `path` 依赖项：

    [dependencies]
    hello_macro = { path = "../hello_macro" }
    hello_macro_derive = { path = "../hello_macro/hello_macro_derive" }

将清单 19 - 30 中的代码放入 `src/main.rs`，然后运行 `cargo run`：它应该打印 `Hello, Macro! My name is Pancakes!` 过程宏对 `HelloMacro` trait 的实现被包含进来，而 `pancakes` crate 无需实现它；`#[derive(HelloMacro)]` 添加了 trait 实现。

接下来，让我们探讨其他类型的过程宏与自定义 `derive` 宏有何不同。
