# 向线程发送信号以停止监听任务

经过我们所做的所有更改，代码可以编译通过且没有任何警告。然而，坏消息是这段代码目前的运行方式并非我们期望的那样。关键在于 `Worker` 实例的线程所运行的闭包中的逻辑：目前，我们调用了 `join`，但这并不会关闭线程，因为它们会永远在 `loop` 中寻找任务。如果我们尝试使用当前的 `drop` 实现来丢弃我们的 `ThreadPool`，主线程将会永远阻塞，等待第一个线程完成。

为了解决这个问题，我们需要对 `ThreadPool` 的 `drop` 实现进行更改，然后再更改 `Worker` 中的循环。

首先，我们将更改 `ThreadPool` 的 `drop` 实现，以便在等待线程完成之前显式地丢弃 `sender`。清单20-23展示了对 `ThreadPool` 进行的更改，以显式地丢弃 `sender`。我们使用与处理线程时相同的 `Option` 和 `take` 技术，以便能够将 `sender` 从 `ThreadPool` 中移出。

文件名：`src/lib.rs`

```rust
pub struct ThreadPool {
    workers: Vec<Worker>,
    sender: Option<mpsc::Sender<Job>>,
}
--snip--
impl ThreadPool {
    pub fn new(size: usize) -> ThreadPool {
        --snip--

        ThreadPool {
            workers,
            sender: Some(sender),
        }
    }

    pub fn execute<F>(&self, f: F)
    where
        F: FnOnce() + Send + 'static,
    {
        let job = Box::new(f);

        self.sender
           .as_ref()
           .unwrap()
           .send(job)
           .unwrap();
    }
}

impl Drop for ThreadPool {
    fn drop(&mut self) {
      1 drop(self.sender.take());

        for worker in &mut self.workers {
            println!("Shutting down worker {}", worker.id);

            if let Some(thread) = worker.thread.take() {
                thread.join().unwrap();
            }
        }
    }
}
```

清单20-23：在加入 `Worker` 线程之前显式丢弃 `sender`

丢弃 `sender` \[1\] 会关闭通道，这表明不会再发送更多消息。当这种情况发生时，`Worker` 实例在无限循环中对 `recv` 的所有调用都将返回一个错误。在清单20-24中，我们更改了 `Worker` 中的循环，以便在这种情况下优雅地退出循环，这意味着当 `ThreadPool` 的 `drop` 实现对它们调用 `join` 时，线程将会完成。

文件名：`src/lib.rs`

```rust
impl Worker {
    fn new(
        id: usize,
        receiver: Arc<Mutex<mpsc::Receiver<Job>>>,
    ) -> Worker {
        let thread = thread::spawn(move || loop {
            let message = receiver.lock().unwrap().recv();

            match message {
                Ok(job) => {
                    println!(
                        "Worker {id} got a job; executing."
                    );

                    job();
                }
                Err(_) => {
                    println!(
                        "Worker {id} shutting down."
                    );
                    break;
                }
            }
        });

        Worker {
            id,
            thread: Some(thread),
        }
    }
}
```

清单20-24：当 `recv` 返回错误时显式跳出循环

为了看到这段代码的实际运行情况，让我们修改 `main` 函数，使其在优雅地关闭服务器之前只接受两个请求，如清单20-25所示。

文件名：`src/main.rs`

```rust
fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();
    let pool = ThreadPool::new(4);

    for stream in listener.incoming().take(2) {
        let stream = stream.unwrap();

        pool.execute(|| {
            handle_connection(stream);
        });
    }

    println!("Shutting down.");
}
```

清单20-25：通过退出循环在处理两个请求后关闭服务器

在实际的Web服务器中，你肯定不希望它只处理两个请求就关闭。这段代码只是为了演示优雅关闭和清理功能是否正常工作。

`take` 方法是在 `Iterator` 特性中定义的，它最多将迭代限制为前两个项。`ThreadPool` 将在 `main` 函数结束时超出作用域，然后 `drop` 实现将会运行。

使用 `cargo run` 启动服务器，并发送三个请求。第三个请求应该会出错，在你的终端中你应该会看到类似这样的输出：

```bash
$ cargo run
   Compiling hello v0.1.0 (file:///projects/hello)
    Finished dev [unoptimized + debuginfo] target(s) in 1.0s
     Running `target/debug/hello`
Worker 0 got a job; executing.
Shutting down.
Shutting down worker 0
Worker 3 got a job; executing.
Worker 1 disconnected; shutting down.
Worker 2 disconnected; shutting down.
Worker 3 disconnected; shutting down.
Worker 0 disconnected; shutting down.
Shutting down worker 1
Shutting down worker 2
Shutting down worker 3
```

你可能会看到不同的 `Worker` ID 和打印消息的顺序。从这些消息中我们可以看出这段代码的工作方式：`Worker` 实例0和3收到了前两个请求。在第二个连接之后，服务器停止接受连接，并且 `ThreadPool` 上的 `Drop` 实现甚至在 `Worker` 3开始其任务之前就开始执行。丢弃 `sender` 会断开所有 `Worker` 实例的连接，并告诉它们关闭。每个 `Worker` 实例在断开连接时都会打印一条消息，然后线程池调用 `join` 来等待每个 `Worker` 线程完成。

注意这个特定执行过程中的一个有趣方面：`ThreadPool` 丢弃了 `sender`，并且在任何 `Worker` 收到错误之前，我们尝试加入 `Worker` 0。`Worker` 0还没有从 `recv` 收到错误，所以主线程阻塞，等待 `Worker` 0完成。与此同时，`Worker` 3收到了一个任务，然后所有线程都收到了一个错误。当 `Worker` 0完成时，主线程等待其余的 `Worker` 实例完成。此时，它们都已经退出了循环并停止了。

恭喜！我们现在已经完成了我们的项目；我们有一个基本的Web服务器，它使用线程池来异步响应。我们能够对服务器进行优雅关闭，这会清理线程池中的所有线程。请访问 *https://www.nostarch.com/Rust2021* 下载本章的完整代码以供参考。

我们还可以做更多的事情！如果你想继续改进这个项目，这里有一些想法：

- 为 `ThreadPool` 及其公共方法添加更多文档。
- 添加对库功能的测试。
- 将对 `unwrap` 的调用更改为更健壮的错误处理。
- 使用 `ThreadPool` 来执行除服务Web请求之外的其他任务。
- 在 *https://crates.io* 上找到一个线程池 crate，并使用该 crate 实现一个类似的Web服务器。然后将其API和健壮性与我们实现的线程池进行比较。
