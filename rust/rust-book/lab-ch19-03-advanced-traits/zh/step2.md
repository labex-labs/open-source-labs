# 关联类型

**关联类型** 将类型占位符与一个 trait 相连接，这样 trait 方法定义就可以在其签名中使用这些占位符类型。trait 的实现者将指定要使用的具体类型，以替代特定实现中的占位符类型。这样，我们就可以定义一个使用某些类型的 trait，而无需在 trait 实现之前确切知道这些类型是什么。

我们将本章中的大多数高级特性描述为很少需要。关联类型则处于中间位置：它们的使用频率低于本书其他部分所解释的特性，但比本章讨论的许多其他特性更常见。

标准库提供的 `Iterator` trait 就是一个带有关联类型的 trait 的例子。关联类型名为 `Item`，代表实现 `Iterator` trait 的类型正在迭代的值的类型。`Iterator` trait 的定义如清单 19-12 所示。

```rust
pub trait Iterator {
    type Item;

    fn next(&mut self) -> Option<Self::Item>;
}
```

清单 19-12：带有关联类型 `Item` 的 `Iterator` trait 的定义

类型 `Item` 是一个占位符，`next` 方法的定义表明它将返回 `Option<Self::Item>` 类型的值。`Iterator` trait 的实现者将为 `Item` 指定具体类型，并且 `next` 方法将返回一个包含该具体类型值的 `Option`。

关联类型可能看起来与泛型是类似的概念，因为后者允许我们定义一个函数而无需指定它可以处理哪些类型。为了研究这两个概念之间的差异，我们将查看在名为 `Counter` 的类型上对 `Iterator` trait 的实现，该实现指定 `Item` 类型为 `u32`：

文件名：`src/lib.rs`

```rust
impl Iterator for Counter {
    type Item = u32;

    fn next(&mut self) -> Option<Self::Item> {
        --snip--
```

这种语法似乎与泛型的语法类似。那么为什么不使用泛型来定义 `Iterator` trait 呢，如清单 19-13 所示？

```rust
pub trait Iterator<T> {
    fn next(&mut self) -> Option<T>;
}
```

清单 19-13：使用泛型对 `Iterator` trait 的假设定义

区别在于，当使用泛型时，如清单 19-13 所示，我们必须在每个实现中注释类型；因为我们也可以为 `Counter` 实现 `Iterator<String>` 或任何其他类型，所以对于 `Counter` 我们可以有多个 `Iterator` 的实现。换句话说，当一个 trait 有一个泛型参数时，它可以为一个类型多次实现，每次改变泛型类型参数的具体类型。当我们在 `Counter` 上使用 `next` 方法时，我们必须提供类型注释以指示我们想要使用 `Iterator` 的哪个实现。

使用关联类型时，我们不需要注释类型，因为我们不能为一个类型多次实现一个 trait。在清单 19-12 中使用关联类型的定义中，我们只能选择一次 `Item` 的类型是什么，因为对于 `Counter` 只能有一个 `impl Iterator for Counter`。我们不必在每次对 `Counter` 调用 `next` 的地方都指定我们想要一个 `u32` 值的迭代器。

关联类型也成为 trait 契约的一部分：trait 的实现者必须提供一个类型来替代关联类型占位符。关联类型通常有一个描述该类型将如何使用的名称，并且在 API 文档中记录关联类型是一种很好的做法。
