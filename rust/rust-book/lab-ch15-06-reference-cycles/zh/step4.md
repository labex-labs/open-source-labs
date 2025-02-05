# 创建树状数据结构：带有子节点的节点

首先，我们将构建一个树，其节点知道它们的子节点。我们将创建一个名为 `Node` 的结构体，它持有自己的 `i32` 值以及对其子节点 `Node` 值的引用：

文件名：`src/main.rs`

```rust
use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug)]
struct Node {
    value: i32,
    children: RefCell<Vec<Rc<Node>>>,
}
```

我们希望一个 `Node` 拥有它的子节点，并且我们希望与变量共享这种所有权，以便我们可以直接访问树中的每个 `Node`。为此，我们将 `Vec<T>` 项定义为 `Rc<Node>` 类型的值。我们还希望修改哪些节点是另一个节点的子节点，因此我们在 `children` 中有一个围绕 `Vec<Rc<Node>>` 的 `RefCell<T>`。

接下来，我们将使用我们的结构体定义，并创建一个名为 `leaf` 的 `Node` 实例，其值为 `3` 且没有子节点，以及另一个名为 `branch` 的实例，其值为 `5` 且 `leaf` 是其一个子节点，如清单 15 - 27 所示。

文件名：`src/main.rs`

```rust
fn main() {
    let leaf = Rc::new(Node {
        value: 3,
        children: RefCell::new(vec![]),
    });

    let branch = Rc::new(Node {
        value: 5,
        children: RefCell::new(vec![Rc::clone(&leaf)]),
    });
}
```

清单 15 - 27：创建一个没有子节点的 `leaf` 节点和一个以 `leaf` 为其子节点之一的 `branch` 节点

我们克隆了 `leaf` 中的 `Rc<Node>` 并将其存储在 `branch` 中，这意味着 `leaf` 中的 `Node` 现在有两个所有者：`leaf` 和 `branch`。我们可以通过 `branch.children` 从 `branch` 访问到 `leaf`，但无法从 `leaf` 访问到 `branch`。原因是 `leaf` 没有对 `branch` 的引用，并且不知道它们之间的关系。我们希望 `leaf` 知道 `branch` 是它的父节点。接下来我们就来实现这一点。
