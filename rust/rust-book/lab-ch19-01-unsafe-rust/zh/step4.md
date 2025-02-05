# 调用不安全的函数或方法

你可以在不安全块中执行的第二种操作是调用不安全函数。不安全函数和方法看起来与普通函数和方法完全一样，但在定义的其他部分之前有一个额外的 `unsafe`。在此上下文中，`unsafe` 关键字表示该函数在我们调用它时有一些要求我们需要遵守，因为 Rust 无法保证我们满足了这些要求。通过在 `unsafe` 块内调用不安全函数，我们是在表明我们已经阅读了该函数的文档，并负责遵守该函数的约定。

这里有一个名为 `dangerous` 的不安全函数，其函数体中不做任何事情：

```rust
unsafe fn dangerous() {}

unsafe {
    dangerous();
}
```

我们必须在一个单独的 `unsafe` 块内调用 `dangerous` 函数。如果我们尝试在没有 `unsafe` 块的情况下调用 `dangerous`，我们会得到一个错误：

```bash
error[E0133]: call to unsafe function is unsafe and requires
unsafe function or block
 --> src/main.rs:4:5
  |
4 |     dangerous();
  |     ^^^^^^^^^^^ call to unsafe function
  |
  = note: consult the function's documentation for information on
how to avoid undefined behavior
```

使用 `unsafe` 块，我们向 Rust 断言我们已经阅读了该函数的文档，我们知道如何正确使用它，并且我们已经验证我们正在履行该函数的约定。

不安全函数的函数体实际上就是 `unsafe` 块，所以要在不安全函数内执行其他不安全操作，我们不需要再添加另一个 `unsafe` 块。
