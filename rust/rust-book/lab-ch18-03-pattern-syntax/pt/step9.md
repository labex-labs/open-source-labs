# Desestruturando Structs e Enums Aninhados

Até agora, nossos exemplos têm correspondido a structs ou enums em um nível de profundidade, mas a correspondência pode funcionar em itens aninhados também! Por exemplo, podemos refatorar o código na Listagem 18-15 para suportar cores RGB e HSV na mensagem `ChangeColor`, conforme mostrado na Listagem 18-16.

Nome do arquivo: `src/main.rs`

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

Listagem 18-16: Correspondência em enums aninhados

O padrão do primeiro braço na expressão `match` corresponde a uma variante de enum `Message::ChangeColor` que contém uma variante `Color::Rgb`; então o padrão se vincula aos três valores `i32` internos. O padrão do segundo braço também corresponde a uma variante de enum `Message::ChangeColor`, mas o enum interno corresponde a `Color::Hsv` em vez disso. Podemos especificar essas condições complexas em uma expressão `match`, mesmo que dois enums estejam envolvidos.
