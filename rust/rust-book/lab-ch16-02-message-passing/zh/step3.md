# 发送多个值并观察接收者的等待状态

清单 16 - 8 中的代码能够编译并运行，但它并没有清晰地向我们展示两个独立的线程是如何通过通道进行通信的。在清单 16 - 10 中，我们做了一些修改，以证明清单 16 - 8 中的代码是在并发运行：新创建的线程现在将发送多个消息，并且在每条消息之间暂停一秒。

文件名：`src/main.rs`

```rust
use std::sync::mpsc;
use std::thread;
use std::time::Duration;

fn main() {
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        let vals = vec![
            String::from("hi"),
            String::from("from"),
            String::from("the"),
            String::from("thread"),
        ];

        for val in vals {
            tx.send(val).unwrap();
            thread::sleep(Duration::from_secs(1));
        }
    });

    for received in rx {
        println!("Got: {received}");
    }
}
```

清单 16 - 10：发送多个消息并在每条消息之间暂停

这一次，新创建的线程有一个字符串向量，我们想要将其发送到主线程。我们遍历这些字符串，逐个发送它们，并通过调用 `thread::sleep` 函数，传入一秒的 `Duration` 值，在每条消息之间暂停。

在主线程中，我们不再显式调用 `recv` 函数：相反，我们将 `rx` 当作一个迭代器来处理。对于接收到的每个值，我们都将其打印出来。当通道关闭时，迭代将会结束。

当运行清单 16 - 10 中的代码时，你应该会看到以下输出，并且每行之间会有一秒的停顿：

    Got: hi
    Got: from
    Got: the
    Got: thread

由于在主线程的 `for` 循环中我们没有任何暂停或延迟的代码，所以我们可以判断主线程正在等待从新创建的线程接收值。
