# `match` 必须穷举所有情况

关于 `match`，我们还需要讨论另一个方面：分支的模式必须涵盖所有可能性。看看我们的 `plus_one` 函数的这个版本，它有一个错误并且无法编译：

```rust
fn plus_one(x: Option<i32>) -> Option<i32> {
    match x {
        Some(i) => Some(i + 1),
    }
}
```

我们没有处理 `None` 的情况，所以这段代码会导致一个错误。幸运的是，这是 Rust 能够捕获的错误。如果我们尝试编译这段代码，会得到如下错误：

```bash
error[E0004]: non-exhaustive patterns: `None` not covered
 --> src/main.rs:3:15
  |
3 |         match x {
  |               ^ pattern `None` not covered
  |
  note: `Option<i32>` defined here
      = note: the matched value is of type `Option<i32>`
help: ensure that all possible cases are being handled by adding
a match arm with a wildcard pattern or an explicit pattern as
shown
    |
4   ~             Some(i) => Some(i + 1),
5   ~             None => todo!(),
    |
```

Rust 知道我们没有涵盖每一种可能的情况，甚至知道我们忘记了哪种模式！Rust 中的 `match` 是**穷举的**：我们必须穷尽每一种可能性，代码才有效。特别是在 `Option<T>` 的情况下，当 Rust 防止我们忘记显式处理 `None` 情况时，它保护我们不会在可能为 `null` 的时候假设我们有一个值，从而避免了前面讨论的那种造成巨大损失的错误。
