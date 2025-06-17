# 使用 Rc`<T>` 来共享数据

让我们回到清单 15-5 中的链表示例。还记得我们是使用 `Box<T>` 来定义它的。这次，我们将创建两个链表，它们都共享对第三个链表的所有权。从概念上讲，这类似于图 15-3。

图 15-3：两个链表 `b` 和 `c`，共享对第三个链表 `a` 的所有权

我们将创建包含 `5` 然后是 `10` 的链表 `a`。然后我们再创建另外两个链表：以 `3` 开头的 `b` 和以 `4` 开头的 `c`。然后 `b` 和 `c` 链表都将继续连接到包含 `5` 和 `10` 的第一个 `a` 链表。换句话说，两个链表将共享包含 `5` 和 `10` 的第一个链表。

尝试使用我们用 `Box<T>` 定义的 `List` 来实现这种情况是行不通的，如清单 15-17 所示。

文件名：`src/main.rs`

```rust
enum List {
    Cons(i32, Box<List>),
    Nil,
}

use crate::List::{Cons, Nil};

fn main() {
    let a = Cons(5, Box::new(Cons(10, Box::new(Nil))));
  1 let b = Cons(3, Box::new(a));
  2 let c = Cons(4, Box::new(a));
}
```

清单 15-17：演示使用 `Box<T>` 时不允许有两个链表尝试共享对第三个链表的所有权

当我们编译这段代码时，会得到如下错误：

```bash
error[E0382]: use of moved value: `a`
  --> src/main.rs:11:30
   |
9  |     let a = Cons(5, Box::new(Cons(10, Box::new(Nil))));
   |         - move occurs because `a` has type `List`, which
does not implement the `Copy` trait
10 |     let b = Cons(3, Box::new(a));
   |                              - value moved here
11 |     let c = Cons(4, Box::new(a));
   |                              ^ value used here after move
```

`Cons` 变体拥有它们所包含的数据，所以当我们创建 `b` 链表时 \[1\]，`a` 被移动到 `b` 中，并且 `b` 拥有 `a`。然后，当我们在创建 `c` 时再次尝试使用 `a` 时 \[2\]，我们不被允许这样做，因为 `a` 已经被移动了。

我们可以将 `Cons` 的定义改为持有引用，但那样我们就必须指定生命周期参数。通过指定生命周期参数，我们将指定链表中的每个元素至少与整个链表存活的时间一样长。清单 15-17 中的元素和链表就是这种情况，但并非在每个场景中都是如此。

相反，我们将把 `List` 的定义改为使用 `Rc<T>` 来代替 `Box<T>`，如清单 15-18 所示。现在每个 `Cons` 变体将持有一个值和一个指向 `List` 的 `Rc<T>`。当我们创建 `b` 时，我们不会获取 `a` 的所有权，而是克隆 `a` 所持有 `Rc<List>`，从而将引用数量从一增加到二，并让 `a` 和 `b` 共享该 `Rc<List>` 中的数据所有权。我们在创建 `c` 时也会克隆 `a`，将引用数量从二增加到三。每次我们调用 `Rc::clone` 时，`Rc<List>` 中数据的引用计数都会增加，并且除非对其没有引用，否则数据不会被清理。

文件名：`src/main.rs`

```rust
enum List {
    Cons(i32, Rc<List>),
    Nil,
}

use crate::List::{Cons, Nil};
1 use std::rc::Rc;

fn main() {
  2 let a = Rc::new(Cons(5, Rc::new(Cons(10, Rc::new(Nil)))));
  3 let b = Cons(3, Rc::clone(&a));
  4 let c = Cons(4, Rc::clone(&a));
}
```

清单 15-18：使用 `Rc<T>` 的 `List` 定义

我们需要添加一个 `use` 语句将 `Rc<T>` 引入作用域 \[1\]，因为它不在 prelude 中。在 `main` 函数中，我们创建包含 `5` 和 `10` 的链表并将其存储在 `a` 中的一个新的 `Rc<List>` 中 \[2\]。然后，当我们创建 `b` \[3\] 和 `c` \[4\] 时，我们调用 `Rc::clone` 函数并将对 `a` 中 `Rc<List>` 的引用作为参数传递。

我们本可以调用 `a.clone()` 而不是 `Rc::clone(&a)`，但在这种情况下 Rust 的惯例是使用 `Rc::clone`。`Rc::clone` 的实现不像大多数类型的 `clone` 实现那样对所有数据进行深拷贝。对 `Rc::clone` 的调用只会增加引用计数，这不会花费太多时间。数据的深拷贝可能会花费很多时间。通过使用 `Rc::clone` 进行引用计数，我们可以在视觉上区分深拷贝类型的克隆和增加引用计数的克隆类型。在查找代码中的性能问题时，我们只需要考虑深拷贝克隆，并且可以忽略对 `Rc::clone` 的调用。
