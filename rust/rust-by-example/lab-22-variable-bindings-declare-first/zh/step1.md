# 先声明

可以先声明变量绑定，之后再对其进行初始化。不过，这种形式很少使用，因为它可能会导致使用未初始化的变量。

```rust
fn main() {
    // 声明一个变量绑定
    let a_binding;

    {
        let x = 2;

        // 初始化该绑定
        a_binding = x * x;
    }

    println!("a binding: {}", a_binding);

    let another_binding;

    // 错误！使用了未初始化的绑定
    println!("another binding: {}", another_binding);
    // FIXME ^ 注释掉这一行

    another_binding = 1;

    println!("another binding: {}", another_binding);
}
```

编译器禁止使用未初始化的变量，因为这会导致未定义行为。
