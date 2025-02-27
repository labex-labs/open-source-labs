# ネストされた構造体と列挙型の分解

これまでの例では、すべて1段階深い構造体や列挙型をマッチさせてきましたが、ネストされた項目に対してもマッチングが機能します！ たとえば、リスト18-15のコードをリファクタリングして、`ChangeColor` メッセージにRGBとHSVの色をサポートするようにします。これはリスト18-16に示されています。

ファイル名: `src/main.rs`

```rust
enum Color {
    Rgb(i32, i32, i32),
    Hsv(i32, i32, i32),
}

enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(Color),
}

fn main() {
    let msg = Message::ChangeColor(Color::Hsv(0, 160, 255));

    match msg {
        Message::ChangeColor(Color::Rgb(r, g, b)) => println!(
            "Change color to red {r}, green {g}, and blue {b}"
        ),
        Message::ChangeColor(Color::Hsv(h, s, v)) => println!(
            "Change color to hue {h}, saturation {s}, value {v}"
        ),
        _ => (),
    }
}
```

リスト18-16: ネストされた列挙型のマッチング

`match` 式の最初のアームのパターンは、`Color::Rgb` バリアントを含む `Message::ChangeColor` 列挙型のバリアントとマッチします。その後、パターンは内部の3つの `i32` 値にバインドされます。2番目のアームのパターンも `Message::ChangeColor` 列挙型のバリアントとマッチしますが、内部の列挙型は代わりに `Color::Hsv` とマッチします。2つの列挙型が関係しているにもかかわらず、これらの複雑な条件を1つの `match` 式で指定することができます。