# 可视化 `strong_count` 和 `weak_count` 的变化

让我们通过创建一个新的内部作用域并将 `branch` 的创建移动到该作用域中来看看 `Rc<Node>` 实例的 `strong_count` 和 `weak_count` 值是如何变化的。这样做，我们可以看到当创建 `branch` 然后它超出作用域被丢弃时会发生什么。修改内容如清单 15 - 29 所示。

文件名：`src/main.rs`

```rust
fn main() {
    let leaf = Rc::new(Node {
        value: 3,
        parent: RefCell::new(Weak::new()),
        children: RefCell::new(vec![]),
    });

    println!(
        "leaf strong = {}, weak = {}",
        Rc::strong_count(&leaf),
        Rc::weak_count(&leaf),
    );

    {
        let branch = Rc::new(Node {
            value: 5,
            parent: RefCell::new(Weak::new()),
            children: RefCell::new(vec![Rc::clone(&leaf)]),
        });

        *leaf.parent.borrow_mut() = Rc::downgrade(&branch);

        println!(
            "branch strong = {}, weak = {}",
            Rc::strong_count(&branch),
            Rc::weak_count(&branch),
        );

        println!(
            "leaf strong = {}, weak = {}",
            Rc::strong_count(&leaf),
            Rc::weak_count(&leaf),
        );
    }

    println!(
        "leaf parent = {:?}",
        leaf.parent.borrow().upgrade()
    );

    println!(
        "leaf strong = {}, weak = {}",
        Rc::strong_count(&leaf),
        Rc::weak_count(&leaf),
    );
}
```

清单 15 - 29：在内部作用域中创建 `branch` 并检查强引用和弱引用计数

创建 `leaf` 之后，它的 `Rc<Node>` 的强引用计数为 1，弱引用计数为 0 \[1\]。在内部作用域 \[2\] 中，我们创建 `branch` 并将其与 `leaf` 关联，此时当我们打印计数时 \[3\]，`branch` 中的 `Rc<Node>` 的强引用计数为 1，弱引用计数为 1（因为 `leaf.parent` 用 `Weak<Node>` 指向 `branch`）。当我们打印 `leaf` 中的计数时 \[4\]，我们会看到它的强引用计数为 2，因为 `branch` 现在在 `branch.children` 中存储了 `leaf` 的 `Rc<Node>` 的克隆，但弱引用计数仍为 0。

当内部作用域结束时 \[5\]，`branch` 超出作用域，`Rc<Node>` 的强引用计数减少到 0，所以它的 `Node` 被丢弃。来自 `leaf.parent` 的弱引用计数 1 与 `Node` 是否被丢弃无关，所以我们不会有任何内存泄漏！

如果我们在作用域结束后尝试访问 `leaf` 的父节点，我们会再次得到 `None` \[6\]。在程序结束时 \[7\]，`leaf` 中的 `Rc<Node>` 的强引用计数为 1，弱引用计数为 0，因为变量 `leaf` 现在又是对 `Rc<Node>` 的唯一引用。

所有管理计数和值丢弃的逻辑都内置于 `Rc<T>` 和 `Weak<T>` 以及它们对 `Drop` 特性的实现中。通过在 `Node` 的定义中指定从子节点到父节点的关系应该是一个 `Weak<T>` 引用，你能够让父节点指向子节点，反之亦然，而不会创建引用循环和内存泄漏。
