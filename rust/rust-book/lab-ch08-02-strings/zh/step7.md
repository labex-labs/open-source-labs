# 对字符串进行索引

在许多其他编程语言中，通过索引引用字符串中的单个字符是一种有效且常见的操作。然而，如果你尝试在 Rust 中使用索引语法来访问 `String` 的部分内容，将会得到一个错误。考虑清单 8-19 中的无效代码。

```rust
let s1 = String::from("hello");
let h = s1[0];
```

清单 8-19：尝试对 `String` 使用索引语法

这段代码将导致以下错误：

```bash
error[E0277]: the type `String` cannot be indexed by `{integer}`
 --> src/main.rs:3:13
  |
3 |     let h = s1[0];
  |             ^^^^^ `String` cannot be indexed by `{integer}`
  |
  = help: the trait `Index<{integer}>` is not implemented for
`String`
```

错误信息和提示说明了原因：Rust 字符串不支持索引。但为什么不支持呢？要回答这个问题，我们需要讨论 Rust 在内存中如何存储字符串。
