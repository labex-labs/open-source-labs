# 线程

Rust 提供了一种通过 `spawn` 函数来创建原生操作系统线程的机制，该函数的参数是一个移动闭包。

```rust
use std::thread;

const NTHREADS: u32 = 10;

// 这是主线程
fn main() {
    // 创建一个向量来保存创建的子线程
    let mut children = vec![];

    for i in 0..NTHREADS {
        // 启动另一个线程
        children.push(thread::spawn(move || {
            println!("这是线程编号 {}", i);
        }));
    }

    for child in children {
        // 等待线程完成。返回一个结果
        let _ = child.join();
    }
}
```

这些线程将由操作系统进行调度。
