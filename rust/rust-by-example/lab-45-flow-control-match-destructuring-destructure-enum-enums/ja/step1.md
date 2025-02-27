# 列挙型

`enum` も同様に分解されます。

```rust
// 1つのバリアントのみが使用されるため、警告を抑制するために `allow` が必要です。
#[allow(dead_code)]
enum Color {
    // これら3つは名前のみで指定されます。
    Red,
    Blue,
    Green,
    // これらは同様に `u32` のタプルを異なる名前（カラーモデル）に紐付けます。
    RGB(u32, u32, u32),
    HSV(u32, u32, u32),
    HSL(u32, u32, u32),
    CMY(u32, u32, u32),
    CMYK(u32, u32, u32, u32),
}

fn main() {
    let color = Color::RGB(122, 17, 40);
    // TODO ^ `color` に対して異なるバリアントを試してみてください

    println!("What color is it?");
    // `enum` は `match` を使って分解できます。
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
        // すべてのバリアントが検査されたため、別のアームは不要です
    }
}
```
