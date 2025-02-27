# enum

Un `enum` se desestructura de manera similar:

```rust
// `allow` es necesario para silenciar advertencias porque solo
// se utiliza una variante.
#[allow(dead_code)]
enum Color {
    // Estas 3 se especifican solo por su nombre.
    Red,
    Blue,
    Green,
    // Estas igualmente asocian tuplas `u32` con diferentes nombres: modelos de color.
    RGB(u32, u32, u32),
    HSV(u32, u32, u32),
    HSL(u32, u32, u32),
    CMY(u32, u32, u32),
    CMYK(u32, u32, u32, u32),
}

fn main() {
    let color = Color::RGB(122, 17, 40);
    // TODO ^ Prueba diferentes variantes para `color`

    println!("¿Qué color es?");
    // Un `enum` se puede desestructurar utilizando una `match`.
    match color {
        Color::Red   => println!("El color es Rojo!"),
        Color::Blue  => println!("El color es Azul!"),
        Color::Green => println!("El color es Verde!"),
        Color::RGB(r, g, b) =>
            println!("Rojo: {}, verde: {}, y azul: {}!", r, g, b),
        Color::HSV(h, s, v) =>
            println!("Matiz: {}, saturación: {}, valor: {}!", h, s, v),
        Color::HSL(h, s, l) =>
            println!("Matiz: {}, saturación: {}, luminosidad: {}!", h, s, l),
        Color::CMY(c, m, y) =>
            println!("Cian: {}, magenta: {}, amarillo: {}!", c, m, y),
        Color::CMYK(c, m, y, k) =>
            println!("Cian: {}, magenta: {}, amarillo: {}, clave (negro): {}!",
                c, m, y, k),
        // No es necesario otro brazo porque todas las variantes han sido examinadas
    }
}
```
