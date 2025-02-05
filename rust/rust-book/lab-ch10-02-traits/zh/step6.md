# 特性约束语法

`impl Trait` 语法在简单的情况下可以正常工作，但实际上它是一种更冗长形式的语法糖，这种冗长形式被称为「特性约束」；它看起来像这样：

```rust
pub fn notify<T: Summary>(item: &T) {
    println!("Breaking news! {}", item.summarize());
}
```

这种更冗长的形式与上一节中的示例等效，但更啰嗦。我们在冒号后和尖括号内，与泛型类型参数的声明一起放置特性约束。

`impl Trait` 语法很方便，在简单的情况下能使代码更简洁，而完整的特性约束语法在其他情况下可以表达更复杂的情况。例如，我们可以有两个实现了 `Summary` 的参数。使用 `impl Trait` 语法时看起来像这样：

```rust
pub fn notify(item1: &impl Summary, item2: &impl Summary) {
```

如果我们希望这个函数允许 `item1` 和 `item2` 具有不同的类型（只要这两种类型都实现了 `Summary`），那么使用 `impl Trait` 是合适的。然而，如果我们想强制两个参数具有相同的类型，那么我们必须使用特性约束，如下所示：

```rust
pub fn notify<T: Summary>(item1: &T, item2: &T) {
```

指定为 `item1` 和 `item2` 参数类型的泛型类型 `T` 对函数进行了约束，使得作为 `item1` 和 `item2` 参数传递的值的具体类型必须相同。
