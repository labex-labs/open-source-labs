# 使用 + 语法指定多个特性约束

我们还可以指定多个特性约束。假设我们希望 `notify` 对 `item` 既使用 `summarize` 方法，又使用显示格式化功能：我们在 `notify` 定义中指定 `item` 必须同时实现 `Display` 和 `Summary`。我们可以使用 `+` 语法来做到这一点：

```rust
pub fn notify(item: &(impl Summary + Display)) {
```

`+` 语法在泛型类型的特性约束中同样有效：

```rust
pub fn notify<T: Summary + Display>(item: &T) {
```

指定了这两个特性约束后，`notify` 的函数体就可以调用 `summarize` 并使用 `{}` 来格式化 `item`。
