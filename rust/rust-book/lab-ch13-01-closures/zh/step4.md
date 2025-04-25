# 捕获引用或转移所有权

闭包可以通过三种方式从其环境中捕获值，这三种方式直接对应于函数获取参数的三种方式：不可变借用、可变借用和获取所有权。闭包将根据函数体对捕获值的操作来决定使用哪种方式。

在清单 13-4 中，我们定义了一个闭包，它捕获了对名为 `list` 的向量的不可变引用，因为它只需要一个不可变引用来打印值。

文件名：`src/main.rs`

```rust
fn main() {
    let list = vec![1, 2, 3];
    println!("Before defining closure: {:?}", list);

  1 let only_borrows = || println!("From closure: {:?}", list);

    println!("Before calling closure: {:?}", list);
  2 only_borrows();
    println!("After calling closure: {:?}", list);
}
```

清单 13-4：定义并调用一个捕获不可变引用的闭包

这个例子还说明了一个变量可以绑定到闭包定义 \[1\]，并且我们可以在之后通过使用变量名和括号来调用闭包，就好像变量名是一个函数名一样 \[2\]。

因为我们可以同时对 `list` 有多个不可变引用，所以在闭包定义之前、闭包定义之后但在闭包调用之前以及闭包调用之后的代码中，`list` 仍然是可访问的。这段代码可以编译、运行并打印：

    Before defining closure: [1, 2, 3]
    Before calling closure: [1, 2, 3]
    From closure: [1, 2, 3]
    After calling closure: [1, 2, 3]

接下来，在清单 13-5 中，我们更改闭包体，使其向 `list` 向量中添加一个元素。现在闭包捕获一个可变引用。

文件名：`src/main.rs`

```rust
fn main() {
    let mut list = vec![1, 2, 3];
    println!("Before defining closure: {:?}", list);

    let mut borrows_mutably = || list.push(7);

    borrows_mutably();
    println!("After calling closure: {:?}", list);
}
```

清单 13-5：定义并调用一个捕获可变引用的闭包

这段代码可以编译、运行并打印：

```rust
Before defining closure: [1, 2, 3]
After calling closure: [1, 2, 3, 7]
```

请注意，在 `borrows_mutably` 闭包的定义和调用之间不再有 `println!`：当定义 `borrows_mutably` 时，它捕获了对 `list` 的可变引用。在闭包调用之后我们不再使用该闭包，所以可变借用结束。在闭包定义和闭包调用之间，不允许进行不可变借用以进行打印，因为当存在可变借用时不允许有其他借用。尝试在那里添加一个 `println!`，看看会得到什么错误消息！

如果你想强制闭包获取它在环境中使用的值的所有权，即使闭包体并不严格需要所有权，你可以在参数列表之前使用 `move` 关键字。

这种技术在将闭包传递给新线程以转移数据以便新线程拥有它时最为有用。我们将在第 16 章讨论并发时详细讨论线程以及为什么要使用它们，但现在，让我们简要探讨一下使用需要 `move` 关键字的闭包来创建一个新线程。清单 13-6 展示了对清单 13-4 的修改，以便在新线程中而不是在主线程中打印向量。

文件名：`src/main.rs`

```rust
use std::thread;

fn main() {
    let list = vec![1, 2, 3];
    println!("Before defining closure: {:?}", list);

  1 thread::spawn(move || {
      2 println!("From thread: {:?}", list)
    }).join().unwrap();
}
```

清单 13-6：使用 `move` 强制线程的闭包获取 `list` 的所有权

我们创建一个新线程，将一个闭包作为参数传递给该线程来运行。闭包体打印出列表。在清单 13-4 中，闭包只使用不可变引用来捕获 `list`，因为打印它所需的对 `list` 的访问权限最少。在这个例子中，即使闭包体仍然只需要一个不可变引用 \[2\]，我们也需要通过在闭包定义的开头放置 `move` 关键字 \[1\] 来指定 `list` 应该被转移到闭包中。新线程可能在主线程的其余部分完成之前完成，或者主线程可能先完成。如果主线程保持对 `list` 的所有权但在新线程之前结束并释放 `list`，则线程中的不可变引用将无效。因此，编译器要求将 `list` 转移到传递给新线程的闭包中，这样引用才会有效。尝试移除 `move` 关键字，或者在闭包定义之后在主线程中使用 `list`，看看会得到什么编译器错误！
