# 错误时触发 `panic!` 的快捷方式：`unwrap` 和 `expect`

使用 `match` 已经足够好用了，但它可能会有点冗长，并且并不总是能很好地传达意图。`Result<T, E>` 类型定义了许多辅助方法来执行各种更具体的任务。`unwrap` 方法是一个快捷方法，其实现方式与我们在清单 9-4 中编写的 `match` 表达式类似。如果 `Result` 值是 `Ok` 变体，`unwrap` 将返回 `Ok` 内部的值。如果 `Result` 是 `Err` 变体，`unwrap` 将为我们调用 `panic!` 宏。以下是 `unwrap` 的一个实际示例：

文件名：`src/main.rs`

```rust
use std::fs::File;

fn main() {
    let greeting_file = File::open("hello.txt").unwrap();
}
```

如果我们在没有 _hello.txt_ 文件的情况下运行此代码，我们将看到 `unwrap` 方法调用 `panic!` 时的错误消息：

    thread'main' panicked at 'called `Result::unwrap()` on an `Err` value: Os {
    code: 2, kind: NotFound, message: "No such file or directory" }',
    src/main.rs:4:49

同样，`expect` 方法让我们也可以选择 `panic!` 错误消息。使用 `expect` 而不是 `unwrap` 并提供良好的错误消息可以传达你的意图，并使追踪 `panic!` 的源头更容易。`expect` 的语法如下：

文件名：`src/main.rs`

```rust
use std::fs::File;

fn main() {
    let greeting_file = File::open("hello.txt")
     .expect("hello.txt should be included in this project");
}
```

我们使用 `expect` 的方式与 `unwrap` 相同：返回文件句柄或调用 `panic!` 宏。`expect` 在调用 `panic!` 时使用的错误消息将是我们传递给 `expect` 的参数，而不是 `unwrap` 使用的默认 `panic!` 消息。如下所示：

    thread'main' panicked at 'hello.txt should be included in this project: Os {
    code: 2, kind: NotFound, message: "No such file or directory" }',
    src/main.rs:5:10

在生产质量的代码中，大多数 Rust 开发者会选择 `expect` 而不是 `unwrap`，并给出更多关于为什么该操作预期总是会成功的上下文信息。这样，如果你的假设被证明是错误的，你在调试时就有更多信息可供使用。
