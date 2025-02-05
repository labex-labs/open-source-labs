# 使用 `join` 句柄等待所有线程完成

清单16-1中的代码不仅由于主线程结束而大多时候会过早地停止派生线程，而且因为无法保证线程的运行顺序，我们甚至不能保证派生线程会运行！

我们可以通过将 `thread::spawn` 的返回值保存在一个变量中来解决派生线程不运行或过早结束的问题。`thread::spawn` 的返回类型是 `JoinHandle<T>`。`JoinHandle<T>` 是一个拥有的值，当我们对其调用 `join` 方法时，它会等待其代表的线程完成。清单16-2展示了如何使用我们在清单16-1中创建的线程的 `JoinHandle<T>` 并调用 `join` 来确保派生线程在 `main` 退出之前完成。

文件名：`src/main.rs`

```rust
use std::thread;
use std::time::Duration;

fn main() {
    let handle = thread::spawn(|| {
        for i in 1..10 {
            println!("hi number {i} from the spawned thread!");
            thread::sleep(Duration::from_millis(1));
        }
    });

    for i in 1..5 {
        println!("hi number {i} from the main thread!");
        thread::sleep(Duration::from_millis(1));
    }

    handle.join().unwrap();
}
```

清单16-2：保存 `thread::spawn` 返回的 `JoinHandle<T>` 以确保线程运行完成

对句柄调用 `join` 会阻塞当前正在运行的线程，直到该句柄代表的线程终止。**阻塞**一个线程意味着阻止该线程执行工作或退出。因为我们将对 `join` 的调用放在了主线程的 `for` 循环之后，运行清单16-2应该会产生类似于以下的输出：

    hi number 1 from the main thread!
    hi number 2 from the main thread!
    hi number 1 from the spawned thread!
    hi number 3 from the main thread!
    hi number 2 from the spawned thread!
    hi number 4 from the main thread!
    hi number 3 from the spawned thread!
    hi number 4 from the spawned thread!
    hi number 5 from the spawned thread!
    hi number 6 from the spawned thread!
    hi number 7 from the spawned thread!
    hi number 8 from the spawned thread!
    hi number 9 from the spawned thread!

两个线程继续交替运行，但主线程由于调用了 `handle.join()` 而等待，直到派生线程完成才结束。

但是，让我们看看如果将 `handle.join()` 移到 `main` 函数中的 `for` 循环之前会发生什么，如下所示：

文件名：`src/main.rs`

```rust
use std::thread;
use std::time::Duration;

fn main() {
    let handle = thread::spawn(|| {
        for i in 1..10 {
            println!("hi number {i} from the spawned thread!");
            thread::sleep(Duration::from_millis(1));
        }
    });

    handle.join().unwrap();

    for i in 1..5 {
        println!("hi number {i} from the main thread!");
        thread::sleep(Duration::from_millis(1));
    }
}
```

主线程将等待派生线程完成，然后运行其 `for` 循环，因此输出将不再交错，如下所示：

    hi number 1 from the spawned thread!
    hi number 2 from the spawned thread!
    hi number 3 from the spawned thread!
    hi number 4 from the spawned thread!
    hi number 5 from the spawned thread!
    hi number 6 from the spawned thread!
    hi number 7 from the spawned thread!
    hi number 8 from the spawned thread!
    hi number 9 from the spawned thread!
    hi number 1 from the main thread!
    hi number 2 from the main thread!
    hi number 3 from the main thread!
    hi number 4 from the main thread!

像调用 `join` 的位置这样的小细节，可能会影响你的线程是否同时运行。
