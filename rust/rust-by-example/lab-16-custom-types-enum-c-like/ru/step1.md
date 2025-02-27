# C-подобные

`enum` также можно использовать как C-подобные перечисления.

```rust
// Аттрибут для скрытия предупреждений о неиспользуемом коде.
#![allow(dead_code)]

// Перечисление с неявным дискриминатором (начинается с 0)
enum Number {
    Zero,
    One,
    Two,
}

// Перечисление с явным дискриминатором
enum Color {
    Red = 0xff0000,
    Green = 0x00ff00,
    Blue = 0x0000ff,
}

fn main() {
    // `enum` можно преобразовать в целые числа.
    println!("zero is {}", Number::Zero as i32);
    println!("one is {}", Number::One as i32);

    println!("roses are #{:06x}", Color::Red as i32);
    println!("violets are #{:06x}", Color::Blue as i32);
}
```
