# 解构嵌套结构体和枚举

到目前为止，我们的示例都是对结构体或枚举进行一层深度的匹配，但匹配也可以用于嵌套项！例如，我们可以重构清单 18-15 中的代码，以在 `ChangeColor` 消息中支持 RGB 和 HSV 颜色，如清单 18-16 所示。

文件名：`src/main.rs`

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

清单 18-16：对嵌套枚举进行匹配

`match` 表达式中第一个分支的模式匹配一个包含 `Color::Rgb` 变体的 `Message::ChangeColor` 枚举变体；然后该模式绑定到三个内部的 `i32` 值。第二个分支的模式也匹配一个 `Message::ChangeColor` 枚举变体，但内部枚举匹配的是 `Color::Hsv`。即使涉及两个枚举，我们也可以在一个 `match` 表达式中指定这些复杂条件。
