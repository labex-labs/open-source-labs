# 从子节点添加到父节点的引用

为了使子节点知道它的父节点，我们需要在 `Node` 结构体定义中添加一个 `parent` 字段。问题在于确定 `parent` 的类型应该是什么。我们知道它不能包含 `Rc<T>`，因为那样会创建一个引用循环，即 `leaf.parent` 指向 `branch`，而 `branch.children` 指向 `leaf`，这会导致它们的 `strong_count` 值永远不会为 0。

从另一个角度考虑这种关系，父节点应该拥有它的子节点：如果父节点被丢弃，它的子节点也应该被丢弃。然而，子节点不应该拥有它的父节点：如果我们丢弃一个子节点，父节点仍然应该存在。这正是弱引用的用武之地！

所以，我们将 `parent` 的类型设为 `Weak<T>`，具体是 `RefCell<Weak<Node>>`，而不是 `Rc<T>`。现在我们的 `Node` 结构体定义如下：

文件名：`src/main.rs`

```rust
use std::cell::RefCell;
use std::rc::{Rc, Weak};

#[derive(Debug)]
struct Node {
    value: i32,
    parent: RefCell<Weak<Node>>,
    children: RefCell<Vec<Rc<Node>>>,
}
```

一个节点将能够引用它的父节点，但并不拥有它的父节点。在清单 15 - 28 中，我们更新 `main` 函数以使用这个新定义，这样 `leaf` 节点就有办法引用它的父节点 `branch` 了。

文件名：`src/main.rs`

```rust
fn main() {
    let leaf = Rc::new(Node {
        value: 3,
        parent: RefCell::new(Weak::new()),
        children: RefCell::new(vec![]),
    });

    println!(
        "leaf parent = {:?}",
        leaf.parent.borrow().upgrade()
    );

    let branch = Rc::new(Node {
        value: 5,
        parent: RefCell::new(Weak::new()),
        children: RefCell::new(vec![Rc::clone(&leaf)]),
    });

    *leaf.parent.borrow_mut() = Rc::downgrade(&branch);

    println!(
        "leaf parent = {:?}",
        leaf.parent.borrow().upgrade()
    );
}
```

清单 15 - 28：一个 `leaf` 节点对其父节点 `branch` 有弱引用

创建 `leaf` 节点与清单 15 - 27 类似，只是多了 `parent` 字段：`leaf` 一开始没有父节点，所以我们创建一个新的、空的 `Weak<Node>` 引用实例 \[1\]。

此时，当我们尝试通过 `upgrade` 方法获取 `leaf` 的父节点引用时，会得到一个 `None` 值。我们可以在第一个 `println!` 语句的输出中看到这一点 \[2\]：

```rust
leaf parent = None
```

当我们创建 `branch` 节点时，它在 `parent` 字段中也会有一个新的 `Weak<Node>` 引用 \[3\]，因为 `branch` 没有父节点。我们仍然将 `leaf` 作为 `branch` 的子节点之一。一旦我们有了 `branch` 中的 `Node` 实例，就可以修改 `leaf` 来给它一个指向其父节点的 `Weak<Node>` 引用 \[4\]。我们对 `leaf` 的 `parent` 字段中的 `RefCell<Weak<Node>>` 使用 `borrow_mut` 方法，然后使用 `Rc::downgrade` 函数从 `branch` 中的 `Rc<Node>` 创建一个指向 `branch` 的 `Weak<Node>` 引用。

当我们再次打印 `leaf` 的父节点时 \[5\]，这次我们会得到一个包含 `branch` 的 `Some` 变体：现在 `leaf` 可以访问它的父节点了！当我们打印 `leaf` 时，也避免了像清单 15 - 26 中那样最终导致堆栈溢出的循环；`Weak<Node>` 引用被打印为 `(Weak)`：

    leaf parent = Some(Node { value: 5, parent: RefCell { value: (Weak) },
    children: RefCell { value: [Node { value: 3, parent: RefCell { value: (Weak) },
    children: RefCell { value: [] } }] } })

没有无限输出表明这段代码没有创建引用循环。我们也可以通过查看调用 `Rc::strong_count` 和 `Rc::weak_count` 得到的值来判断这一点。
