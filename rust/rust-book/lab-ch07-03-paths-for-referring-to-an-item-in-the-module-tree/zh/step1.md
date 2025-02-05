# 模块树中引用项的路径

为了向 Rust 指明在模块树中何处找到某个项，我们使用路径，就像在文件系统中导航时使用路径一样。要调用一个函数，我们需要知道它的路径。

路径可以有两种形式：

- **绝对路径**：是从 crate 根开始的完整路径；对于来自外部 crate 的代码，绝对路径以 crate 名称开头，对于来自当前 crate 的代码，它以字面量 `crate` 开头。
- **相对路径**：从当前模块开始，并使用 `self`、`super` 或当前模块中的标识符。

绝对路径和相对路径后面都跟着一个或多个由双冒号（`::`）分隔的标识符。

回到清单 7-1，假设我们想要调用 `add_to_waitlist` 函数。这就相当于问：`add_to_waitlist` 函数的路径是什么？清单 7-3 包含了清单 7-1，但移除了一些模块和函数。

我们将展示两种从 crate 根中定义的新函数 `eat_at_restaurant` 调用 `add_to_waitlist` 函数的方法。这些路径是正确的，但还有另一个问题会阻止这个示例按原样编译。我们稍后会解释原因。

`eat_at_restaurant` 函数是我们库 crate 公共 API 的一部分，所以我们用 `pub` 关键字标记它。在“使用 `pub` 关键字暴露路径”中，我们将更详细地介绍 `pub`。

文件名：`src/lib.rs`

```rust
mod front_of_house {
    mod hosting {
        fn add_to_waitlist() {}
    }
}

pub fn eat_at_restaurant() {
    // 绝对路径
    crate::front_of_house::hosting::add_to_waitlist();

    // 相对路径
    front_of_house::hosting::add_to_waitlist();
}
```

清单 7-3：使用绝对路径和相对路径调用 `add_to_waitlist` 函数

我们第一次在 `eat_at_restaurant` 中调用 `add_to_waitlist` 函数时，使用了绝对路径。`add_to_waitlist` 函数与 `eat_at_restaurant` 在同一个 crate 中定义，这意味着我们可以使用 `crate` 关键字来开始一个绝对路径。然后我们包含每个后续模块，直到找到 `add_to_waitlist`。你可以想象一个具有相同结构的文件系统：我们会指定路径 `/front_of_house/hosting/add_to_waitlist` 来运行 `add_to_waitlist` 程序；使用 `crate` 名称从 crate 根开始，就像在 shell 中使用 `/` 从文件系统根开始一样。

我们第二次在 `eat_at_restaurant` 中调用 `add_to_waitlist` 时，使用了相对路径。路径以 `front_of_house` 开头，它是在模块树中与 `eat_at_restaurant` 处于同一级别的模块名称。这里对应的文件系统路径是 `front_of_house/hosting/add_to_waitlist`。以模块名称开头意味着该路径是相对的。

选择使用相对路径还是绝对路径，这是你要根据项目情况做出的决定，这取决于你更倾向于将项定义代码与使用该项的代码分开还是一起移动。例如，如果我们将 `front_of_house` 模块和 `eat_at_restaurant` 函数移动到一个名为 `customer_experience` 的模块中，我们需要更新到 `add_to_waitlist` 的绝对路径，但相对路径仍然有效。然而，如果我们将 `eat_at_restaurant` 函数单独移动到一个名为 `dining` 的模块中，到 `add_to_waitlist` 调用的绝对路径将保持不变，但相对路径需要更新。一般来说，我们更倾向于指定绝对路径，因为我们更有可能希望独立地移动代码定义和项调用。

让我们尝试编译清单 7-3，看看为什么它还不能编译！我们得到的错误如清单 7-4 所示。

```bash
$ cargo build
   Compiling restaurant v0.1.0 (file:///projects/restaurant)
error[E0603]: module `hosting` is private
 --> src/lib.rs:9:28
  |
9 |     crate::front_of_house::hosting::add_to_waitlist();
  |                            ^^^^^^^ private module
  |
note: the module `hosting` is defined here
 --> src/lib.rs:2:5
  |
2 |     mod hosting {
  |     ^^^^^^^^^^^

error[E0603]: module `hosting` is private
  --> src/lib.rs:12:21
   |
12 |     front_of_house::hosting::add_to_waitlist();
   |                     ^^^^^^^ private module
   |
note: the module `hosting` is defined here
  --> src/lib.rs:2:5
   |
2  |     mod hosting {
   |     ^^^^^^^^^^^
```

清单 7-4：构建清单 7-3 中的代码时的编译器错误

错误消息说模块 `hosting` 是私有的。换句话说，我们对于 `hosting` 模块和 `add_to_waitlist` 函数有正确的路径，但 Rust 不让我们使用它们，因为它无法访问私有部分。在 Rust 中，默认情况下，所有项（函数、方法、结构体、枚举、模块和常量）对于父模块都是私有的。如果你想让像函数或结构体这样的项成为私有，你把它放在一个模块中。

父模块中的项不能使用子模块中的私有项，但子模块中的项可以使用其祖先模块中的项。这是因为子模块封装并隐藏了它们的实现细节，但子模块可以看到它们所定义的上下文。继续用我们的比喻来说，把隐私规则想象成餐厅的后台办公室：里面发生的事情对餐厅顾客来说是私有的，但办公室经理可以看到并处理他们经营的餐厅里的一切。

Rust 选择让模块系统以这种方式工作，以便隐藏内部实现细节是默认行为。这样，你就知道在不破坏外部代码的情况下，可以更改内部代码的哪些部分。然而，Rust 确实给你提供了一个选项，即通过使用 `pub` 关键字使项公开，从而将子模块代码的内部部分暴露给外部祖先模块。
