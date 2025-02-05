# 通过克隆发送端创建多个生产者

之前我们提到过 `mpsc` 是「多个生产者，单个消费者」的首字母缩写。现在让我们使用 `mpsc` 并扩展清单 16 - 10 中的代码，来创建多个线程，这些线程都向同一个接收端发送值。我们可以通过克隆发送端来实现这一点，如清单 16 - 11 所示。

文件名：`src/main.rs`

```rust
--snip--

let (tx, rx) = mpsc::channel();

let tx1 = tx.clone();
thread::spawn(move || {
    let vals = vec![
        String::from("hi"),
        String::from("from"),
        String::from("the"),
        String::from("thread"),
    ];

    for val in vals {
        tx1.send(val).unwrap();
        thread::sleep(Duration::from_secs(1));
    }
});

thread::spawn(move || {
    let vals = vec![
        String::from("more"),
        String::from("messages"),
        String::from("for"),
        String::from("you"),
    ];

    for val in vals {
        tx.send(val).unwrap();
        thread::sleep(Duration::from_secs(1));
    }
});

for received in rx {
    println!("Got: {received}");
}

--snip--
```

清单 16 - 11：从多个生产者发送多个消息

这一次，在我们创建第一个新线程之前，我们对发送端调用 `clone`。这将给我们一个新的发送端，我们可以将其传递给第一个新线程。我们将原始发送端传递给第二个新线程。这样我们就有了两个线程，每个线程都向同一个接收端发送不同的消息。

当你运行这段代码时，输出可能如下所示：

    Got: hi
    Got: more
    Got: from
    Got: messages
    Got: for
    Got: the
    Got: thread
    Got: you

根据你的系统，你可能会看到值以另一种顺序出现。这就是并发既有趣又困难的地方。如果你尝试使用 `thread::sleep`，在不同线程中给它设置不同的值，那么每次运行都会更加不可预测，并且每次都会产生不同的输出。

既然我们已经了解了通道的工作原理，接下来让我们看看另一种并发方法。
