# C 言語風

`enum` は C 言語風の列挙型としても使用できます。

```rust
// 未使用のコードに対する警告を非表示にする属性
#![allow(dead_code)]

// 暗黙的な識別子付きの列挙型 (0 から始まる)
enum Number {
    Zero,
    One,
    Two,
}

// 明示的な識別子付きの列挙型
enum Color {
    Red = 0xff0000,
    Green = 0x00ff00,
    Blue = 0x0000ff,
}

fn main() {
    // `enum` を整数にキャストできます。
    println!("zero is {}", Number::Zero as i32);
    println!("one is {}", Number::One as i32);

    println!("roses are #{:06x}", Color::Red as i32);
    println!("violets are #{:06x}", Color::Blue as i32);
}
```
