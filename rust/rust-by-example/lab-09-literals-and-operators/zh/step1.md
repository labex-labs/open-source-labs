# 字面量和运算符

整数 `1`、浮点数 `1.2`、字符 `'a'`、字符串 `"abc"`、布尔值 `true` 和单元类型 `()` 都可以使用字面量来表示。

整数也可以分别使用这些前缀，以十六进制、八进制或二进制表示法来表示：`0x`、`0o` 或 `0b`。

可以在数字字面量中插入下划线以提高可读性，例如 `1_000` 与 `1000` 相同，`0.000_001` 与 `0.000001` 相同。

Rust 还支持科学记数法，例如 `1e6`、`7.6e-4`。其关联类型为 `f64`。

我们需要告诉编译器我们使用的字面量的类型。目前，我们将使用 `u32` 后缀来表示该字面量是一个无符号 32 位整数，使用 `i32` 后缀来表示它是一个有符号 32 位整数。

Rust 中可用的运算符及其优先级与其他类 C 语言类似。

```rust
fn main() {
    // 整数加法
    println!("1 + 2 = {}", 1u32 + 2);

    // 整数减法
    println!("1 - 2 = {}", 1i32 - 2);
    // TODO ^ 尝试将 `1i32` 改为 `1u32`，看看为什么类型很重要

    // 科学记数法
    println!("1e4 是 {}, -2.5e-3 是 {}", 1e4, -2.5e-3);

    // 短路布尔逻辑
    println!("true AND false 是 {}", true && false);
    println!("true OR false 是 {}", true || false);
    println!("NOT true 是 {}",!true);

    // 位运算
    println!("0011 AND 0101 是 {:04b}", 0b0011u32 & 0b0101);
    println!("0011 OR 0101 是 {:04b}", 0b0011u32 | 0b0101);
    println!("0011 XOR 0101 是 {:04b}", 0b0011u32 ^ 0b0101);
    println!("1 << 5 是 {}", 1u32 << 5);
    println!("0x80 >> 2 是 0x{:x}", 0x80u32 >> 2);

    // 使用下划线提高可读性！
    println!("一百万写作 {}", 1_000_000u32);
}
```
