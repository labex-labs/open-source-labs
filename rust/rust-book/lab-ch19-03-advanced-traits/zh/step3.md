# 默认泛型类型参数与运算符重载

当我们使用泛型类型参数时，可以为泛型类型指定一个默认的具体类型。如果默认类型适用，这样 trait 的实现者就无需指定具体类型。在使用 `<占位符类型=具体类型>` 语法声明泛型类型时指定默认类型。

这种技术很有用的一个绝佳例子是**运算符重载**，即你可以在特定情况下自定义运算符（如 `+`）的行为。

Rust 不允许你创建自己的运算符或重载任意运算符。但你可以通过实现与运算符相关联的 trait 来重载 `std::ops` 中列出的操作及相应 trait。例如，在清单 19-14 中，我们重载 `+` 运算符，以便将两个 `Point` 实例相加。我们通过在 `Point` 结构体上实现 `Add` trait 来做到这一点。

文件名：`src/main.rs`

```rust
use std::ops::Add;

#[derive(Debug, Copy, Clone, PartialEq)]
struct Point {
    x: i32,
    y: i32,
}

impl Add for Point {
    type Output = Point;

    fn add(self, other: Point) -> Point {
        Point {
            x: self.x + other.x,
            y: self.y + other.y,
        }
    }
}

fn main() {
    assert_eq!(
        Point { x: 1, y: 0 } + Point { x: 2, y: 3 },
        Point { x: 3, y: 3 }
    );
}
```

清单 19-14：为 `Point` 实例实现 `Add` trait 以重载 `+` 运算符

`add` 方法将两个 `Point` 实例的 `x` 值和 `y` 值相加，以创建一个新的 `Point`。`Add` trait 有一个名为 `Output` 的关联类型，它决定了 `add` 方法返回的类型。

这段代码中的默认泛型类型在 `Add` trait 内部。其定义如下：

    trait Add<Rhs=Self> {
        type Output;

        fn add(self, rhs: Rhs) -> Self::Output;
    }

这段代码总体上应该看起来很熟悉：一个带有一个方法和一个关联类型的 trait。新的部分是 `Rhs=Self`：这种语法称为**默认类型参数**。泛型类型参数 `Rhs`（“右手边”的缩写）定义了 `add` 方法中 `rhs` 参数的类型。当我们为 `Add` trait 实现时，如果不指定 `Rhs` 的具体类型，`Rhs` 的类型将默认为 `Self`，也就是我们正在为其实现 `Add` 的类型。

当我们为 `Point` 实现 `Add` 时，我们使用了 `Rhs` 的默认值，因为我们想要将两个 `Point` 实例相加。让我们看一个实现 `Add` trait 的例子，在这个例子中我们想要自定义 `Rhs` 类型而不是使用默认值。

我们有两个结构体 `Millimeters` 和 `Meters`，它们保存不同单位的值。在另一个结构体中对现有类型进行这种轻量级包装被称为**新类型模式**，我们将在“使用新类型模式为外部类型实现外部 trait”中更详细地描述它。我们想要将以毫米为单位的值与以米为单位的值相加，并让 `Add` 的实现正确地进行转换。我们可以为 `Millimeters` 实现 `Add`，将 `Meters` 作为 `Rhs`，如清单 19-15 所示。

文件名：`src/lib.rs`

```rust
use std::ops::Add;

struct Millimeters(u32);
struct Meters(u32);

impl Add<Meters> for Millimeters {
    type Output = Millimeters;

    fn add(self, other: Meters) -> Millimeters {
        Millimeters(self.0 + (other.0 * 1000))
    }
}
```

清单 19-15：在 `Millimeters` 上实现 `Add` trait 以将 `Millimeters` 和 `Meters` 相加

为了将 `Millimeters` 和 `Meters` 相加，我们指定 `impl Add<Meters>` 来设置 `Rhs` 类型参数的值，而不是使用默认的 `Self`。

你将主要以两种方式使用默认类型参数：

1.  在不破坏现有代码的情况下扩展类型
2.  在大多数用户不需要的特定情况下允许定制

标准库的 `Add` trait 是第二个目的的一个例子：通常，你会将两个相同类型相加，但 `Add` trait 提供了超越此限制的定制能力。在 `Add` trait 定义中使用默认类型参数意味着大多数时候你不必指定额外的参数。换句话说，不需要一些实现样板代码，这使得使用该 trait 更容易。

第一个目的与第二个目的类似，但方向相反：如果你想向现有 trait 添加一个类型参数，可以给它一个默认值，以便在不破坏现有实现代码的情况下扩展 trait 的功能。
