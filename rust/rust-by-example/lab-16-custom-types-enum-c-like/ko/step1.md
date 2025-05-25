# C 스타일

`enum`은 C 스타일 열거형으로도 사용할 수 있습니다.

```rust
// 사용하지 않는 코드에 대한 경고를 숨기는 속성입니다.
#![allow(dead_code)]

// 암시적 식별자 (0 부터 시작) 를 가진 enum
enum Number {
    Zero,
    One,
    Two,
}

// 명시적 식별자를 가진 enum
enum Color {
    Red = 0xff0000,
    Green = 0x00ff00,
    Blue = 0x0000ff,
}

fn main() {
    // `enums` 는 정수로 캐스팅될 수 있습니다.
    println!("zero is {}", Number::Zero as i32);
    println!("one is {}", Number::One as i32);

    println!("roses are #{:06x}", Color::Red as i32);
    println!("violets are #{:06x}", Color::Blue as i32);
}
```
