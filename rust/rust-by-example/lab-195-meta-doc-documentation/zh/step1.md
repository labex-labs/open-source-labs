# 文档

使用 `cargo doc` 在 `target/doc` 中生成文档。

使用 `cargo test` 运行所有测试（包括文档测试），使用 `cargo test --doc` 仅运行文档测试。

这些命令将根据需要适当地调用 `rustdoc`（以及 `rustc`）。

## 文档注释

文档注释对于需要文档的大型项目非常有用。在运行 `rustdoc` 时，这些注释会被编译为文档。它们由 `///` 表示，并支持 [Markdown]。

````rust
#![crate_name = "doc"]

/// 这里表示一个人
pub struct Person {
    /// 一个人必须有一个名字，不管朱丽叶有多讨厌它
    name: String,
}

impl Person {
    /// 返回一个具有给定名字的人
    ///
    /// # 参数
    ///
    /// * `name` - 一个字符串切片，包含这个人的名字
    ///
    /// # 示例
    ///
    /// ```
    /// // 你可以在注释中的围栏内包含 Rust 代码
    /// // 如果你将 --test 传递给 `rustdoc`，它甚至会为你测试！
    /// use doc::Person;
    /// let person = Person::new("name");
    /// ```
    pub fn new(name: &str) -> Person {
        Person {
            name: name.to_string(),
        }
    }

    /// 友好地打招呼！
    ///
    /// 对调用它的 `Person` 说 "Hello, [name](Person::name)"。
    pub fn hello(& self) {
        println!("Hello, {}!", self.name);
    }
}

fn main() {
    let john = Person::new("John");

    john.hello();
}
````

要运行测试，首先将代码构建为库，然后告诉 `rustdoc` 在哪里找到库，以便它可以将其链接到每个文档测试程序中：

```shell
$ rustc doc.rs --crate-type lib
$ rustdoc --test --extern doc="libdoc.rlib" doc.rs
```

## 文档属性

以下是一些与 `rustdoc` 一起使用的最常见的 `#[doc]` 属性示例。

## `inline`

用于内联文档，而不是链接到单独的页面。

```rust
#[doc(inline)]
pub use bar::Bar;

/// bar 文档
mod bar {
    /// Bar 的文档
    pub struct Bar;
}
```

## `no_inline`

用于防止链接到单独的页面或任何地方。

```rust
// 来自 libcore/prelude 的示例
#[doc(no_inline)]
pub use crate::mem::drop;
```

## `hidden`

使用此属性会告诉 `rustdoc` 不要将其包含在文档中：

```rust
// 来自 futures-rs 库的示例
#[doc(hidden)]
pub use self::async_await::*;
```

对于文档，`rustdoc` 在社区中被广泛使用。它用于生成 [标准库文档](https://doc.rust-lang.org/std/)。
