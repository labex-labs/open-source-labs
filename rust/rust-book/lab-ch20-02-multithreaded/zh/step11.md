# 实现 `execute` 方法

现在让我们最终在 `ThreadPool` 上实现 `execute` 方法。我们还将把 `Job` 从一个结构体改为一个类型别名，用于表示持有 `execute` 接收的闭包类型的 trait 对象。正如在“使用类型别名创建类型同义词”中所讨论的，类型别名使我们能够将长类型缩短，以便于使用。请看清单20-19。

文件名：`src/lib.rs`

```rust
--snip--

type Job = Box<dyn FnOnce() + Send + 'static>;

impl ThreadPool {
    --snip--

    pub fn execute<F>(&self, f: F)
    where
        F: FnOnce() + Send + 'static,
    {
      1 let job = Box::new(f);

      2 self.sender.send(job).unwrap();
    }
}

--snip--
```

清单20-19：为持有每个闭包的 `Box` 创建一个 `Job` 类型别名，然后通过通道发送任务

在使用 `execute` 中得到的闭包创建一个新的 `Job` 实例之后\[1\]，我们将该任务通过通道的发送端发送出去\[2\]。对于 `send` 操作，我们调用 `unwrap` 来处理发送失败的情况。例如，如果我们停止所有线程的执行，这意味着接收端已经停止接收新消息，那么发送就可能会失败。目前，我们无法停止线程的执行：只要线程池存在，我们的线程就会继续执行。我们使用 `unwrap` 的原因是我们知道失败情况不会发生，但编译器并不知道这一点。

但我们还没有完全完成！在 `Worker` 中，传递给 `thread::spawn` 的闭包仍然只是*引用*通道的接收端。相反，我们需要闭包永远循环，向通道的接收端请求任务，并在收到任务时运行它。让我们对 `Worker::new` 进行清单20-20所示的更改。

文件名：`src/lib.rs`

```rust
--snip--

impl Worker {
    fn new(
        id: usize,
        receiver: Arc<Mutex<mpsc::Receiver<Job>>>,
    ) -> Worker {
        let thread = thread::spawn(move || loop {
            let job = receiver
              1.lock()
              2.unwrap()
              3.recv()
              4.unwrap();

            println!("Worker {id} got a job; executing.");

            job();
        });

        Worker { id, thread }
    }
}
```

清单20-20：在 `Worker` 实例的线程中接收并执行任务

在这里，我们首先对 `receiver` 调用 `lock` 来获取互斥锁\[1\]，然后调用 `unwrap` 以在出现任何错误时使程序恐慌\[2\]。如果互斥锁处于*中毒*状态，获取锁可能会失败，当其他线程在持有锁时恐慌而不是释放锁时，就会发生这种情况。在这种情况下，调用 `unwrap` 使这个线程恐慌是正确的操作。你可以随意将这个 `unwrap` 改为带有对你有意义的错误消息的 `expect`。

如果我们获得了互斥锁，我们调用 `recv` 从通道接收一个 `Job`\[3\]。最后一个 `unwrap` 也会处理这里可能出现的任何错误\[4\]，如果持有发送端的线程已经关闭，就可能会出现错误，类似于如果接收端关闭，`send` 方法会返回 `Err` 的情况。

对 `recv` 的调用会阻塞，所以如果还没有任务，当前线程将等待，直到有任务可用。`Mutex<T>` 确保一次只有一个 `Worker` 线程试图请求任务。

我们的线程池现在处于工作状态！运行 `cargo run` 并进行一些请求：

```bash

```

成功！我们现在有了一个可以异步执行连接的线程池。创建的线程永远不会超过四个，所以如果服务器收到大量请求，我们的系统不会过载。如果我们向 _/sleep_ 发出请求，服务器将能够通过让另一个线程运行其他请求来处理它们。

> 注意：如果你同时在多个浏览器窗口中打开 _/sleep_，它们可能会以五秒的间隔依次加载。由于缓存原因，一些网页浏览器会顺序执行同一请求的多个实例。这个限制不是由我们的Web服务器造成的。

在学习了第18章中的 `while let` 循环之后，你可能想知道为什么我们没有像清单20-21那样编写 `Worker` 线程代码。

文件名：`src/lib.rs`

```rust
--snip--

impl Worker {
    fn new(
        id: usize,
        receiver: Arc<Mutex<mpsc::Receiver<Job>>>,
    ) -> Worker {
        let thread = thread::spawn(move || {
            while let Ok(job) = receiver.lock().unwrap().recv() {
                println!("Worker {id} got a job; executing.");

                job();
            }
        });

        Worker { id, thread }
    }
}
```

清单20-21：使用 `while let` 的 `Worker::new` 的替代实现

这段代码可以编译并运行，但不会产生期望的线程行为：一个缓慢的请求仍然会导致其他请求等待处理。原因有点微妙：`Mutex` 结构体没有公共的 `unlock` 方法，因为锁的所有权基于 `lock` 方法返回的 `LockResult<MutexGuard<T>>` 中的 `MutexGuard<T>` 的生命周期。在编译时，借用检查器可以强制执行这样的规则：除非我们持有锁，否则不能访问由 `Mutex` 保护的资源。然而，如果我们不注意 `MutexGuard<T>` 的生命周期，这种实现也可能导致锁被持有比预期更长的时间。

清单20-20中使用 `let job = receiver.lock().unwrap().recv().unwrap();` 的代码之所以有效，是因为使用 `let` 时，等号右侧表达式中使用的任何临时值在 `let` 语句结束时会立即被丢弃。但是，`while let`（以及 `if let` 和 `match`）直到相关块结束才会丢弃临时值。在清单20-21中，锁在调用 `job()` 的整个过程中都被持有，这意味着其他 `Worker` 实例无法接收任务。
