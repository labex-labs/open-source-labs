# Enums

Ein `enum` wird ähnlich zerlegt:

```rust
// `allow` erforderlich, um Warnungen zu unterdrücken, da nur
// eine Variante verwendet wird.
#[allow(dead_code)]
enum Color {
    // Diese 3 werden ausschließlich durch ihren Namen angegeben.
    Red,
    Blue,
    Green,
    // Diese verbinden ebenfalls `u32`-Tupel mit verschiedenen Namen: Farbmodelle.
    RGB(u32, u32, u32),
    HSV(u32, u32, u32),
    HSL(u32, u32, u32),
    CMY(u32, u32, u32),
    CMYK(u32, u32, u32, u32),
}

fn main() {
    let color = Color::RGB(122, 17, 40);
    // TODO ^ Versuchen Sie verschiedene Varianten für `color`

    println!("What color is it?");
    // Ein `enum` kann mit einer `match` zerlegt werden.
    match color {
        Color::Red   => println!("The color is Red!"),
        Color::Blue  => println!("The color is Blue!"),
        Color::Green => println!("The color is Green!"),
        Color::RGB(r, g, b) =>
            println!("Red: {}, green: {}, and blue: {}!", r, g, b),
        Color::HSV(h, s, v) =>
            println!("Hue: {}, saturation: {}, value: {}!", h, s, v),
        Color::HSL(h, s, l) =>
            println!("Hue: {}, saturation: {}, lightness: {}!", h, s, l),
        Color::CMY(c, m, y) =>
            println!("Cyan: {}, magenta: {}, yellow: {}!", c, m, y),
        Color::CMYK(c, m, y, k) =>
            println!("Cyan: {}, magenta: {}, yellow: {}, key (black): {}!",
                c, m, y, k),
        // Es ist nicht erforderlich, einen weiteren Fall zu definieren, da alle Varianten überprüft wurden
    }
}
```
