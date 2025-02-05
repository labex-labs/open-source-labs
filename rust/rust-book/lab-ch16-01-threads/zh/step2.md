# 使用 `spawn` 创建新线程

要创建一个新线程，我们调用 `thread::spawn` 函数，并向其传递一个闭包（我们在第13章讨论过闭包），该闭包包含我们想要在新线程中运行的代码。清单16-1中的示例在主线程中打印一些文本，并在新线程中打印其他文本。

文件名：`src/main.rs`

```rust
use std::thread;
use std::time::Duration;

fn main() {
    thread::spawn(|| {
        for i in 1..10 {
            println!("hi number {i} from the spawned thread!");
            thread::sleep(Duration::from_millis(1));
        }
    });

    for i in 1..5 {
        println!("hi number {i} from the main thread!");
        thread::sleep(Duration::from_millis(1));
    }
}
```

清单16-1：创建一个新线程来打印一些内容，同时主线程打印其他内容

请注意，当Rust程序的主线程完成时，所有派生的线程都会被关闭，无论它们是否已经完成运行。每次运行此程序的输出可能会略有不同，但它看起来会类似于以下内容：

    hi number 1 from the main thread!
    hi number 1 from the spawned thread!
    hi number 2 from the main thread!
    hi number 2 from the spawned thread!
    hi number 3 from the main thread!
    hi number 3 from the spawned thread!
    hi number 4 from the main thread!
    hi number 4 from the spawned thread!
    hi number 5 from the spawned thread!

对 `thread::sleep` 的调用会强制一个线程在短时间内停止执行，从而允许另一个线程运行。线程可能会轮流执行，但这并不能保证：这取决于你的操作系统如何调度线程。在这次运行中，主线程先打印，尽管派生线程中的打印语句在代码中排在前面。而且，即使我们告诉派生线程打印到 `i` 为9，在主线程关闭之前它只打印到了5。

如果你运行这段代码，只看到了主线程的输出，或者没有看到任何重叠的输出，可以尝试增加范围中的数字，以便为操作系统提供更多在不同线程之间切换的机会。
