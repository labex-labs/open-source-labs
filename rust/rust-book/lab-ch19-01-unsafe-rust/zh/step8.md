# 实现不安全的 trait

我们可以使用 `unsafe` 来实现一个不安全的 trait。当一个 trait 的至少一个方法具有编译器无法验证的某种不变量时，该 trait 就是不安全的。我们通过在 `trait` 之前添加 `unsafe` 关键字，并将 trait 的实现也标记为 `unsafe`，来声明一个 trait 是不安全的，如清单 19-11 所示。

```rust
unsafe trait Foo {
    // 方法定义在此处
}

unsafe impl Foo for i32 {
    // 方法实现在此处
}
```

清单 19-11：定义和实现一个不安全的 trait

通过使用 `unsafe impl`，我们承诺会遵守编译器无法验证的不变量。

例如，回忆一下我们在“使用 Send 和 Sync trait 实现可扩展并发”中讨论的 `Send` 和 `Sync` 标记 trait：如果我们的类型完全由 `Send` 和 `Sync` 类型组成，编译器会自动实现这些 trait。如果我们实现的类型包含一个不是 `Send` 或 `Sync` 的类型，比如裸指针，并且我们想将该类型标记为 `Send` 或 `Sync`，就必须使用 `unsafe`。Rust 无法验证我们的类型是否遵守可以安全地跨线程发送或从多个线程访问的保证；因此，我们需要手动进行这些检查，并使用 `unsafe` 来表明这一点。
