# 可变性

默认情况下，变量绑定是不可变的，但可以使用 `mut` 修饰符来覆盖此行为。

```rust
fn main() {
    let _immutable_binding = 1;
    let mut mutable_binding = 1;

    println!("Before mutation: {}", mutable_binding);

    // 没问题
    mutable_binding += 1;

    println!("After mutation: {}", mutable_binding);

    // 错误！不能给不可变变量赋新值
    _immutable_binding += 1;
}
```

编译器会抛出有关可变性错误的详细诊断信息。
