# Strukturzerlegung geschachtelter Structs und Enums

Bisher haben unsere Beispiele alle nur auf Structs oder Enums eine Ebene tief abgestimmt, aber das Abgleichen funktioniert auch für geschachtelte Elemente! Beispielsweise können wir den Code in Listing 18-15 umgestalten, um RGB- und HSV-Farben in der `ChangeColor`-Nachricht zu unterstützen, wie in Listing 18-16 gezeigt.

Dateiname: `src/main.rs`

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
            "Farbe ändern zu rot {r}, grün {g} und blau {b}"
        ),
        Message::ChangeColor(Color::Hsv(h, s, v)) => println!(
            "Farbe ändern zu Farbton {h}, Sättigung {s}, Helligkeit {v}"
        ),
        _ => (),
    }
}
```

Listing 18-16: Abgleichen von geschachtelten Enums

Das Muster des ersten Arms im `match`-Ausdruck passt auf eine `Message::ChangeColor`-Enum-Variante, die eine `Color::Rgb`-Variante enthält; dann bindet das Muster an die drei inneren `i32`-Werte. Das Muster des zweiten Arms passt ebenfalls auf eine `Message::ChangeColor`-Enum-Variante, aber die innere Enum passt auf `Color::Hsv` statt dessen. Wir können diese komplexen Bedingungen in einem einzigen `match`-Ausdruck angeben, auch wenn zwei Enums beteiligt sind.
