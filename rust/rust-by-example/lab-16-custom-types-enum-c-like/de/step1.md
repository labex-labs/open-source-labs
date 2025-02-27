# C-ähnlich

`enum` kann auch als C-ähnliche Enums verwendet werden.

```rust
// Ein Attribut, um Warnungen für nicht genutzten Code zu unterdrücken.
#![allow(dead_code)]

// enum mit implizitem Diskriminator (beginnt bei 0)
enum Number {
    Zero,
    One,
    Two,
}

// enum mit explizitem Diskriminator
enum Color {
    Red = 0xff0000,
    Green = 0x00ff00,
    Blue = 0x0000ff,
}

fn main() {
    // `enums` können als Ganzzahlen umgewandelt werden.
    println!("zero is {}", Number::Zero as i32);
    println!("one is {}", Number::One as i32);

    println!("roses are #{:06x}", Color::Red as i32);
    println!("violets are #{:06x}", Color::Blue as i32);
}
```
