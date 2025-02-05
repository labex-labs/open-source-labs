# 使用超 trait

有时你可能会编写一个依赖于另一个 trait 的 trait 定义：为了让一个类型实现第一个 trait，你希望要求该类型也实现第二个 trait。这样做是为了让你的 trait 定义能够利用第二个 trait 的关联项。你的 trait 定义所依赖的 trait 被称为你的 trait 的**超 trait**。

例如，假设我们想要创建一个 `OutlinePrint` trait，它有一个 `outline_print` 方法，该方法将打印一个给定的值，并将其格式设置为用星号框起来。也就是说，给定一个实现了标准库 trait `Display` 并输出 `(x, y)` 的 `Point` 结构体，当我们在一个 `x` 为 `1` 且 `y` 为 `3` 的 `Point` 实例上调用 `outline_print` 时，它应该打印以下内容：

    **********
    *        *
    * (1, 3) *
    *        *
    **********

在 `outline_print` 方法的实现中，我们想要使用 `Display` trait 的功能。因此，我们需要指定 `OutlinePrint` trait 仅适用于也实现了 `Display` 并提供 `OutlinePrint` 所需功能的类型。我们可以在 trait 定义中通过指定 `OutlinePrint: Display` 来做到这一点。这种技术类似于为 trait 添加一个 trait 约束。清单 19-22 展示了 `OutlinePrint` trait 的实现。

文件名：`src/main.rs`

```rust
use std::fmt;

trait OutlinePrint: fmt::Display {
    fn outline_print(&self) {
        let output = self.to_string();
        let len = output.len();
        println!("{}", "*".repeat(len + 4));
        println!("*{}*", " ".repeat(len + 2));
        println!("* {} *", output);
        println!("*{}*", " ".repeat(len + 2));
        println!("{}", "*".repeat(len + 4));
    }
}
```

清单 19-22：实现需要 `Display` 功能的 `OutlinePrint` trait

因为我们指定了 `OutlinePrint` 需要 `Display` trait，所以我们可以使用为任何实现了 `Display` 的类型自动实现的 `to_string` 函数。如果我们在 trait 名称后没有添加冒号并指定 `Display` trait 就尝试使用 `to_string`，我们会得到一个错误，提示在当前作用域中为类型 `&Self` 未找到名为 `to_string` 的方法。

让我们看看当我们尝试在一个未实现 `Display` 的类型（如 `Point` 结构体）上实现 `OutlinePrint` 时会发生什么：

文件名：`src/main.rs`

```rust
struct Point {
    x: i32,
    y: i32,
}

impl OutlinePrint for Point {}
```

我们会得到一个错误，提示需要 `Display` 但未实现：

```bash
error[E0277]: `Point` doesn't implement `std::fmt::Display`
  --> src/main.rs:20:6
   |
20 | impl OutlinePrint for Point {}
   |      ^^^^^^^^^^^^ `Point` cannot be formatted with the default formatter
   |
   = help: the trait `std::fmt::Display` is not implemented for `Point`
   = note: in format strings you may be able to use `{:?}` (or {:#?} for
pretty-print) instead
note: required by a bound in `OutlinePrint`
  --> src/main.rs:3:21
   |
3  | trait OutlinePrint: fmt::Display {
   |                     ^^^^^^^^^^^^ required by this bound in `OutlinePrint`
```

为了解决这个问题，我们在 `Point` 上实现 `Display`，以满足 `OutlinePrint` 所需的约束，如下所示：

文件名：`src/main.rs`

```rust
use std::fmt;

impl fmt::Display for Point {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "({}, {})", self.x, self.y)
    }
}
```

然后，在 `Point` 上实现 `OutlinePrint` trait 将成功编译，并且我们可以在 `Point` 实例上调用 `outline_print`，以在星号轮廓中显示它。
