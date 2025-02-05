# 返回闭包

闭包由 trait 表示，这意味着你不能直接返回闭包。在大多数你可能想要返回 trait 的情况下，你可以改为使用实现该 trait 的具体类型作为函数的返回值。然而，对于闭包你不能这样做，因为它们没有可返回的具体类型；例如，你不被允许使用函数指针 `fn` 作为返回类型。

以下代码尝试直接返回一个闭包，但它无法编译：

```rust
fn returns_closure() -> dyn Fn(i32) -> i32 {
    |x| x + 1
}
```

编译器错误如下：

```bash
error[E0746]: return type cannot have an unboxed trait object
 --> src/lib.rs:1:25
  |
1 | fn returns_closure() -> dyn Fn(i32) -> i32 {
  |                         ^^^^^^^^^^^^^^^^^^ doesn't have a size known at
compile-time
  |
  = note: for information on `impl Trait`, see
<https://doc.rust-lang.org/book/ch10-02-traits.html#returning-types-that-
implement-traits>
help: use `impl Fn(i32) -> i32` as the return type, as all return paths are of
type `[closure@src/lib.rs:2:5: 2:14]`, which implements `Fn(i32) -> i32`
  |
1 | fn returns_closure() -> impl Fn(i32) -> i32 {
  |                         ~~~~~~~~~~~~~~~~~~~
```

错误再次引用了 `Sized` trait！Rust 不知道需要多少空间来存储闭包。我们之前见过这个问题的解决方案。我们可以使用 trait 对象：

```rust
fn returns_closure() -> Box<dyn Fn(i32) -> i32> {
    Box::new(|x| x + 1)
}
```

这段代码将顺利编译。有关 trait 对象的更多信息，请参考“使用允许不同类型值的 trait 对象”。

接下来，让我们看看宏！
