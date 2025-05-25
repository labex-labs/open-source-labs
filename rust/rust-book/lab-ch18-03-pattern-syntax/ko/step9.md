# 중첩된 구조체 및 열거형 디스트럭처링 (Destructuring Nested Structs and Enums)

지금까지의 예제는 모두 구조체 또는 열거형을 한 단계 깊이로 매칭했지만, 매칭은 중첩된 항목에서도 작동할 수 있습니다! 예를 들어, Listing 18-15 의 코드를 리팩터링하여 Listing 18-16 과 같이 `ChangeColor` 메시지에서 RGB 및 HSV 색상을 지원할 수 있습니다.

파일 이름: `src/main.rs`

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

Listing 18-16: 중첩된 열거형 매칭

`match` 표현식의 첫 번째 arm 의 패턴은 `Color::Rgb` 변형을 포함하는 `Message::ChangeColor` 열거형 변형과 일치합니다. 그런 다음 패턴은 세 개의 내부 `i32` 값에 바인딩됩니다. 두 번째 arm 의 패턴도 `Message::ChangeColor` 열거형 변형과 일치하지만 내부 열거형은 대신 `Color::Hsv`와 일치합니다. 두 개의 열거형이 관련되어 있더라도 이러한 복잡한 조건을 하나의 `match` 표현식으로 지정할 수 있습니다.
