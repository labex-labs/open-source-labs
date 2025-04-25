# 创建用于存储线程的空间

既然我们已经有了一种方法来确定我们有有效的线程数量可以存储在池中，那么我们可以创建这些线程，并在返回结构体之前将它们存储在`ThreadPool`结构体中。但是我们如何“存储”一个线程呢？让我们再看一下`thread::spawn`的签名：

```rust
pub fn spawn<F, T>(f: F) -> JoinHandle<T>
    where
        F: FnOnce() -> T,
        F: Send + 'static,
        T: Send + 'static,
```

`spawn`函数返回一个`JoinHandle<T>`，其中`T`是闭包返回的类型。让我们也尝试使用`JoinHandle`，看看会发生什么。在我们的例子中，我们传递给线程池的闭包将处理连接并且不返回任何东西，所以`T`将是单元类型`()`。

清单 20-14 中的代码将编译通过，但还没有创建任何线程。我们已经更改了`ThreadPool`的定义，使其持有一个`thread::JoinHandle<()>`实例的向量，用容量为`size`初始化该向量，设置了一个`for`循环，该循环将运行一些代码来创建线程，并返回一个包含这些线程的`ThreadPool`实例。

文件名：`src/lib.rs`

```rust
1 use std::thread;

pub struct ThreadPool {
  2 threads: Vec<thread::JoinHandle<()>>,
}

impl ThreadPool {
    --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

      3 let mut threads = Vec::with_capacity(size);

        for _ in 0..size {
            // 创建一些线程并将它们存储在向量中
        }

        ThreadPool { threads }
    }
    --snip--
}
```

清单 20-14：为`ThreadPool`创建一个向量来存储线程

我们已经在库 crate 中引入了`std::thread`到作用域\[1\]，因为我们在`ThreadPool`中使用`thread::JoinHandle`作为向量中元素的类型\[2\]。

一旦接收到有效的大小，我们的`ThreadPool`会创建一个新的向量，该向量可以容纳`size`个元素\[3\]。`with_capacity`函数执行与`Vec::new`相同的任务，但有一个重要的区别：它预先在向量中分配空间。因为我们知道我们需要在向量中存储`size`个元素，所以预先进行这种分配比使用`Vec::new`稍微高效一些，`Vec::new`会在插入元素时自行调整大小。

当你再次运行`cargo check`时，它应该会成功。
