# 可反驳性：模式是否可能匹配失败

模式有两种形式：可反驳的和不可反驳的。对于任何传入的可能值都能匹配的模式是**不可反驳的**。例如，在语句 `let x = 5;` 中的 `x`，因为 `x` 可以匹配任何值，所以不可能匹配失败。对于某些可能值可能匹配失败的模式是**可反驳的**。例如，在表达式 `if let Some(x) = a_value` 中的 `Some(x)`，因为如果 `a_value` 变量中的值是 `None` 而不是 `Some`，那么 `Some(x)` 模式将无法匹配。

函数参数、`let` 语句和 `for` 循环只能接受不可反驳的模式，因为当值不匹配时，程序无法做任何有意义的事情。`if let` 和 `while let` 表达式既可以接受可反驳的模式，也可以接受不可反驳的模式，但编译器会对不可反驳的模式发出警告，因为根据定义，它们旨在处理可能的失败情况：条件语句的功能在于根据成功或失败执行不同的操作。

一般来说，你不必担心可反驳模式和不可反驳模式之间的区别；然而，你确实需要熟悉可反驳性的概念，以便在错误消息中看到它时能够做出响应。在这些情况下，你需要根据代码的预期行为，更改模式或使用该模式的结构。

让我们来看一个例子，当我们尝试在 Rust 需要不可反驳模式的地方使用可反驳模式，或者反之亦然时会发生什么。清单 18 - 8 展示了一个 `let` 语句，但对于模式，我们指定了 `Some(x)`，这是一个可反驳的模式。正如你可能预期的那样，这段代码不会编译。

```rust
let Some(x) = some_option_value;
```

清单 18 - 8：尝试在 `let` 中使用可反驳模式

如果 `some_option_value` 是 `None` 值，它将无法匹配模式 `Some(x)`，这意味着该模式是可反驳的。然而，`let` 语句只能接受不可反驳的模式，因为对于 `None` 值，代码无法进行有效的处理。在编译时，Rust 会抱怨我们试图在需要不可反驳模式的地方使用了可反驳模式：

```bash
error[E0005]: refutable pattern in local binding: `None` not covered
   --> src/main.rs:3:9
    |
3   |     let Some(x) = some_option_value;
    |         ^^^^^^^ pattern `None` not covered
    |
    = note: `let` bindings require an "irrefutable pattern", like a `struct` or
an `enum` with only one variant
    = note: for more information, visit
https://doc.rust-lang.org/book/ch18-02-refutability.html
    = note: the matched value is of type `Option<i32>`
help: you might want to use `if let` to ignore the variant that isn't matched
    |
3   |     let x = if let Some(x) = some_option_value { x } else { todo!() };
    |     ++++++++++                                 ++++++++++++++++++++++
```

因为我们没有用模式 `Some(x)` 覆盖（也无法覆盖！）每个有效的值，所以 Rust 理所当然地产生了一个编译错误。

如果我们在需要不可反驳模式的地方有一个可反驳模式，我们可以通过更改使用该模式的代码来修复它：我们可以使用 `if let` 而不是 `let`。然后，如果模式不匹配，代码将跳过花括号中的代码，从而提供一种继续有效执行的方式。清单 18 - 9 展示了如何修复清单 18 - 8 中的代码。

```rust
if let Some(x) = some_option_value {
    println!("{x}");
}
```

清单 18 - 9：使用 `if let` 和带有可反驳模式的代码块代替 `let`

我们给代码提供了一个解决方案！这段代码是完全有效的，尽管这意味着如果不接收错误，我们就不能使用不可反驳模式。如果我们给 `if let` 一个总是能匹配的模式，比如 `x`，如清单 18 - 10 所示，编译器会发出警告。

```rust
if let x = 5 {
    println!("{x}");
};
```

清单 18 - 10：尝试在 `if let` 中使用不可反驳模式

Rust 会抱怨使用不可反驳模式与 `if let` 没有意义：

```bash
warning: irrefutable `if let` pattern
 --> src/main.rs:2:8
  |
2 |     if let x = 5 {
  |        ^^^^^^^^^
  |
  = note: `#[warn(irrefutable_let_patterns)]` on by default
  = note: this pattern will always match, so the `if let` is
useless
  = help: consider replacing the `if let` with a `let`
```

出于这个原因，`match` 分支必须使用可反驳模式，除了最后一个分支，它应该使用不可反驳模式来匹配任何剩余的值。Rust 允许我们在只有一个分支的 `match` 中使用不可反驳模式，但这种语法并不是特别有用，可以用更简单的 `let` 语句来代替。

既然你已经知道了在哪里使用模式以及可反驳模式和不可反驳模式之间的区别，那么让我们来介绍一下我们可以用来创建模式的所有语法。
