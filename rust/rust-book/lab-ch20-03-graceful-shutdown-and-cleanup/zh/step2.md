# 在线程池上实现 Drop 特性

让我们从在线程池上实现 `Drop` 特性开始。当线程池被丢弃时，我们的线程应该全部调用 `join` 以确保它们完成工作。清单 20-22 展示了对 `Drop` 实现的首次尝试；这段代码目前还不能正常工作。

文件名：`src/lib.rs`

```rust
impl Drop for ThreadPool {
    fn drop(&mut self) {
      1 for worker in &mut self.workers {
          2 println!("Shutting down worker {}", worker.id);

          3 worker.thread.join().unwrap();
        }
    }
}
```

清单 20-22：当线程池超出作用域时，让每个线程调用 join

首先，我们遍历线程池中的每个 `worker` \[1\]。这里我们使用 `&mut`，因为 `self` 是一个可变引用，并且我们还需要能够修改 `worker`。对于每个 `worker`，我们打印一条消息，表明这个特定的 `Worker` 实例正在关闭 \[2\]，然后我们在该 `Worker` 实例的线程上调用 `join` \[3\]。如果对 `join` 的调用失败，我们使用 `unwrap` 使 Rust 发生恐慌并进入非优雅关闭状态。

当我们编译这段代码时，会得到以下错误：

```bash
error[E0507]: cannot move out of `worker.thread` which is behind a mutable
reference
    --> src/lib.rs:52:13
     |
52   |             worker.thread.join().unwrap();
     |             ^^^^^^^^^^^^^ ------ `worker.thread` moved due to this
method call
     |             |
     |             move occurs because `worker.thread` has type
`JoinHandle<()>`, which does not implement the `Copy` trait
     |
note: this function takes ownership of the receiver `self`, which moves
`worker.thread`
```

错误提示我们不能调用 `join`，因为我们对每个 `worker` 只有一个可变借用，而 `join` 会获取其参数的所有权。为了解决这个问题，我们需要将线程从拥有 `thread` 的 `Worker` 实例中移出，这样 `join` 才能消耗该线程。我们在清单 17-15 中就是这么做的：如果 `Worker` 持有一个 `Option<thread::JoinHandle<()>>`，而不是其他类型，我们就可以在 `Option` 上调用 `take` 方法，将值从 `Some` 变体中移出，并在其位置留下一个 `None` 变体。换句话说，正在运行的 `Worker` 在 `thread` 中会有一个 `Some` 变体，当我们想要清理一个 `Worker` 时，我们会用 `None` 替换 `Some`，这样 `Worker` 就没有线程可运行了。

所以我们知道需要像这样更新 `Worker` 的定义：

文件名：`src/lib.rs`

```rust
struct Worker {
    id: usize,
    thread: Option<thread::JoinHandle<()>>,
}
```

现在让我们依靠编译器来找到其他需要更改的地方。检查这段代码时，我们得到两个错误：

```bash
error[E0599]: no method named `join` found for enum `Option` in the current
scope
  --> src/lib.rs:52:27
   |
52 |             worker.thread.join().unwrap();
   |                           ^^^^ method not found in
`Option<JoinHandle<()>>`

error[E0308]: mismatched types
  --> src/lib.rs:72:22
   |
72 |         Worker { id, thread }
   |                      ^^^^^^ expected enum `Option`, found struct
`JoinHandle`
   |
   = note: expected enum `Option<JoinHandle<()>>`
            found struct `JoinHandle<_>`
help: try wrapping the expression in `Some`
   |
72 |         Worker { id, thread: Some(thread) }
   |                      +++++++++++++      +
```

让我们先解决第二个错误，它指向 `Worker::new` 末尾的代码；当我们创建一个新的 `Worker` 时，需要将 `thread` 值包装在 `Some` 中。进行以下更改以修复此错误：

文件名：`src/lib.rs`

```rust
impl Worker {
    fn new(
        id: usize,
        receiver: Arc<Mutex<mpsc::Receiver<Job>>>,
    ) -> Worker {
        --snip--

        Worker {
            id,
            thread: Some(thread),
        }
    }
}
```

第一个错误出现在我们的 `Drop` 实现中。我们之前提到过，我们打算在 `Option` 值上调用 `take` 以将 `thread` 从 `worker` 中移出。以下更改将实现这一点：

文件名：`src/lib.rs`

```rust
impl Drop for ThreadPool {
    fn drop(&mut self) {
        for worker in &mut self.workers {
            println!("Shutting down worker {}", worker.id);

          1 if let Some(thread) = worker.thread.take() {
              2 thread.join().unwrap();
            }
        }
    }
}
```

如第 17 章所述，`Option` 上的 `take` 方法会取出 `Some` 变体并在其位置留下 `None`。我们使用 `if let` 来解构 `Some` 并获取线程 \[1\]；然后我们在线程上调用 `join` \[2\]。如果一个 `Worker` 实例的线程已经是 `None`，我们知道该 `Worker` 的线程已经被清理，所以在这种情况下什么也不会发生。
