# `while let` 条件循环

`while let` 条件循环在结构上与 `if let` 类似，它允许 `while` 循环只要模式持续匹配就一直运行。在清单 18-2 中，我们编写了一个 `while let` 循环，它将一个向量用作栈，并以与入栈相反的顺序打印向量中的值。

文件名：`src/main.rs`

```rust
let mut stack = Vec::new();

stack.push(1);
stack.push(2);
stack.push(3);

while let Some(top) = stack.pop() {
    println!("{top}");
}
```

清单 18-2：使用 `while let` 循环，只要 `stack.pop()` 返回 `Some` 就打印值

这个示例打印出 `3`、`2`，然后是 `1`。`pop` 方法从向量中取出最后一个元素并返回 `Some(value)`。如果向量为空，`pop` 返回 `None`。只要 `pop` 返回 `Some`，`while` 循环就会继续运行其块中的代码。当 `pop` 返回 `None` 时，循环停止。我们可以使用 `while let` 从栈中弹出每个元素。
