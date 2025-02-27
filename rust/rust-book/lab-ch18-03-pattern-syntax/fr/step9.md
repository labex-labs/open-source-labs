# Déconstruction de structs et d'enums imbriqués

Jusqu'à présent, nos exemples ont tous été des correspondances de structs ou d'enums à une seule profondeur, mais la correspondance peut également fonctionner sur des éléments imbriqués! Par exemple, nous pouvons refactoriser le code de la Liste 18-15 pour prendre en charge les couleurs RGB et HSV dans le message `ChangeColor`, comme montré dans la Liste 18-16.

Nom de fichier : `src/main.rs`

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

Liste 18-16 : Correspondance sur des enums imbriqués

Le motif du premier bras dans l'expression `match` correspond à une variante d'enum `Message::ChangeColor` qui contient une variante `Color::Rgb` ; puis le motif se lie aux trois valeurs `i32` internes. Le motif du second bras correspond également à une variante d'enum `Message::ChangeColor`, mais l'enum interne correspond à `Color::Hsv` à la place. Nous pouvons spécifier ces conditions complexes dans une seule expression `match`, même si deux enums sont impliqués.
