# 使用 Rc`<T>` 和 RefCell`<T>` 允许可变数据有多个所有者

使用 `RefCell<T>` 的一种常见方式是将其与 `Rc<T>` 结合使用。回忆一下，`Rc<T>` 允许你对某些数据有多个所有者，但它只提供对该数据的不可变访问。如果你有一个持有 `RefCell<T>` 的 `Rc<T>`，你可以得到一个既能有多个所有者**又**能变异的值！

例如，回忆一下清单 15 - 18 中的链表示例，我们使用 `Rc<T>` 允许多个链表共享另一个链表的所有权。因为 `Rc<T>` 只持有不可变值，一旦我们创建了链表中的值，就不能再更改它们。让我们加入 `RefCell<T>` 以获得更改链表中值的能力。清单 15 - 24 展示了通过在 `Cons` 定义中使用 `RefCell<T>`，我们可以修改存储在所有链表中的值。

文件名：`src/main.rs`

```rust
#[derive(Debug)]
enum List {
    Cons(Rc<RefCell<i32>>, Rc<List>),
    Nil,
}

use crate::List::{Cons, Nil};
use std::cell::RefCell;
use std::rc::Rc;

fn main() {
  1 let value = Rc::new(RefCell::new(5));

  2 let a = Rc::new(Cons(Rc::clone(&value), Rc::new(Nil)));

    let b = Cons(Rc::new(RefCell::new(3)), Rc::clone(&a));
    let c = Cons(Rc::new(RefCell::new(4)), Rc::clone(&a));

  3 *value.borrow_mut() += 10;

    println!("a after = {:?}", a);
    println!("b after = {:?}", b);
    println!("c after = {:?}", c);
}
```

清单 15 - 24：使用 `Rc<RefCell<i32>>` 创建一个我们可以变异的 `List`

我们创建一个 `Rc<RefCell<i32>>` 实例的值，并将其存储在名为 `value` 的变量中 \[1\]，这样我们稍后就可以直接访问它。然后我们在 `a` 中创建一个 `List`，其 `Cons` 变体持有 `value` \[2\]。我们需要克隆 `value`，这样 `a` 和 `value` 都拥有内部值 `5` 的所有权，而不是将所有权从 `value` 转移到 `a`，或者让 `a` 从 `value` 借用。

我们将链表 `a` 包装在一个 `Rc<T>` 中，这样当我们创建链表 `b` 和 `c` 时，它们都可以引用 `a`，这与我们在清单 15 - 18 中所做的一样。

在我们创建了 `a`、`b` 和 `c` 中的链表之后，我们想将 `value` 中的值增加 10 \[3\]。我们通过对 `value` 调用 `borrow_mut` 来做到这一点，它使用了我们在“`->` 运算符在哪里？”中讨论的自动解引用功能，将 `Rc<T>` 解引用为内部的 `RefCell<T>` 值。`borrow_mut` 方法返回一个 `RefMut<T>` 智能指针，我们对其使用解引用运算符并更改内部值。

当我们打印 `a`、`b` 和 `c` 时，可以看到它们都有修改后的值 `15` 而不是 `5`：

    a after = Cons(RefCell { value: 15 }, Nil)
    b after = Cons(RefCell { value: 3 }, Cons(RefCell { value: 15 }, Nil))
    c after = Cons(RefCell { value: 4 }, Cons(RefCell { value: 15 }, Nil))

这种技术非常巧妙！通过使用 `RefCell<T>`，我们有一个表面上不可变的 `List` 值。但我们可以使用 `RefCell<T>` 上提供对其内部可变性访问的方法，这样在需要时就可以修改我们的数据。借用规则的运行时检查保护我们免受数据竞争的影响，并且在我们的数据结构中为了这种灵活性而牺牲一点速度有时是值得的。请注意，`RefCell<T>` 不适用于多线程代码！`Mutex<T>` 是 `RefCell<T>` 的线程安全版本，我们将在第 16 章讨论 `Mutex<T>`。
