# 作用域与遮蔽

变量绑定具有作用域，并且被限制在一个 _代码块_ 中。代码块是由花括号 `{}` 括起来的一组语句。

```rust
fn main() {
    // 这个绑定存在于main函数中
    let long_lived_binding = 1;

    // 这是一个代码块，其作用域比main函数小
    {
        // 这个绑定只存在于这个代码块中
        let short_lived_binding = 2;

        println!("内部短生命周期变量: {}", short_lived_binding);
    }
    // 代码块结束

    // 错误！`short_lived_binding` 在此作用域中不存在
    println!("外部短生命周期变量: {}", short_lived_binding);
    // FIXME ^ 注释掉这一行

    println!("外部长生命周期变量: {}", long_lived_binding);
}
```

此外，变量遮蔽是允许的。

```rust
fn main() {
    let shadowed_binding = 1;

    {
        println!("被遮蔽之前: {}", shadowed_binding);

        // 这个绑定 *遮蔽* 了外部的绑定
        let shadowed_binding = "abc";

        println!("在内部代码块中被遮蔽: {}", shadowed_binding);
    }
    println!("在内部代码块外部: {}", shadowed_binding);

    // 这个绑定 *遮蔽* 了之前的绑定
    let shadowed_binding = 2;
    println!("在外部代码块中被遮蔽: {}", shadowed_binding);
}
```
