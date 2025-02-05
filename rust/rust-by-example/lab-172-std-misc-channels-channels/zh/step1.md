# 通道

Rust提供了用于线程间通信的异步 `通道`。通道允许在两个端点之间进行单向信息流传输：`发送端`（Sender）和 `接收端`（Receiver）。

```rust
use std::sync::mpsc::{Sender, Receiver};
use std::sync::mpsc;
use std::thread;

static NTHREADS: i32 = 3;

fn main() {
    // 通道有两个端点：`Sender<T>` 和 `Receiver<T>`，
    // 其中 `T` 是要传输的消息类型
    // （类型注释是多余的）
    let (tx, rx): (Sender<i32>, Receiver<i32>) = mpsc::channel();
    let mut children = Vec::new();

    for id in 0..NTHREADS {
        // 发送端端点可以被复制
        let thread_tx = tx.clone();

        // 每个线程将通过通道发送其ID
        let child = thread::spawn(move || {
            // 线程获取 `thread_tx` 的所有权
            // 每个线程在通道中排队一条消息
            thread_tx.send(id).unwrap();

            // 发送是一个非阻塞操作，线程在发送消息后将立即继续
            println!("thread {} finished", id);
        });

        children.push(child);
    }

    // 在这里，所有消息都被收集
    let mut ids = Vec::with_capacity(NTHREADS as usize);
    for _ in 0..NTHREADS {
        // `recv` 方法从通道中选取一条消息
        // 如果没有可用消息，`recv` 将阻塞当前线程
        ids.push(rx.recv());
    }

    // 等待线程完成任何剩余工作
    for child in children {
        child.join().expect("oops! the child thread panicked");
    }

    // 显示消息发送的顺序
    println!("{:?}", ids);
}
```
