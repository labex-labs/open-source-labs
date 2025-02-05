# 关于 cons 列表的更多信息

「cons 列表」是一种源自 Lisp 编程语言及其方言的数据结构，由嵌套的对组成，是链表的 Lisp 版本。它的名字来源于 Lisp 中的 `cons` 函数（构造函数的缩写），该函数从两个参数构造一个新的对。通过对由一个值和另一个对组成的对调用 `cons`，我们可以构造由递归对组成的 cons 列表。

例如，这里是一个包含列表 `1, 2, 3` 的 cons 列表的伪代码表示，每个对用括号括起来：

```rust
(1, (2, (3, Nil)))
```

cons 列表中的每个项包含两个元素：当前项的值和下一项。列表中的最后一项只包含一个名为 `Nil` 的值，没有下一项。cons 列表是通过递归调用 `cons` 函数生成的。表示递归基例的规范名称是 `Nil`。请注意，这与第 6 章中的「null」或「nil」概念不同，后者是一个无效或缺失的值。

cons 列表在 Rust 中不是常用的数据结构。在 Rust 中，大多数时候当你有一个项的列表时，`Vec<T>` 是更好的选择。其他更复杂的递归数据类型在各种情况下是有用的，但是通过在本章中从 cons 列表开始，我们可以探索盒指针如何让我们定义一个递归数据类型而不会有太多干扰。

清单 15-2 包含了一个 cons 列表的枚举定义。请注意，这段代码还不能编译，因为 `List` 类型的大小未知，我们将对此进行演示。

文件名：`src/main.rs`

```rust
enum List {
    Cons(i32, List),
    Nil,
}
```

清单 15-2：定义一个枚举来表示 `i32` 值的 cons 列表数据结构的首次尝试

> 注意：为了这个示例的目的，我们正在实现一个只包含 `i32` 值的 cons 列表。正如我们在第 10 章中讨论的，我们可以使用泛型来实现它，以定义一个可以存储任何类型值的 cons 列表类型。

使用 `List` 类型来存储列表 `1, 2, 3` 看起来会像清单 15-3 中的代码。

文件名：`src/main.rs`

```rust
--snip--

use crate::List::{Cons, Nil};

fn main() {
    let list = Cons(1, Cons(2, Cons(3, Nil)));
}
```

清单 15-3：使用 `List` 枚举来存储列表 `1, 2, 3`

第一个 `Cons` 值包含 `1` 和另一个 `List` 值。这个 `List` 值是另一个 `Cons` 值，它包含 `2` 和另一个 `List` 值。这个 `List` 值是另一个 `Cons` 值，它包含 `3` 和一个 `List` 值，最后这个 `List` 值是 `Nil`，即表示列表结束的非递归变体。

如果我们尝试编译清单 15-3 中的代码，我们会得到清单 15-4 中所示的错误。

```bash
error[E0072]: recursive type `List` has infinite size
 --> src/main.rs:1:1
  |
1 | enum List {
  | ^^^^^^^^^ recursive type has infinite size
2 |     Cons(i32, List),
  |               ---- recursive without indirection
  |
help: insert some indirection (e.g., a `Box`, `Rc`, or `&`) to make `List`
representable
  |
2 |     Cons(i32, Box<List>),
  |               ++++    +
```

清单 15-4：尝试定义递归枚举时得到的错误

错误显示这个类型「大小无限」。原因是我们定义的 `List` 有一个递归变体：它直接包含自身的另一个值。因此，Rust 无法确定存储一个 `List` 值需要多少空间。让我们来分析一下为什么会得到这个错误。首先，我们来看看 Rust 如何确定存储一个非递归类型的值需要多少空间。
