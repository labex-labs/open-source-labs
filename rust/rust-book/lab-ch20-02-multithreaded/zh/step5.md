# 创建有限数量的线程

我们希望我们的线程池以一种类似且熟悉的方式工作，这样从线程切换到线程池时，使用我们 API 的代码无需进行大量更改。清单 20-12 展示了我们想要使用的`ThreadPool`结构体的假设接口，以此来替代`thread::spawn`。

文件名：`src/main.rs`

```rust
fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();
  1 let pool = ThreadPool::new(4);

    for stream in listener.incoming() {
        let stream = stream.unwrap();

      2 pool.execute(|| {
            handle_connection(stream);
        });
    }
}
```

清单 20-12：我们理想中的`ThreadPool`接口

我们使用`ThreadPool::new`来创建一个新的线程池，其线程数量可配置，在这种情况下是四个\[1\]。然后，在`for`循环中，`pool.execute`具有与`thread::spawn`类似的接口，即它接受一个闭包，线程池会为每个流运行该闭包\[2\]。我们需要实现`pool.execute`，使其接受闭包并将其交给线程池中的一个线程来运行。这段代码目前还无法编译，但我们会尝试一下，以便编译器能指导我们如何修复它。
