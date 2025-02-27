# ネストされた構造体と列挙型のデストラクチャリング

これまでの例では、構造体や列挙型を 1 レベル深さでマッチさせてきましたが、マッチングはネストされた要素にも適用できます！ たとえば、リスト 18-15 のコードをリファクタリングして、`ChangeColor` メッセージで RGB と HSV の色をサポートすることができます。これをリスト 18-16 に示します。

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

リスト 18-16: ネストされた列挙型に対するマッチング

`match` 式の最初のアームのパターンは、`Color::Rgb` バリアントを含む `Message::ChangeColor` 列挙型のバリアントにマッチします。その後、パターンは内部の 3 つの `i32` 値にバインドされます。2 番目のアームのパターンも `Message::ChangeColor` 列挙型のバリアントにマッチしますが、内部の列挙型は `Color::Hsv` にマッチします。2 つの列挙型が関与している場合でも、これらの複雑な条件を 1 つの `match` 式で指定することができます。
