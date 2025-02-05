# 使用派生 trait 添加有用的功能

在调试程序时，能够打印 `Rectangle` 实例并查看其所有字段的值会很有用。清单 5-11 尝试使用我们在前面章节中使用过的 `println!` 宏。然而，这行不通。

文件名：`src/main.rs`

```rust
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!("rect1 is {}", rect1);
}
```

清单 5-11：尝试打印 `Rectangle` 实例

当我们编译这段代码时，会得到一个核心错误信息：

```bash
error[E0277]: `Rectangle` doesn't implement `std::fmt::Display`
```

`println!` 宏可以进行多种格式化，默认情况下，花括号告诉 `println!` 使用一种称为 `Display` 的格式化：用于直接供最终用户消费的输出。到目前为止我们看到的原生类型默认实现了 `Display`，因为向用户展示 `1` 或任何其他原生类型只有一种方式。但是对于结构体，`println!` 应该如何格式化输出不太明确，因为有更多的显示可能性：是否要逗号？是否要打印花括号？是否要显示所有字段？由于这种模糊性，Rust 不会试图猜测我们想要什么，并且结构体没有为与 `println!` 和 `{}` 占位符一起使用而提供的 `Display` 实现。

如果我们继续阅读错误信息，会找到这条有用的提示：

    = help: the trait `std::fmt::Display` is not implemented for `Rectangle`
    = note: in format strings you may be able to use `{:?}` (or {:#?} for
    pretty-print) instead

让我们试试！现在 `println!` 宏调用将看起来像 `println!("rect1 is {:?}", rect1);`。在花括号内放入 specifier `:?` 告诉 `println!` 我们想要使用一种称为 `Debug` 的输出格式。`Debug` trait 使我们能够以对开发者有用的方式打印我们的结构体，这样我们在调试代码时就能看到它的值。

用这个更改编译代码。哎呀！我们仍然得到一个错误：

```bash
error[E0277]: `Rectangle` doesn't implement `Debug`
```

但同样，编译器给了我们一条有用的提示：

```rust
= help: the trait `Debug` is not implemented for `Rectangle`
= note: add `#[derive(Debug)]` or manually implement `Debug`
```

Rust 确实包含打印调试信息的功能，但我们必须显式选择加入才能使该功能对我们的结构体可用。要做到这一点，我们在结构体定义之前添加外部属性 `#[derive(Debug)]`，如清单 5-12 所示。

文件名：`src/main.rs`

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!("rect1 is {:?}", rect1);
}
```

清单 5-12：添加属性以派生 `Debug` trait 并使用调试格式打印 `Rectangle` 实例

现在当我们运行程序时，不会得到任何错误，并且我们会看到以下输出：

```rust
rect1 is Rectangle { width: 30, height: 50 }
```

很好！这不是最漂亮的输出，但它显示了这个实例所有字段的值，这在调试期间肯定会有帮助。当我们有更大的结构体时，有更易于阅读的输出会很有用；在那些情况下，我们可以在 `println!` 字符串中使用 `{:#?}` 而不是 `{:?}`。在这个例子中，使用 `{:#?}` 样式将输出如下：

    rect1 is Rectangle {
        width: 30,
        height: 50,
    }

另一种使用 `Debug` 格式打印值的方法是使用 `dbg!` 宏，它获取一个表达式的所有权（与 `println!` 不同，`println!` 获取一个引用），打印 `dbg!` 宏调用在你的代码中出现的文件和行号以及该表达式的结果值，并返回该值的所有权。

> 注意：调用 `dbg!` 宏会打印到标准错误控制台流（`stderr`），而 `println!` 会打印到标准输出控制台流（`stdout`）。我们将在“将错误消息写入标准错误而不是标准输出”中更多地讨论 `stderr` 和 `stdout`。

这里有一个例子，我们对赋给 `width` 字段的值以及 `rect1` 中整个结构体的值感兴趣：

文件名：`src/main.rs`

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let scale = 2;
    let rect1 = Rectangle {
      1 width: dbg!(30 * scale),
        height: 50,
    };

  2 dbg!(&rect1);
}
```

我们可以在表达式 `30 * scale` 周围加上 `dbg!`\[1\]，并且因为 `dbg!` 返回表达式值的所有权，`width` 字段将获得与我们不在那里使用 `dbg!` 调用时相同的值。我们不希望 `dbg!` 获取 `rect1` 的所有权，所以在下一次调用中我们对 `rect1` 使用引用\[2\]。这个例子的输出如下：

    [src/main.rs:10] 30 * scale = 60
    [src/main.rs:14] &rect1 = Rectangle {
        width: 60,
        height: 50,
    }

我们可以看到第一部分输出来自\[1\]，在那里我们正在调试表达式 `30 * scale`，其结果值是 `60`（为整数实现的 `Debug` 格式化只是打印它们的值）。在\[2\]处的 `dbg!` 调用输出 `&rect1` 的值，即 `Rectangle` 结构体。这个输出使用了 `Rectangle` 类型漂亮的 `Debug` 格式化。当你试图弄清楚你的代码在做什么时，`dbg!` 宏真的很有帮助！

除了 `Debug` trait 之外，Rust 还为我们提供了许多 trait 与 `derive` 属性一起使用，可以为我们的自定义类型添加有用的行为。这些 trait 及其行为列在附录 C 中。我们将在第 10 章中介绍如何用自定义行为实现这些 trait 以及如何创建自己的 trait。除了 `derive` 之外还有许多属性；有关更多信息，请参阅 Rust 参考的“属性”部分 *https://doc.rust-lang.org/reference/attributes.html*。

我们的 `area` 函数非常特定：它只计算矩形的面积。将此行为与我们的 `Rectangle` 结构体更紧密地联系起来会很有帮助，因为它不适用于任何其他类型。让我们看看如何通过将 `area` 函数转换为在我们的 `Rectangle` 类型上定义的 `area` _方法_ 来继续重构这段代码。
