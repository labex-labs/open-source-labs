# 상수

Rust 에는 전역 범위를 포함한 모든 범위에서 선언할 수 있는 두 가지 유형의 상수가 있습니다. 두 가지 유형 모두 명시적인 타입 주석이 필요합니다.

- `const`: 변경할 수 없는 값 (일반적인 경우).
- `static`: `'static` 수명을 가진, 가능하게는 `mut`able 변수. static 수명은 추론되며 명시할 필요가 없습니다. 가변 static 변수에 접근하거나 수정하는 것은 `unsafe`입니다.

```rust
// 전역 변수는 다른 모든 범위 외부에 선언됩니다.
static LANGUAGE: &str = "Rust";
const THRESHOLD: i32 = 10;

fn is_big(n: i32) -> bool {
    // 어떤 함수에서 상수에 접근
    n > THRESHOLD
}

fn main() {
    let n = 16;

    // 메인 스레드에서 상수에 접근
    println!("이것은 {}", LANGUAGE);
    println!("임계값은 {}", THRESHOLD);
    println!("{}는 {}", n, if is_big(n) { "크다" } else { "작다" });

    // 오류! `const` 는 수정할 수 없습니다.
    THRESHOLD = 5;
    // FIXME ^ 이 줄을 주석 처리하세요
}
```
