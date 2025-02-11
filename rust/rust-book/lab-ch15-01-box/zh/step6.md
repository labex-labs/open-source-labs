# 使用 `Box<T>` 获得大小已知的递归类型

由于 Rust 无法确定为递归定义的类型分配多少空间，编译器会给出一个带有如下有用建议的错误：

    help: insert some indirection (e.g., a `Box`, `Rc`, or `&`) to make `List`
    representable
      |
    2 |     Cons(i32, Box<List>),
      |               ++++    +

在这个建议中，「间接性」意味着我们不应直接存储值，而是应该通过存储指向该值的指针来间接存储值，从而改变数据结构。

因为 `Box<T>` 是一个指针，Rust 始终知道一个 `Box<T>` 需要多少空间：指针的大小不会因其所指向的数据量而改变。这意味着我们可以在 `Cons` 变体中放入一个 `Box<T>`，而不是直接放入另一个 `List` 值。`Box<T>` 将指向堆上的下一个 `List` 值，而不是在 `Cons` 变体内部。从概念上讲，我们仍然有一个列表，它由包含其他列表的列表组成，但现在这种实现更像是将这些项并排放置，而不是相互嵌套。

我们可以将清单 15-2 中 `List` 枚举的定义以及清单 15-3 中 `List` 的用法更改为清单 15-5 中的代码，这样代码就能编译通过了。

文件名：`src/main.rs`

```rust
enum List {
    Cons(i32, Box<List>),
    Nil,
}

use crate::List::{Cons, Nil};

fn main() {
    let list = Cons(
        1,
        Box::new(Cons(
            2,
            Box::new(Cons(
                3,
                Box::new(Nil)
            ))
        ))
    );
}
```

清单 15-5：使用 `Box<T>` 以使大小已知的 `List` 的定义

`Cons` 变体需要一个 `i32` 的大小加上存储盒子指针数据的空间。`Nil` 变体不存储任何值，所以它需要的空间比 `Cons` 变体少。现在我们知道任何 `List` 值将占用一个 `i32` 的大小加上盒子指针数据的大小。通过使用盒子，我们打破了无限的递归链，这样编译器就能算出存储一个 `List` 值所需的大小。图 15-2 展示了现在 `Cons` 变体的样子。

图 15-2：一个大小不是无限的 `List`，因为 `Cons` 包含一个 `Box`

盒子只提供间接性和堆分配；它们没有任何其他特殊功能，比如我们将在其他智能指针类型中看到的那些功能。它们也没有这些特殊功能所带来的性能开销，所以在像 cons 列表这样间接性是我们唯一需要的功能的情况下，它们可能会很有用。我们将在第 17 章中查看盒子的更多用例。

`Box<T>` 类型是一个智能指针，因为它实现了 `Deref` 特性，这使得 `Box<T>` 值可以像引用一样被处理。当一个 `Box<T>` 值超出作用域时，由于 `Drop` 特性的实现，盒子所指向的堆数据也会被清理。这两个特性对于我们在本章剩余部分将讨论的其他智能指针类型所提供的功能来说将更加重要。让我们更详细地探讨这两个特性。
