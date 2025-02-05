# 从线程池向线程发送代码

我们在清单20-14的`for`循环中留下了一条关于创建线程的注释。在这里，我们将看看如何实际创建线程。标准库提供了`thread::spawn`作为创建线程的一种方式，并且`thread::spawn`期望在创建线程时立即获得线程应该运行的一些代码。然而，在我们的例子中，我们想要创建线程并让它们*等待*我们稍后发送的代码。标准库中线程的实现没有包含任何这样做的方法；我们必须手动实现它。

我们将通过在线程池和线程之间引入一个新的数据结构来管理这种新行为，从而实现这种行为。我们将把这个数据结构称为*工作线程（Worker）*，这在池化实现中是一个常用术语。工作线程获取需要运行的代码并在其线程中运行该代码。

想象一下在餐厅厨房工作的人：工人们等待顾客下单，然后他们负责接收这些订单并完成它们。

我们将在线程池中存储`Worker`结构体的实例，而不是存储`JoinHandle<()>`实例的向量。每个工作线程将存储一个`JoinHandle<()>`实例。然后我们将在`Worker`上实现一个方法，该方法将接受要运行的代码闭包并将其发送到已经在运行的线程进行执行。我们还将为每个工作线程赋予一个`id`，以便在日志记录或调试时我们可以区分线程池中的不同工作线程实例。

以下是创建线程池时将发生的新过程。在我们以这种方式设置好工作线程之后，我们将实现将闭包发送到线程的代码：

1. 定义一个持有`id`和`JoinHandle<()>`的`Worker`结构体。
2. 更改`ThreadPool`以持有`Worker`实例的向量。
3. 定义一个`Worker::new`函数，该函数接受一个`id`编号并返回一个持有该`id`和使用空闭包创建的线程的`Worker`实例。
4. 在`ThreadPool::new`中，使用`for`循环计数器生成一个`id`，使用该`id`创建一个新的工作线程，并将该工作线程存储在向量中。

如果你愿意接受挑战，可以在查看清单20-15中的代码之前自己尝试实现这些更改。

准备好了吗？以下是清单20-15，其中展示了进行上述修改的一种方法。

文件名：`src/lib.rs`

```rust
use std::thread;

pub struct ThreadPool {
  1 workers: Vec<Worker>,
}

impl ThreadPool {
    --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

        let mut workers = Vec::with_capacity(size);

      2 for id in 0..size {
          3 workers.push(Worker::new(id));
        }

        ThreadPool { workers }
    }
    --snip--
}

4 struct Worker {
    id: usize,
    thread: thread::JoinHandle<()>,
}

impl Worker {
  5 fn new(id: usize) -> Worker {
      6 let thread = thread::spawn(|| {});

        Worker { 7 id, 8 thread }
    }
}
```

清单20-15：修改`ThreadPool`以持有`Worker`实例而不是直接持有线程

我们将`ThreadPool`上的字段名称从`threads`改为`workers`，因为现在它持有`Worker`实例而不是`JoinHandle<()>`实例\[1\]。我们在`for`循环中使用计数器\[2\]作为参数传递给`Worker::new`，并将每个新的工作线程存储在名为`workers`的向量中\[3\]。

外部代码（比如我们在`src/main.rs`中的服务器）不需要知道在线程池中使用`Worker`结构体的实现细节，所以我们将`Worker`结构体\[4\]及其`new`函数\[5\]设为私有。`Worker::new`函数使用我们给它的`id`\[7\]，并存储一个通过使用空闭包创建新线程而得到的`JoinHandle<()>`实例\[8\]，该闭包为\[6\]。

> 注意：如果操作系统因为没有足够的系统资源而无法创建线程，`thread::spawn`将会恐慌。这将导致我们整个服务器恐慌，即使某些线程的创建可能会成功。为了简单起见，这种行为是可以的，但在生产环境中的线程池实现中，你可能希望使用`std::thread::Builder`及其返回`Result`的`spawn`方法。

这段代码将编译通过，并将存储我们作为参数传递给`ThreadPool::new`的工作线程实例的数量。但我们*仍然*没有处理在`execute`中得到的闭包。接下来让我们看看如何处理它。
