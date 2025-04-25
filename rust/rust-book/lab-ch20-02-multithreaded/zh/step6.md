# 使用编译器驱动开发构建线程池

按照清单 20-12 对`src/main.rs`进行更改，然后让我们利用`cargo check`产生的编译器错误来推动我们的开发。这是我们得到的第一个错误：

```bash
$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
error[E0433]: failed to resolve: use of undeclared type `ThreadPool`
  --> src/main.rs:11:16
   |
11 |     let pool = ThreadPool::new(4);
   |                ^^^^^^^^^^ use of undeclared type `ThreadPool`
```

太棒了！这个错误告诉我们需要一个`ThreadPool`类型或模块，所以我们现在就来构建一个。我们对`ThreadPool`的实现将独立于我们的 Web 服务器所做的工作类型。所以让我们把`hello` crate 从一个二进制 crate 切换为一个库 crate，来存放我们对`ThreadPool`的实现。在我们切换到库 crate 之后，我们也可以将这个单独的线程池库用于任何我们想使用线程池来做的工作，而不仅仅是用于提供 Web 请求服务。

创建一个`src/lib.rs`文件，其中包含以下内容，这是我们目前能有的`ThreadPool`结构体的最简单定义：

文件名：`src/lib.rs`

```rust
pub struct ThreadPool;
```

然后编辑`main.rs`文件，通过在`src/main.rs`的顶部添加以下代码，将`ThreadPool`从库 crate 引入作用域：

文件名：`src/main.rs`

```rust
use hello::ThreadPool;
```

这段代码仍然无法工作，但让我们再次检查它，以得到下一个我们需要解决的错误：

```bash
$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
error[E0599]: no function or associated item named `new` found for struct
`ThreadPool` in the current scope
  --> src/main.rs:12:28
   |
12 |     let pool = ThreadPool::new(4);
   |                            ^^^ function or associated item not found in
`ThreadPool`
```

这个错误表明接下来我们需要为`ThreadPool`创建一个名为`new`的关联函数。我们也知道`new`需要有一个能接受`4`作为参数的参数，并且应该返回一个`ThreadPool`实例。让我们实现一个具有这些特性的最简单的`new`函数：

文件名：`src/lib.rs`

```rust
pub struct ThreadPool;

impl ThreadPool {
    pub fn new(size: usize) -> ThreadPool {
        ThreadPool
    }
}
```

我们选择`usize`作为`size`参数的类型，因为我们知道负数个线程是没有意义的。我们也知道我们会将这个`4`用作线程集合中的元素数量，正如在“整数类型”中所讨论的，这就是`usize`类型的用途。

让我们再次检查代码：

```bash
$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
error[E0599]: no method named `execute` found for struct `ThreadPool` in the
current scope
  --> src/main.rs:17:14
   |
17 |         pool.execute(|| {
   |              ^^^^^^^ method not found in `ThreadPool`
```

现在出现错误是因为我们在`ThreadPool`上没有`execute`方法。回想一下“创建有限数量的线程”，我们决定我们的线程池应该有一个类似于`thread::spawn`的接口。此外，我们将实现`execute`函数，使其接受给定的闭包，并将其交给线程池中的一个空闲线程来运行。

我们将在`ThreadPool`上定义`execute`方法，使其接受一个闭包作为参数。回想一下“将捕获的值移出闭包和 Fn 特质”，我们可以使用三种不同的特质将闭包作为参数：`Fn`、`FnMut`和`FnOnce`。我们需要决定在这里使用哪种类型的闭包。我们知道我们最终会做一些类似于标准库`thread::spawn`实现的事情，所以我们可以看看`thread::spawn`的签名对其参数有哪些约束。文档向我们展示了以下内容：

```rust
pub fn spawn<F, T>(f: F) -> JoinHandle<T>
    where
        F: FnOnce() -> T,
        F: Send + 'static,
        T: Send + 'static,
```

这里我们关心的是`F`类型参数；`T`类型参数与返回值有关，我们不关心那个。我们可以看到`spawn`使用`FnOnce`作为对`F`的特质约束。这可能也是我们想要的，因为我们最终会将在`execute`中得到的参数传递给`spawn`。我们可以更确定`FnOnce`是我们想要使用的特质，因为运行请求的线程只会执行该请求的闭包一次，这与`FnOnce`中的`Once`相匹配。

`F`类型参数还有特质约束`Send`和生命周期约束`'static`，这在我们的情况下很有用：我们需要`Send`来将闭包从一个线程转移到另一个线程，并且需要`'static`，因为我们不知道线程执行需要多长时间。让我们在`ThreadPool`上创建一个`execute`方法，它将接受一个具有这些约束的泛型参数`F`：

文件名：`src/lib.rs`

```rust
impl ThreadPool {
    --snip--
    pub fn execute<F>(&self, f: F)
    where
        F: FnOnce() 1 + Send + 'static,
    {
    }
}
```

我们仍然在`FnOnce`之后使用`()`\[1\]，因为这个`FnOnce`表示一个不接受参数并返回单元类型`()`的闭包。就像函数定义一样，签名中可以省略返回类型，但即使我们没有参数，我们仍然需要括号。

同样，这是`execute`方法的最简单实现：它什么都不做，但我们只是试图让我们的代码编译通过。让我们再次检查它：

```bash
$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
    Finished dev [unoptimized + debuginfo] target(s) in 0.24s
```

它编译通过了！但请注意，如果你尝试`cargo run`并在浏览器中发出请求，你会在浏览器中看到我们在本章开头看到的错误。我们的库实际上还没有调用传递给`execute`的闭包！

> 注意：你可能会听到关于像 Haskell 和 Rust 这样具有严格编译器的语言的一种说法，即“如果代码编译通过，它就可以工作”。但这种说法并不总是正确的。我们的项目编译通过了，但它实际上什么都没做！如果我们正在构建一个真实、完整的项目，这将是一个开始编写单元测试的好时机，以检查代码是否编译通过 _并且_ 具有我们想要的行为。
