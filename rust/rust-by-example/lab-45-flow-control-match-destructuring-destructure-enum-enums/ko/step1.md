# 열거형 (enums)

`enum`도 비슷하게 분해됩니다.

```rust
// 경고를 무시하기 위해 `allow` 가 필요합니다.
// 단 하나의 변형만 사용되기 때문입니다.
#[allow(dead_code)]
enum Color {
    // 이 3 가지는 이름만으로 지정됩니다.
    Red,
    Blue,
    Green,
    // 이들 역시 `u32` 튜플을 다른 이름 (색상 모델) 과 연결합니다.
    RGB(u32, u32, u32),
    HSV(u32, u32, u32),
    HSL(u32, u32, u32),
    CMY(u32, u32, u32),
    CMYK(u32, u32, u32, u32),
}

fn main() {
    let color = Color::RGB(122, 17, 40);
    // TODO ^ `color` 에 다른 변형을 시도해 보세요.

    println!("어떤 색상인가요?");
    // `enum` 은 `match` 를 사용하여 분해할 수 있습니다.
    match color {
        Color::Red   => println!("색상은 빨강입니다!"),
        Color::Blue  => println!("색상은 파랑입니다!"),
        Color::Green => println!("색상은 초록입니다!"),
        Color::RGB(r, g, b) =>
            println!("빨강: {}, 초록: {}, 파랑: {}!", r, g, b),
        Color::HSV(h, s, v) =>
            println!("색조: {}, 채도: {}, 명도: {}!", h, s, v),
        Color::HSL(h, s, l) =>
            println!("색조: {}, 채도: {}, 밝기: {}!", h, s, l),
        Color::CMY(c, m, y) =>
            println!("청록: {}, 마젠타: {}, 노랑: {}!", c, m, y),
        Color::CMYK(c, m, y, k) =>
            println!("청록: {}, 마젠타: {}, 노랑: {}, 검정: {}!",
                c, m, y, k),
        // 모든 변형을 검사했으므로 다른 분기는 필요하지 않습니다.
    }
}
```
