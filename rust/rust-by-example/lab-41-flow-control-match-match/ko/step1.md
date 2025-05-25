# match

Rust 는 `match` 키워드를 통해 패턴 매칭을 제공하며, 이는 C 의 `switch`와 유사하게 사용할 수 있습니다. 첫 번째 일치하는 팔 (arm) 이 평가되며 모든 가능한 값은 커버되어야 합니다.

```rust
fn main() {
    let number = 13;
    // TODO ^ `number` 에 다른 값을 시도해 보세요.

    println!("Tell me about {}", number);
    match number {
        // 단일 값 일치
        1 => println!("One!"),
        // 여러 값 일치
        2 | 3 | 5 | 7 | 11 => println!("This is a prime"),
        // TODO ^ 소수 값 목록에 13 을 추가해 보세요.
        // 범위 일치 (포함)
        13..=19 => println!("A teen"),
        // 나머지 경우 처리
        _ => println!("Ain't special"),
        // TODO ^ 이 catch-all arm 을 주석 처리해 보세요.
    }

    let boolean = true;
    // match 는 표현식이기도 합니다.
    let binary = match boolean {
        // match 의 팔 (arm) 은 모든 가능한 값을 커버해야 합니다.
        false => 0,
        true => 1,
        // TODO ^ 이 중 하나의 arm 을 주석 처리해 보세요.
    };

    println!("{} -> {}", boolean, binary);
}
```
