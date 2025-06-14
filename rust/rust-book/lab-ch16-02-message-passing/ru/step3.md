# Отправка нескольких значений и наблюдение за ожиданием получателя

Код из Listing 16-8 скомпилировался и запустился, но он не показал нам явно, что два отдельных потока общаются друг с другом по каналу. В Listing 16-10 мы внесли некоторые изменения, которые будут доказывать, что код из Listing 16-8 выполняется параллельно: созданный поток теперь будет отправлять несколько сообщений и останавливаться на секунду между каждым сообщением.

Filename: `src/main.rs`

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

Listing 16-10: Отправка нескольких сообщений и пауза между каждым

На этот раз созданный поток имеет вектор строк, которые мы хотим отправить в главный поток. Мы итерируемся по ним, отправляя каждый отдельно, и останавливаемся между каждым вызовом функции `thread::sleep` с значением `Duration` в одну секунду.

В главном потоке мы不再显式调用`recv`函数：相反，我们将`rx`视为一个迭代器。对于接收到的每个值，我们都将其打印出来。当通道关闭时，迭代将结束。

当运行 Listing 16-10 中的代码时，你应该会看到以下输出，每行之间有一秒的停顿：

    Got: hi
    Got: from
    Got: the
    Got: thread

因为我们在主线程的`for`循环中没有任何暂停或延迟的代码，所以我们可以看出主线程在等待从生成的线程接收值。
