# 使用类型别名创建类型同义词

Rust 提供了声明*类型别名*的功能，为现有类型赋予另一个名称。为此我们使用 `type` 关键字。例如，我们可以像这样为 `i32` 创建别名 `Kilometers`：

```rust
type Kilometers = i32;
```

现在，别名 `Kilometers` 是 `i32` 的*同义词*；与我们在清单 19-15 中创建的 `Millimeters` 和 `Meters` 类型不同，`Kilometers` 不是一个单独的新类型。具有 `Kilometers` 类型的值将被视为与 `i32` 类型的值相同：

    type Kilometers = i32;

    let x: i32 = 5;
    let y: Kilometers = 5;

    println!("x + y = {}", x + y);

因为 `Kilometers` 和 `i32` 是同一类型，所以我们可以将这两种类型的值相加，并且可以将 `Kilometers` 值传递给接受 `i32` 参数的函数。然而，使用这种方法，我们无法获得前面讨论的新类型模式所带来的类型检查优势。换句话说，如果我们在某处混淆了 `Kilometers` 和 `i32` 值，编译器不会给我们报错。

类型同义词的主要用例是减少重复。例如，我们可能有一个很长的类型，如下所示：

```rust
Box<dyn Fn() + Send + 'static>
```

在函数签名中以及在整个代码中作为类型注释编写这个冗长的类型既麻烦又容易出错。想象一下有一个项目充满了像清单 19-24 那样的代码。

```rust
let f: Box<dyn Fn() + Send + 'static> = Box::new(|| {
    println!("hi");
});

fn takes_long_type(f: Box<dyn Fn() + Send + 'static>) {
    --snip--
}

fn returns_long_type() -> Box<dyn Fn() + Send + 'static> {
    --snip--
}
```

清单 19-24：在多处使用长类型

通过减少重复，类型别名使这段代码更易于管理。在清单 19-25 中，我们为这个冗长的类型引入了一个名为 `Thunk` 的别名，并可以用更短的别名 `Thunk` 替换该类型的所有使用。

    type Thunk = Box<dyn Fn() + Send + 'static>;

    let f: Thunk = Box::new(|| println!("hi"));

    fn takes_long_type(f: Thunk) {
        --snip--
    }

    fn returns_long_type() -> Thunk {
        --snip--
    }

清单 19-25：引入类型别名 `Thunk` 以减少重复

这段代码读写起来要容易得多！为类型别名选择一个有意义的名称也有助于传达你的意图（_thunk_ 是指稍后要计算的代码，所以它是存储闭包的合适名称）。

类型别名也常用于 `Result<T, E>` 类型以减少重复。考虑标准库中的 `std::io` 模块。I/O 操作通常返回一个 `Result<T, E>` 来处理操作失败的情况。这个库有一个 `std::io::Error` 结构体来表示所有可能的 I/O 错误。`std::io` 中的许多函数将返回 `Result<T, E>`，其中 `E` 是 `std::io::Error`，比如 `Write` trait 中的这些函数：

```rust
use std::fmt;
use std::io::Error;

pub trait Write {
    fn write(&mut self, buf: &[u8]) -> Result<usize, Error>;
    fn flush(&mut self) -> Result<(), Error>;

    fn write_all(&mut self, buf: &[u8]) -> Result<(), Error>;
    fn write_fmt(
        &mut self,
        fmt: fmt::Arguments,
    ) -> Result<(), Error>;
}
```

`Result<..., Error>` 被大量重复。因此，`std::io` 有这样的类型别名声明：

```rust
type Result<T> = std::result::Result<T, std::io::Error>;
```

因为这个声明在 `std::io` 模块中，我们可以使用完全限定的别名 `std::io::Result<T>`；也就是说，一个 `Result<T, E>`，其中 `E` 被填充为 `std::io::Error`。`Write` trait 的函数签名最终看起来像这样：

```rust
pub trait Write {
    fn write(&mut self, buf: &[u8]) -> Result<usize>;
    fn flush(&mut self) -> Result<()>;

    fn write_all(&mut self, buf: &[u8]) -> Result<()>;
    fn write_fmt(&mut self, fmt: fmt::Arguments) -> Result<()>;
}
```

类型别名在两个方面有所帮助：它使代码更易于编写，并且在整个 `std::io` 中为我们提供了一致的接口。因为它是一个别名，它只是另一个 `Result<T, E>`，这意味着我们可以对它使用任何适用于 `Result<T, E>` 的方法，以及像 `?` 运算符这样的特殊语法。
