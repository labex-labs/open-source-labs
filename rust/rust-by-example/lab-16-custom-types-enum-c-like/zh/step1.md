# 类似 C 语言的用法

`enum` 也可以用作类似 C 语言的枚举。

```rust
// 用于隐藏未使用代码警告的属性。
#![allow(dead_code)]

// 带有隐式判别器的枚举（从 0 开始）
enum Number {
    Zero,
    One,
    Two,
}

// 带有显式判别器的枚举
enum Color {
    Red = 0xff0000,
    Green = 0x00ff00,
    Blue = 0x0000ff,
}

fn main() {
    // `enums` 可以转换为整数。
    println!("zero is {}", Number::Zero as i32);
    println!("one is {}", Number::One as i32);

    println!("roses are #{:06x}", Color::Red as i32);
    println!("violets are #{:06x}", Color::Blue as i32);
}
```
