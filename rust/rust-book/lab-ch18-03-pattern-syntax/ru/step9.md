# Деструктуризация вложенных структур и перечислений (Destructuring Nested Structs and Enums)

До сих пор наши примеры были связаны с сопоставлением структур или перечислений на одном уровне, но сопоставление может работать и с вложенными элементами! Например, мы можем переписать код из листинга 18 - 15 так, чтобы он поддерживал цвета в формате RGB и HSV в сообщении `ChangeColor`, как показано в листинге 18 - 16.

Имя файла: `src/main.rs`

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

Листинг 18 - 16: Сопоставление вложенных перечислений

Шаблон первой ветки в выражении `match` соответствует варианту перечисления `Message::ChangeColor`, который содержит вариант `Color::Rgb`; затем шаблон связывается с тремя внутренними значениями типа `i32`. Шаблон второй ветки также соответствует варианту перечисления `Message::ChangeColor`, но внутреннее перечисление соответствует `Color::Hsv`. Мы можем задать эти сложные условия в одном выражении `match`, даже если участвуют два перечисления.
