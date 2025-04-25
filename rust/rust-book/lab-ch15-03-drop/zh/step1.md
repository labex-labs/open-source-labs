# 使用 Drop 特性在清理时运行代码

智能指针模式中第二个重要的特性是 `Drop`，它允许你自定义当一个值即将超出作用域时会发生什么。你可以为任何类型实现 `Drop` 特性，并且该代码可用于释放诸如文件或网络连接等资源。

我们在智能指针的上下文中引入 `Drop`，是因为在实现智能指针时几乎总会用到 `Drop` 特性的功能。例如，当一个 `Box<T>` 被丢弃时，它会释放该盒子所指向的堆上的空间。

在某些语言中，对于某些类型，程序员必须在每次使用完这些类型的实例后调用代码来释放内存或资源。例如文件句柄、套接字和锁。如果他们忘记了，系统可能会过载并崩溃。在 Rust 中，你可以指定每当一个值超出作用域时运行一段特定的代码，并且编译器会自动插入这段代码。因此，你无需担心在程序中每个特定类型的实例使用完毕的地方都放置清理代码 —— 你仍然不会泄漏资源！

你通过实现 `Drop` 特性来指定当一个值超出作用域时要运行的代码。`Drop` 特性要求你实现一个名为 `drop` 的方法，该方法接受一个指向 `self` 的可变引用。为了了解 Rust 何时调用 `drop`，我们现在先用 `println!` 语句来实现 `drop`。

清单 15-14 展示了一个 `CustomSmartPointer` 结构体，其唯一的自定义功能是当实例超出作用域时会打印 `Dropping CustomSmartPointer!`，以展示 Rust 何时运行 `drop` 方法。

文件名：`src/main.rs`

```rust
struct CustomSmartPointer {
    data: String,
}

impl Drop for CustomSmartPointer {
    fn drop(&mut self) {
        println!(
            "Dropping CustomSmartPointer with data `{}`!",
            self.data
        );
    }
}

fn main() {
    let c = CustomSmartPointer {
        data: String::from("my stuff"),
    };
    let d = CustomSmartPointer {
        data: String::from("other stuff"),
    };
    println!("CustomSmartPointers created.");
}
```

清单 15-14：一个实现了 `Drop` 特性的 `CustomSmartPointer` 结构体，我们会在其中放置清理代码

`Drop` 特性包含在 prelude 中，所以我们无需将其引入作用域。我们在 `CustomSmartPointer` 上实现 `Drop` 特性 \[1\]，并为调用 `println!` 的 `drop` 方法提供一个实现 \[2\]。`drop` 方法的主体是你想要在类型的实例超出作用域时运行的任何逻辑的放置位置。我们在这里打印一些文本，以便直观地展示 Rust 何时会调用 `drop`。

在 `main` 函数中，我们在 \[3\] 和 \[4\] 创建了两个 `CustomSmartPointer` 实例，然后打印 `CustomSmartPointers created` \[5\]。在 `main` 的末尾 \[6\]，我们的 `CustomSmartPointer` 实例将超出作用域，Rust 将调用我们在 `drop` 方法中放置的代码 \[2\]，打印我们的最终消息。请注意，我们无需显式调用 `drop` 方法。

当我们运行这个程序时，会看到以下输出：

    CustomSmartPointers created.
    Dropping CustomSmartPointer with data `other stuff`!
    Dropping CustomSmartPointer with data `my stuff`!

当我们的实例超出作用域时，Rust 会自动为我们调用 `drop`，调用我们指定的代码。变量按照创建的相反顺序被丢弃，所以 `d` 在 `c` 之前被丢弃。这个示例的目的是直观地向你展示 `drop` 方法是如何工作的；通常你会指定你的类型需要运行的清理代码，而不是打印消息。

不幸的是，禁用自动的 `drop` 功能并不简单。通常不需要禁用 `drop`；`Drop` 特性的重点就在于它会自动处理。然而，偶尔你可能想要提前清理一个值。一个例子是在使用管理锁的智能指针时：你可能想要强制调用释放锁的 `drop` 方法，以便同一作用域中的其他代码可以获取锁。Rust 不允许你手动调用 `Drop` 特性的 `drop` 方法；相反，如果你想在值的作用域结束前强制它被丢弃，你必须调用标准库提供的 `std::mem::drop` 函数。

如果我们尝试通过修改清单 15-14 中的 `main` 函数来手动调用 `Drop` 特性的 `drop` 方法，如清单 15-15 所示，我们会得到一个编译器错误。

文件名：`src/main.rs`

```rust
fn main() {
    let c = CustomSmartPointer {
        data: String::from("some data"),
    };
    println!("CustomSmartPointer created.");
    c.drop();
    println!(
        "CustomSmartPointer dropped before the end of main."
    );
}
```

清单 15-15：尝试手动调用 `Drop` 特性的 `drop` 方法以提前清理

当我们尝试编译这段代码时，会得到如下错误：

```bash
error[E0040]: explicit use of destructor method
  --> src/main.rs:16:7
   |
16 |     c.drop();
   |     --^^^^--
   |     | |
   |     | explicit destructor calls not allowed
   |     help: consider using `drop` function: `drop(c)`
```

这个错误信息表明我们不允许显式调用 `drop`。错误信息中使用了“析构函数”这个术语，它是用于清理实例的函数的通用编程术语。“析构函数”类似于“构造函数”，构造函数用于创建实例。Rust 中的 `drop` 函数就是一种特定的析构函数。

Rust 不允许我们显式调用 `drop`，因为在 `main` 函数结束时 Rust 仍然会自动对该值调用 `drop`。这会导致“双重释放”错误，因为 Rust 会尝试两次清理同一个值。

我们既不能禁用当一个值超出作用域时自动插入 `drop` 的操作，也不能显式调用 `drop` 方法。所以，如果我们需要提前强制清理一个值，我们就使用 `std::mem::drop` 函数。

`std::mem::drop` 函数与 `Drop` 特性中的 `drop` 方法不同。我们通过将想要强制丢弃的值作为参数传递来调用它。该函数在 prelude 中，所以我们可以修改清单 15-15 中的 `main` 函数来调用 `drop` 函数，如清单 15-16 所示。

文件名：`src/main.rs`

```rust
fn main() {
    let c = CustomSmartPointer {
        data: String::from("some data"),
    };
    println!("CustomSmartPointer created.");
    drop(c);
    println!(
        "CustomSmartPointer dropped before the end of main."
    );
}
```

清单 15-16：在值超出作用域之前调用 `std::mem::drop` 显式丢弃它

运行这段代码会打印如下内容：

    CustomSmartPointer created.
    Dropping CustomSmartPointer with data `some data`!
    CustomSmartPointer dropped before the end of main.

文本 `Dropping CustomSmartPointer with data `some data`!` 打印在 `CustomSmartPointer created.` 和 `CustomSmartPointer dropped before the end of main.` 文本之间，表明在那个时候调用了 `drop` 方法的代码来丢弃 `c`。

你可以以多种方式使用在 `Drop` 特性实现中指定的代码，以使清理变得方便和安全：例如，你可以用它来创建自己的内存分配器！有了 `Drop` 特性和 Rust 的所有权系统，你不必记得去清理，因为 Rust 会自动完成。

你也不必担心因意外清理仍在使用的值而产生的问题：确保引用始终有效的所有权系统也确保了只有在值不再被使用时 `drop` 才会被调用一次。

既然我们已经研究了 `Box<T>` 和智能指针的一些特性，接下来让我们看看标准库中定义的其他一些智能指针。
