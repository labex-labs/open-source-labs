# 数据类型

Rust 中的每个值都具有某种**数据类型**，它告诉 Rust 正在指定何种类型的数据，以便 Rust 知道如何处理该数据。我们将研究两种数据类型子集：标量类型和复合类型。

请记住，Rust 是一种**静态类型**语言，这意味着它必须在编译时就知道所有变量的类型。编译器通常可以根据值以及我们使用值的方式推断出我们想要使用的类型。在有多种可能类型的情况下，例如在“将猜测值与秘密数字进行比较”中使用 `parse` 将 `String` 转换为数字类型时，我们必须添加类型标注，如下所示：

```rust
let guess: u32 = "42".parse().expect("Not a number!");
```

如果我们不添加上述代码中显示的 `: u32` 类型标注，Rust 将显示以下错误，这意味着编译器需要我们提供更多信息才能知道我们想要使用的类型：

```bash
$ cargo build
   Compiling no_type_annotations v0.1.0 (file:///projects/no_type_annotations)
error[E0282]: type annotations needed
 --> src/main.rs:2:9
  |
2 |     let guess = "42".parse().expect("Not a number!");
  |         ^^^^^ consider giving `guess` a type
```

对于其他数据类型，你会看到不同的类型标注。
