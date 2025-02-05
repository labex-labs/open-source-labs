# 通道与所有权转移

所有权规则在消息发送中起着至关重要的作用，因为它们有助于你编写安全的并发代码。在整个 Rust 程序中考虑所有权是防止并发编程错误的优势。让我们做一个实验来展示通道和所有权是如何协同工作以防止问题的：我们将尝试在通过通道发送 `val` 值之后，在新创建的线程中使用它。尝试编译清单 16 - 9 中的代码，看看为什么这段代码不被允许。

文件名：`src/main.rs`

```rust
use std::sync::mpsc;
use std::thread;

fn main() {
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        let val = String::from("hi");
        tx.send(val).unwrap();
        println!("val is {val}");
    });

    let received = rx.recv().unwrap();
    println!("Got: {received}");
}
```

清单 16 - 9：在通过通道发送 `val` 之后尝试使用它

在这里，我们在通过 `tx.send` 将 `val` 发送到通道之后，尝试打印 `val`。允许这样做会是个坏主意：一旦值被发送到另一个线程，在我们再次尝试使用该值之前，那个线程可能会修改或丢弃它。潜在地，其他线程的修改可能会由于数据不一致或不存在而导致错误或意外结果。然而，如果我们尝试编译清单 16 - 9 中的代码，Rust 会给我们一个错误：

```bash
error[E0382]: borrow of moved value: `val`
  --> src/main.rs:10:31
   |
8  |         let val = String::from("hi");
   |             --- move occurs because `val` has type `String`, which does
not implement the `Copy` trait
9  |         tx.send(val).unwrap();
   |                 --- value moved here
10 |         println!("val is {val}");
   |                           ^^^ value borrowed here after move
```

我们的并发错误导致了一个编译时错误。`send` 函数获取其参数的所有权，并且当值被移动时，接收者获取它的所有权。这阻止了我们在发送值之后意外地再次使用它；所有权系统会检查一切是否正常。
