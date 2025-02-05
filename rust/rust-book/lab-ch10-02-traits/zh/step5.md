# 作为参数的特性

既然你已经知道如何定义和实现特性，我们可以探讨如何使用特性来定义接受多种不同类型的函数。我们将使用在清单 10-13 中为 `NewsArticle` 和 `Tweet` 类型实现的 `Summary` 特性，来定义一个 `notify` 函数，该函数会在其 `item` 参数（它是实现了 `Summary` 特性的某种类型）上调用 `summarize` 方法。为此，我们使用 `impl Trait` 语法，如下所示：

```rust
pub fn notify(item: &impl Summary) {
    println!("Breaking news! {}", item.summarize());
}
```

我们不是为 `item` 参数指定具体的类型，而是指定 `impl` 关键字和特性名称。这个参数接受任何实现了指定特性的类型。在 `notify` 的函数体中，我们可以对 `item` 调用来自 `Summary` 特性的任何方法，比如 `summarize`。我们可以调用 `notify` 并传入任何 `NewsArticle` 或 `Tweet` 的实例。用任何其他类型（比如 `String` 或 `i32`）调用该函数的代码将无法编译，因为那些类型没有实现 `Summary`。
