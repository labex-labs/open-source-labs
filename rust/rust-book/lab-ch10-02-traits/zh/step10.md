# 使用特性约束有条件地实现方法

通过在使用泛型类型参数的 `impl` 块中使用特性约束，我们可以为实现了指定特性的类型有条件地实现方法。例如，清单 10-15 中的 `Pair<T>` 类型总是实现 `new` 函数来返回 `Pair<T>` 的新实例（从“定义方法”中回忆起，`Self` 是 `impl` 块类型的类型别名，在这种情况下是 `Pair<T>`）。但是在下一个 `impl` 块中，只有当 `Pair<T>` 的内部类型 `T` 实现了用于比较的 `PartialOrd` 特性和用于打印的 `Display` 特性时，`Pair<T>` 才实现 `cmp_display` 方法。

文件名：`src/lib.rs`

```rust
use std::fmt::Display;

struct Pair<T> {
    x: T,
    y: T,
}

impl<T> Pair<T> {
    fn new(x: T, y: T) -> Self {
        Self { x, y }
    }
}

impl<T: Display + PartialOrd> Pair<T> {
    fn cmp_display(&self) {
        if self.x >= self.y {
            println!("The largest member is x = {}", self.x);
        } else {
            println!("The largest member is y = {}", self.y);
        }
    }
}
```

清单 10-15：根据特性约束有条件地在泛型类型上实现方法

我们还可以为实现了另一个特性的任何类型有条件地实现一个特性。在满足特性约束的任何类型上对特性的实现被称为**覆盖实现**，并且在 Rust 标准库中被广泛使用。例如，标准库为任何实现了 `Display` 特性的类型实现了 `ToString` 特性。标准库中的 `impl` 块看起来类似于以下代码：

```rust
impl<T: Display> ToString for T {
    --snip--
}
```

因为标准库有这个覆盖实现，所以我们可以在任何实现了 `Display` 特性的类型上调用由 `ToString` 特性定义的 `to_string` 方法。例如，因为整数实现了 `Display`，所以我们可以像这样将整数转换为它们相应的 `String` 值：

```rust
let s = 3.to_string();
```

覆盖实现在特性文档的“实现者”部分中显示。

特性和特性约束使我们能够编写使用泛型类型参数的代码，以减少重复，同时向编译器指定我们希望泛型类型具有特定的行为。然后编译器可以使用特性约束信息来检查与我们的代码一起使用的所有具体类型是否提供了正确的行为。在动态类型语言中，如果我们在未定义该方法的类型上调用方法，我们会在运行时得到一个错误。但是 Rust 将这些错误转移到编译时，所以我们被迫在代码甚至能够运行之前修复问题。此外，我们不必编写在运行时检查行为的代码，因为我们已经在编译时进行了检查。这样做在不放弃泛型灵活性的情况下提高了性能。
