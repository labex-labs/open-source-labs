# 通过通道向线程发送请求

我们接下来要解决的问题是，传递给`thread::spawn`的闭包什么都不做。目前，我们在`execute`方法中得到了想要执行的闭包。但是我们需要在创建线程池期间创建每个`Worker`时，给`thread::spawn`一个要运行的闭包。

我们希望刚刚创建的`Worker`结构体从线程池中持有的队列中获取要运行的代码，并将该代码发送到其线程中运行。

我们在第16章中学到的通道——一种在两个线程之间进行通信的简单方式——非常适合这个用例。我们将使用一个通道作为任务队列，并且`execute`将从线程池向`Worker`实例发送一个任务，`Worker`实例再将任务发送到其线程。具体计划如下：

1. 线程池将创建一个通道并持有发送端。
2. 每个`Worker`将持有接收端。
3. 我们将创建一个新的`Job`结构体，用于持有我们想要通过通道发送的闭包。
4. `execute`方法将通过发送端发送它想要执行的任务。
5. 在其线程中，`Worker`将遍历其接收端并执行它接收到的任何任务的闭包。

让我们首先在`ThreadPool::new`中创建一个通道，并将发送端保存在`ThreadPool`实例中，如清单20-16所示。目前`Job`结构体不持有任何内容，但它将是我们通过通道发送的项的类型。

文件名：`src/lib.rs`

```rust
use std::{sync::mpsc, thread};

pub struct ThreadPool {
    workers: Vec<Worker>,
    sender: mpsc::Sender<Job>,
}

struct Job;

impl ThreadPool {
    --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

      1 let (sender, receiver) = mpsc::channel();

        let mut workers = Vec::with_capacity(size);

        for id in 0..size {
            workers.push(Worker::new(id));
        }

        ThreadPool { workers, 2 sender }
    }
    --snip--
}
```

清单20-16：修改`ThreadPool`以存储用于传输`Job`实例的通道的发送端

在`ThreadPool::new`中，我们创建了新的通道\[1\]，并让线程池持有发送端\[2\]。这将成功编译。

让我们尝试在线程池创建通道时，将通道的接收端传递给每个`Worker`。我们知道我们希望在`Worker`实例创建的线程中使用接收端，所以我们将在闭包中引用`receiver`参数。清单20-17中的代码还不能完全编译通过。

文件名：`src/lib.rs`

```rust
impl ThreadPool {
    --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

        let (sender, receiver) = mpsc::channel();

        let mut workers = Vec::with_capacity(size);

        for id in 0..size {
          1 workers.push(Worker::new(id, receiver));
        }

        ThreadPool { workers, sender }
    }
    --snip--
}

--snip--

impl Worker {
    fn new(id: usize, receiver: mpsc::Receiver<Job>) -> Worker {
        let thread = thread::spawn(|| {
          2 receiver;
        });

        Worker { id, thread }
    }
}
```

清单20-17：将接收端传递给每个`Worker`

我们做了一些小而直接的更改：我们将接收端传递给`Worker::new`\[1\]，然后在闭包中使用它\[2\]。

当我们尝试检查这段代码时，会得到以下错误：

```bash
$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
error[E0382]: use of moved value: `receiver`
  --> src/lib.rs:26:42
   |
21 |         let (sender, receiver) = mpsc::channel();
   |                      -------- move occurs because `receiver` has type
`std::sync::mpsc::Receiver<Job>`, which does not implement the `Copy` trait
...
26 |             workers.push(Worker::new(id, receiver));
   |                                          ^^^^^^^^ value moved here, in
previous iteration of loop
```

代码试图将`receiver`传递给多个`Worker`实例。这行不通，正如你从第16章中回忆的那样：Rust提供的通道实现是多个*生产者*，单个*消费者*。这意味着我们不能仅仅克隆通道的消费端来修复这段代码。我们也不希望向多个消费者多次发送消息；我们希望有一个包含多个`Worker`实例的消息列表，这样每个消息只被处理一次。

此外，从通道队列中取出一个任务涉及到对`receiver`进行变异，所以线程需要一种安全的方式来共享和修改`receiver`；否则，我们可能会遇到竞争条件（如第16章所述）。

回忆一下第16章中讨论的线程安全智能指针：为了在多个线程之间共享所有权并允许线程变异值，我们需要使用`Arc<Mutex<T>>`。`Arc`类型将允许多个`Worker`实例拥有接收端，而`Mutex`将确保一次只有一个`Worker`从接收端获取任务。清单20-18展示了我们需要做的更改。

文件名：`src/lib.rs`

```rust
use std::{
    sync::{mpsc, Arc, Mutex},
    thread,
};
--snip--

impl ThreadPool {
    --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

        let (sender, receiver) = mpsc::channel();

      1 let receiver = Arc::new(Mutex::new(receiver));

        let mut workers = Vec::with_capacity(size);

        for id in 0..size {
            workers.push(
                Worker::new(id, Arc::clone(& 2 receiver))
            );
        }

        ThreadPool { workers, sender }
    }

    --snip--
}

--snip--

impl Worker {
    fn new(
        id: usize,
        receiver: Arc<Mutex<mpsc::Receiver<Job>>>,
    ) -> Worker {
        --snip--
    }
}
```

清单20-18：使用`Arc`和`Mutex`在`Worker`实例之间共享接收端

在`ThreadPool::new`中，我们将接收端放入`Arc`和`Mutex`中\[1\]。对于每个新的`Worker`，我们克隆`Arc`以增加引用计数，这样`Worker`实例就可以共享接收端的所有权\[2\]。

通过这些更改，代码编译通过了！我们正在逐步实现目标！
