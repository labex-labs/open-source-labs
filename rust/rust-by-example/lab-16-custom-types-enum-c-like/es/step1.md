# Similar a C

`enum` también se puede usar como enumeraiones en C.

```rust
// Un atributo para ocultar advertencias de código no utilizado.
#![allow(dead_code)]

// enum con discriminador implícito (empieza en 0)
enum Number {
    Zero,
    One,
    Two,
}

// enum con discriminador explícito
enum Color {
    Red = 0xff0000,
    Green = 0x00ff00,
    Blue = 0x0000ff,
}

fn main() {
    // Las `enums` se pueden convertir en enteros.
    println!("cero es {}", Number::Zero as i32);
    println!("uno es {}", Number::One as i32);

    println!("las rosas son #{:06x}", Color::Red as i32);
    println!("las violetas son #{:06x}", Color::Blue as i32);
}
```
