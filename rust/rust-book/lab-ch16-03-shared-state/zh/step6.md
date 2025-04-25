# 使用 Arc`<T>` 进行原子引用计数{=html}

幸运的是，`Arc<T>` 是一种类似于 `Rc<T>` 的类型，在并发情况下使用是安全的。这里的“a”代表“atomic”（原子的），意思是它是一种“原子引用计数”类型。原子类型是另一种并发原语，我们在这里不会详细介绍：有关更多详细信息，请参阅 `std::sync::atomic` 的标准库文档。此时，你只需要知道原子类型的工作方式类似于基本类型，但在线程间共享是安全的。

然后你可能会想，为什么所有基本类型都不是原子的，以及为什么标准库类型默认不实现为使用 `Arc<T>`。原因是线程安全会带来性能开销，只有在真正需要时才值得付出这个代价。如果你只是在单个线程内对值执行操作，那么如果不必强制执行原子类型提供的保证，你的代码可以运行得更快。

让我们回到我们的示例：`Arc<T>` 和 `Rc<T>` 具有相同的 API，所以我们通过更改 `use` 行、对 `new` 的调用以及对 `clone` 的调用，来修复我们的程序。清单 16 - 15 中的代码最终将编译并运行。

文件名：`src/main.rs`

```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    let counter = Arc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..10 {
        let counter = Arc::clone(&counter);
        let handle = thread::spawn(move || {
            let mut num = counter.lock().unwrap();

            *num += 1;
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("Result: {}", *counter.lock().unwrap());
}
```

清单 16 - 15：使用 `Arc<T>` 包装 `Mutex<T>` 以便能够在多个线程之间共享所有权

这段代码将输出以下内容：

```rust
Result: 10
```

我们做到了！我们从 0 数到了 10，这可能看起来不是很了不起，但它确实让我们对 `Mutex<T>` 和线程安全有了很多了解。你也可以使用这个程序的结构来执行比仅仅增加计数器更复杂的操作。使用这种策略，你可以将一个计算分成独立的部分，在线程间拆分这些部分，然后使用 `Mutex<T>` 让每个线程用其部分更新最终结果。

请注意，如果你正在进行简单的数值操作，标准库的 `std::sync::atomic` 模块提供了比 `Mutex<T>` 类型更简单的类型。这些类型提供对基本类型的安全、并发、原子访问。我们在这个示例中选择将 `Mutex<T>` 与基本类型一起使用，以便我们可以专注于 `Mutex<T>` 的工作方式。
