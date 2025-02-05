# 在线程中使用 `move` 闭包

我们经常会在传递给 `thread::spawn` 的闭包中使用 `move` 关键字，因为这样闭包就会获取其从环境中使用的值的所有权，从而将这些值的所有权从一个线程转移到另一个线程。在“使用闭包捕获环境”中，我们在闭包的上下文中讨论了 `move`。现在我们将更多地关注 `move` 与 `thread::spawn` 之间的交互。

注意在清单16-1中，我们传递给 `thread::spawn` 的闭包没有参数：我们在派生线程的代码中没有使用主线程中的任何数据。要在派生线程中使用主线程中的数据，派生线程的闭包必须捕获它需要的值。清单16-3展示了一个在主线程中创建一个向量并在派生线程中使用它的尝试。然而，正如你马上会看到的，这目前还无法工作。

文件名：`src/main.rs`

```rust
use std::thread;

fn main() {
    let v = vec![1, 2, 3];

    let handle = thread::spawn(|| {
        println!("Here's a vector: {:?}", v);
    });

    handle.join().unwrap();
}
```

清单16-3：尝试在另一个线程中使用主线程创建的向量

闭包使用了 `v`，所以它会捕获 `v` 并使其成为闭包环境的一部分。因为 `thread::spawn` 在一个新线程中运行这个闭包，我们应该能够在那个新线程中访问 `v`。但是当我们编译这个示例时，会得到以下错误：

```bash
error[E0373]: closure may outlive the current function, but it borrows `v`,
which is owned by the current function
 --> src/main.rs:6:32
  |
6 |     let handle = thread::spawn(|| {
  |                                ^^ may outlive borrowed value `v`
7 |         println!("Here's a vector: {:?}", v);
  |                                           - `v` is borrowed here
  |
note: function requires argument type to outlive `'static`
 --> src/main.rs:6:18
  |
6 |       let handle = thread::spawn(|| {
  |  __________________^
7 | |         println!("Here's a vector: {:?}", v);
8 | |     });
  | |______^
help: to force the closure to take ownership of `v` (and any other referenced
variables), use the `move` keyword
  |
6 |     let handle = thread::spawn(move || {
  |                                ++++
```

Rust **推断** 如何捕获 `v`，并且因为 `println!` 只需要对 `v` 的引用，所以闭包尝试借用 `v`。然而，有一个问题：Rust 无法知道派生线程会运行多长时间，所以它不知道对 `v` 的引用是否总是有效。

清单16-4提供了一个更有可能出现对 `v` 的引用无效的场景。

文件名：`src/main.rs`

```rust
use std::thread;

fn main() {
    let v = vec![1, 2, 3];

    let handle = thread::spawn(|| {
        println!("Here's a vector: {:?}", v);
    });

    drop(v); // 糟了！

    handle.join().unwrap();
}
```

清单16-4：一个线程中的闭包尝试从主线程捕获对 `v` 的引用，而主线程丢弃了 `v`

如果 Rust 允许我们运行这段代码，有可能派生线程会立即被放到后台而根本不运行。派生线程内部有一个对 `v` 的引用，但是主线程立即使用我们在第15章讨论过的 `drop` 函数丢弃了 `v`。然后，当派生线程开始执行时，`v` 不再有效，所以对它的引用也无效了。糟了！

要修复清单16-3中的编译器错误，我们可以按照错误消息的建议来做：

    help: to force the closure to take ownership of `v` (and any other referenced
    variables), use the `move` keyword
      |
    6 |     let handle = thread::spawn(move || {
      |                                ++++

通过在闭包之前添加 `move` 关键字，我们强制闭包获取它正在使用的值的所有权，而不是让 Rust 推断它应该借用这些值。清单16-5中对清单16-3的修改将按我们预期的那样编译并运行。

文件名：`src/main.rs`

```rust
use std::thread;

fn main() {
    let v = vec![1, 2, 3];

    let handle = thread::spawn(move || {
        println!("Here's a vector: {:?}", v);
    });

    handle.join().unwrap();
}
```

清单16-5：使用 `move` 关键字强制闭包获取它使用的值的所有权

我们可能会想尝试用同样的方法来修复清单16-4中主线程调用 `drop` 的代码，即使用一个 `move` 闭包。然而，这个修复方法行不通，因为清单16-4试图做的事情由于另一个原因是不被允许的。如果我们在闭包中添加 `move`，我们会将 `v` 移动到闭包的环境中，并且我们将无法再在主线程中对它调用 `drop`。我们会得到这个编译器错误：

```bash
error[E0382]: use of moved value: `v`
  --> src/main.rs:10:10
   |
4  |     let v = vec![1, 2, 3];
   |         - move occurs because `v` has type `Vec<i32>`, which does not
implement the `Copy` trait
5  |
6  |     let handle = thread::spawn(move || {
   |                                ------- value moved into closure here
7  |         println!("Here's a vector: {:?}", v);
   |                                           - variable moved due to use in
closure
...
10 |     drop(v); // oh no!
   |          ^ value used here after move
```

Rust 的所有权规则又一次帮了我们！我们从清单16-3的代码中得到一个错误，是因为 Rust 比较保守，只在线程中借用 `v`，这意味着主线程理论上可以使派生线程的引用无效。通过告诉 Rust 将 `v` 的所有权移动到派生线程，我们向 Rust 保证主线程不会再使用 `v` 了。如果我们以同样的方式修改清单16-4，那么当我们试图在主线程中使用 `v` 时，就会违反所有权规则。`move` 关键字覆盖了 Rust 保守的默认借用行为；它不会让我们违反所有权规则。

既然我们已经介绍了线程是什么以及线程 API 提供的方法，让我们来看看一些可以使用线程的场景。
