# C-like

`enum` peut également être utilisé comme des énumérations C.

```rust
// Un attribut pour masquer les avertissements pour le code inutilisé.
#![allow(dead_code)]

// enum avec discriminateur implicite (commence à 0)
enum Number {
    Zero,
    One,
    Two,
}

// enum avec discriminateur explicite
enum Color {
    Red = 0xff0000,
    Green = 0x00ff00,
    Blue = 0x0000ff,
}

fn main() {
    // Les `enums` peuvent être converties en entiers.
    println!("zero is {}", Number::Zero as i32);
    println!("one is {}", Number::One as i32);

    println!("roses are #{:06x}", Color::Red as i32);
    println!("violets are #{:06x}", Color::Blue as i32);
}
```
