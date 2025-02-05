# 多线程中的多重所有权

在第15章中，我们通过使用智能指针 `Rc<T>` 创建一个引用计数的值，将一个值赋予多个所有者。让我们在这里做同样的事情，看看会发生什么。在清单16 - 14中，我们将 `Mutex<T>` 包装在 `Rc<T>` 中，并在将所有权转移到线程之前克隆 `Rc<T>`。

文件名：`src/main.rs`

```rust
use std::rc::Rc;
use std::sync::Mutex;
use std::thread;

fn main() {
    let counter = Rc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..10 {
        let counter = Rc::clone(&counter);
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

清单16 - 14：尝试使用 `Rc<T>` 让多个线程拥有 `Mutex<T>`

再一次，我们编译后得到了……不同的错误！编译器教会了我们很多。

```bash
error[E0277]: `Rc<Mutex<i32>>` cannot be sent between threads safely 1
   --> src/main.rs:11:22
    |
11  |           let handle = thread::spawn(move || {
    |  ______________________^^^^^^^^^^^^^_-
    | |                      |
    | |                      `Rc<Mutex<i32>>` cannot be sent between threads
safely
12  | |             let mut num = counter.lock().unwrap();
13  | |
14  | |             *num += 1;
15  | |         });
    | |_________- within this `[closure@src/main.rs:11:36: 15:10]`
    |
= help: within `[closure@src/main.rs:11:36: 15:10]`, the trait `Send` is not
implemented for `Rc<Mutex<i32>>` 2
    = note: required because it appears within the type
`[closure@src/main.rs:11:36: 15:10]`
note: required by a bound in `spawn`
```

哇，那个错误信息好长啊！这里需要关注的重要部分是：“`Rc<Mutex<i32>>` 不能在线程之间安全地传递”\[1\]。编译器也告诉了我们原因：“`Rc<Mutex<i32>>` 没有实现 `Send` 特性”\[2\]。我们将在下一节讨论 `Send`：它是确保我们在线程中使用的类型适用于并发情况的特性之一。

不幸的是，`Rc<T>` 在线程间共享是不安全的。当 `Rc<T>` 管理引用计数时，每次调用 `clone` 它都会增加计数，每次克隆被丢弃时都会减少计数。但它没有使用任何并发原语来确保对计数的更改不会被另一个线程中断。这可能会导致错误的计数——这些微妙的错误可能会进而导致内存泄漏或在我们用完一个值之前它就被丢弃。我们需要的是一种与 `Rc<T>` 完全一样的类型，但它能以线程安全的方式更改引用计数。
