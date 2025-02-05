# 使用 RefCell`<T>` 在运行时跟踪借用情况

在创建不可变引用和可变引用时，我们分别使用 `&` 和 `&mut` 语法。对于 `RefCell<T>`，我们使用 `borrow` 和 `borrow_mut` 方法，它们是属于 `RefCell<T>` 的安全 API 的一部分。`borrow` 方法返回智能指针类型 `Ref<T>`，`borrow_mut` 返回智能指针类型 `RefMut<T>`。这两种类型都实现了 `Deref`，所以我们可以像对待普通引用一样对待它们。

`RefCell<T>` 会跟踪当前有多少个 `Ref<T>` 和 `RefMut<T>` 智能指针处于活动状态。每次我们调用 `borrow` 时，`RefCell<T>` 会增加其处于活动状态的不可变借用数量的计数。当一个 `Ref<T>` 值超出作用域时，不可变借用的计数会减 1。就像编译时的借用规则一样，`RefCell<T>` 允许我们在任何时刻拥有多个不可变借用或一个可变借用。

如果我们试图违反这些规则，与使用引用时会得到编译时错误不同，`RefCell<T>` 的实现会在运行时恐慌。清单 15 - 23 展示了对清单 15 - 22 中 `send` 方法实现的修改。我们故意尝试在同一作用域内创建两个活动的可变借用，以说明 `RefCell<T>` 在运行时会阻止我们这样做。

文件名：`src/lib.rs`

```rust
impl Messenger for MockMessenger {
    fn send(&self, message: &str) {
        let mut one_borrow = self.sent_messages.borrow_mut();
        let mut two_borrow = self.sent_messages.borrow_mut();

        one_borrow.push(String::from(message));
        two_borrow.push(String::from(message));
    }
}
```

清单 15 - 23：在同一作用域内创建两个可变引用以查看 `RefCell<T>` 会恐慌

我们为从 `borrow_mut` 返回的 `RefMut<T>` 智能指针创建一个变量 `one_borrow`。然后我们以相同的方式在变量 `two_borrow` 中创建另一个可变借用。这在同一作用域内创建了两个可变引用，这是不允许的。当我们运行库的测试时，清单 15 - 23 中的代码将在没有任何错误的情况下编译，但测试会失败：

    ---- tests::it_sends_an_over_75_percent_warning_message stdout ----
    thread 'main' panicked at 'already borrowed: BorrowMutError', src/lib.rs:60:53
    note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

注意，代码因消息 `already borrowed: BorrowMutError` 而恐慌。这就是 `RefCell<T>` 在运行时处理违反借用规则的方式。

像我们在这里所做的那样，选择在运行时而不是编译时捕获借用错误，意味着你可能会在开发过程的后期才发现代码中的错误：可能直到你的代码部署到生产环境中才会发现。此外，由于在运行时而不是编译时跟踪借用情况，你的代码会在运行时产生轻微的性能开销。然而，使用 `RefCell<T>` 可以让你编写一个模拟对象，在只允许不可变值的上下文中使用它时，该模拟对象可以自我修改以跟踪它所看到的消息。尽管有这些权衡，你仍然可以使用 `RefCell<T>` 来获得比普通引用更多的功能。
