# 使用新类型模式实现外部 trait

在“为类型实现 trait”中，我们提到了孤儿规则，该规则指出，只有当 trait 或类型（或两者）都在我们的 crate 本地时，我们才被允许在类型上实现 trait。使用**新类型模式**可以绕过此限制，该模式涉及在元组结构体中创建一个新类型。（我们在“使用无命名字段的元组结构体创建不同类型”中介绍了元组结构体。）元组结构体将有一个字段，并且是我们想要为其实现 trait 的类型的轻量级包装。然后，包装类型在我们的 crate 本地，我们可以在包装上实现 trait。“新类型”一词源自 Haskell 编程语言。使用此模式没有运行时性能损失，并且包装类型在编译时会被省略。

例如，假设我们想要在 `Vec<T>` 上实现 `Display`，但孤儿规则阻止我们直接这样做，因为 `Display` trait 和 `Vec<T>` 类型是在我们的 crate 外部定义的。我们可以创建一个包含 `Vec<T>` 实例的 `Wrapper` 结构体；然后我们可以在 `Wrapper` 上实现 `Display` 并使用 `Vec<T>` 值，如清单 19-23 所示。

文件名：`src/main.rs`

```rust
use std::fmt;

struct Wrapper(Vec<String>);

impl fmt::Display for Wrapper {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "[{}]", self.0.join(", "))
    }
}

fn main() {
    let w = Wrapper(vec![
        String::from("hello"),
        String::from("world"),
    ]);
    println!("w = {w}");
}
```

清单 19-23：围绕 `Vec<String>` 创建一个 `Wrapper` 类型以实现 `Display`

`Display` 的实现使用 `self.0` 来访问内部的 `Vec<T>`，因为 `Wrapper` 是一个元组结构体，而 `Vec<T>` 是元组中索引为 0 的项。然后我们可以在 `Wrapper` 上使用 `Display` 类型的功能。

使用此技术的缺点是，`Wrapper` 是一个新类型，因此它没有它所包含的值的方法。我们必须直接在 `Wrapper` 上实现 `Vec<T>` 的所有方法，以便这些方法委托给 `self.0`，这样我们就可以将 `Wrapper` 完全当作 `Vec<T>` 来处理。如果我们希望新类型具有内部类型的每个方法，在 `Wrapper` 上实现 `Deref` trait 以返回内部类型将是一个解决方案（我们在“使用 Deref 将智能指针当作常规引用处理”中讨论了实现 `Deref` trait）。如果我们不希望 `Wrapper` 类型具有内部类型的所有方法——例如，限制 `Wrapper` 类型的行为——我们将不得不手动实现我们确实需要的方法。

即使不涉及 trait，这种新类型模式也很有用。让我们换个关注点，看看与 Rust 类型系统进行交互的一些高级方法。
