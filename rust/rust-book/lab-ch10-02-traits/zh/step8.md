# 使用 where 子句实现更清晰的特性约束

使用过多的特性约束有其缺点。每个泛型都有自己的特性约束，所以带有多个泛型类型参数的函数在函数名和参数列表之间可能包含大量的特性约束信息，这使得函数签名难以阅读。出于这个原因，Rust 有一种替代语法，用于在函数签名后的 `where` 子句中指定特性约束。所以，不用这样写：

```rust
fn some_function<T: Display + Clone, U: Clone + Debug>(t: &T, u: &U) -> i32 {
```

我们可以使用 `where` 子句，像这样：

```rust
fn some_function<T, U>(t: &T, u: &U) -> i32
where
    T: Display + Clone,
    U: Clone + Debug,
{
```

这个函数的签名没那么杂乱：函数名、参数列表和返回类型靠得很近，类似于一个没有大量特性约束的函数。
