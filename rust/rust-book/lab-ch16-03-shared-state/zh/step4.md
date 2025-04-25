# 在多个线程之间共享 Mutex`<T>`{=html}

现在让我们尝试使用 `Mutex<T>` 在多个线程之间共享一个值。我们将启动 10 个线程，让它们每个都将一个计数器值加 1，这样计数器就从 0 增加到 10。清单 16 - 13 中的示例会有一个编译错误，我们将利用这个错误来更多地了解使用 `Mutex<T>` 以及 Rust 如何帮助我们正确地使用它。

文件名：`src/main.rs`

```rust
use std::sync::Mutex;
use std::thread;

fn main() {
  1 let counter = Mutex::new(0);
    let mut handles = vec![];

  2 for _ in 0..10 {
      3 let handle = thread::spawn(move || {
          4 let mut num = counter.lock().unwrap();

          5 *num += 1;
        });
      6 handles.push(handle);
    }

    for handle in handles {
      7 handle.join().unwrap();
    }

  8 println!("Result: {}", *counter.lock().unwrap());
}
```

清单 16 - 13:10 个线程，每个线程都对由 `Mutex<T>` 保护的计数器加 1

和在清单 16 - 12 中一样，我们创建一个 `counter` 变量来在 `Mutex<T>` 中保存一个 `i32`\[1\]。接下来，我们通过遍历一个数字范围来创建 10 个线程\[2\]。我们使用 `thread::spawn` 并给所有线程相同的闭包：一个将计数器移动到线程中的闭包\[3\]，通过调用 `lock` 方法获取 `Mutex<T>` 上的锁\[4\]，然后将互斥锁中的值加 1\[5\]。当一个线程完成运行其闭包时，`num` 将超出作用域并释放锁，以便另一个线程可以获取它。

在主线程中，我们收集所有的连接句柄\[6\]。然后，就像在清单 16 - 2 中一样，我们对每个句柄调用 `join` 以确保所有线程都完成\[7\]。在那个时候，主线程将获取锁并打印这个程序的结果\[8\]。

我们暗示过这个示例不会编译。现在让我们找出原因！

```bash
error[E0382]: use of moved value: `counter`
  --> src/main.rs:9:36
   |
5  |     let counter = Mutex::new(0);
   |         ------- move occurs because `counter` has type `Mutex<i32>`, which
does not implement the `Copy` trait
...
9  |         let handle = thread::spawn(move || {
   |                                    ^^^^^^^ value moved into closure here,
in previous iteration of loop
10 |             let mut num = counter.lock().unwrap();
   |                           ------- use occurs due to use in closure
```

错误信息指出 `counter` 值在循环的上一次迭代中被移动了。Rust 告诉我们不能将锁 `counter` 的所有权移动到多个线程中。让我们使用第 15 章中讨论的多重所有权方法来修复编译错误。
