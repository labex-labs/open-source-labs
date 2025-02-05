# 定义方法

让我们把那个以 `Rectangle` 实例作为参数的 `area` 函数进行修改，改为在 `Rectangle` 结构体上定义一个 `area` 方法，如清单 5-13 所示。

文件名：`src/main.rs`

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!(
        "The area of the rectangle is {} square pixels.",
        rect1.area()
    );
}
```

清单 5-13：在 `Rectangle` 结构体上定义 `area` 方法

为了在 `Rectangle` 的上下文中定义函数，我们为 `Rectangle` 开始一个 `impl`（实现）块\[1\]。这个 `impl` 块中的所有内容都将与 `Rectangle` 类型相关联。然后我们把 `area` 函数移到 `impl` 花括号内\[2\]，并在签名以及函数体中的各处将第一个（在这种情况下也是唯一的）参数改为 `self`。在 `main` 函数中，我们之前调用 `area` 函数并传递 `rect1` 作为参数，现在我们可以使用**方法语法**来调用 `Rectangle` 实例上的 `area` 方法\[3\]。方法语法紧跟在实例之后：我们添加一个点，后面跟着方法名、括号以及任何参数。

在 `area` 的签名中，我们使用 `&self` 而不是 `rectangle: &Rectangle`。`&self` 实际上是 `self: &Self` 的简写。在 `impl` 块中，类型 `Self` 是该 `impl` 块所针对的类型的别名。方法必须将第一个参数命名为 `self`，其类型为 `Self`，所以 Rust 允许你在第一个参数位置只用名称 `self` 来缩写。请注意，我们仍然需要在 `self` 简写前使用 `&`，以表明这个方法借用了 `Self` 实例，就像我们在 `rectangle: &Rectangle` 中所做的那样。方法可以获取 `self` 的所有权，像这里一样不可变地借用 `self`，或者可变地借用 `self`，就像它们对待任何其他参数一样。

我们在这里选择使用 `&self` 的原因与在函数版本中使用 `&Rectangle` 的原因相同：我们不想获取所有权，只是想读取结构体中的数据，而不是写入数据。如果我们想在方法执行过程中改变调用该方法的实例，我们会将第一个参数使用 `&mut self`。使用仅以 `self` 作为第一个参数来获取实例所有权的方法很少见；这种技术通常用于方法将 `self` 转换为其他东西，并且你想防止调用者在转换后使用原始实例的情况。

使用方法而不是函数的主要原因，除了提供方法语法并且不必在每个方法的签名中重复 `self` 的类型之外，还在于组织性。我们把可以对一个类型的实例进行的所有操作都放在一个 `impl` 块中，而不是让我们代码的未来使用者在我们提供的库的各个地方去寻找 `Rectangle` 的功能。

请注意，我们可以选择给一个方法取与结构体的某个字段相同的名字。例如，我们可以在 `Rectangle` 上定义一个也叫 `width` 的方法：

文件名：`src/main.rs`

```rust
impl Rectangle {
    fn width(&self) -> bool {
        self.width > 0
    }
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    if rect1.width() {
        println!(
            "The rectangle has a nonzero width; it is {}",
            rect1.width
        );
    }
}
```

在这里，如果实例的 `width` 字段中的值大于 `0`，我们选择让 `width` 方法返回 `true`，如果值为 `0` 则返回 `false`：我们可以在同名的方法中出于任何目的使用字段。在 `main` 函数中，当我们在 `rect1.width` 后面加上括号时，Rust 知道我们指的是 `width` 方法。当我们不使用括号时，Rust 知道我们指的是 `width` 字段。

通常，但不总是，当我们给方法取与字段相同的名字时，我们希望它只返回字段中的值，不做其他事情。像这样的方法被称为**获取器**，Rust 不像其他一些语言那样为结构体字段自动实现它们。获取器很有用，因为你可以将字段设为私有，但方法设为公共，从而作为类型公共 API 的一部分实现对该字段的只读访问。我们将在第 7 章讨论什么是公共和私有，以及如何将字段或方法指定为公共或私有。

> **`->` 运算符在哪里？**
>
> 在 C 和 C++ 中，调用方法使用两种不同的运算符：如果你直接在对象上调用方法，使用 `.`；如果你在指向对象的指针上调用方法并且需要先解引用指针，则使用 `->`。换句话说，如果 `object` 是一个指针，`object->`something`()` 类似于 `(*object).`something`()`。
>
> Rust 没有与 `->` 运算符等效的东西；相反，Rust 有一个名为**自动引用和解引用**的特性。调用方法是 Rust 中具有这种行为的少数几个地方之一。
>
> 它的工作方式如下：当你使用 `object.`something`()` 调用方法时，Rust 会自动添加 `&`、`&mut` 或 `*`，以便 `object` 与方法的签名匹配。换句话说，以下两者是等效的：
>
>     p1.distance(&p2);
>     (&p1).distance(&p2);
>
> 第一个看起来更简洁。这种自动引用行为之所以有效，是因为方法有一个明确的接收者——`self` 的类型。给定接收者和方法名，Rust 可以明确地确定该方法是在读取（`&self`）、变异（`&mut self`）还是消耗（`self`）。Rust 使方法接收者的借用变得隐式，这在实践中是使所有权使用起来更方便的一个重要部分。
