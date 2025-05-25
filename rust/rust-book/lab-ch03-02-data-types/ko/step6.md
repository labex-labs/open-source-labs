# 부울린 타입 (The Boolean Type)

대부분의 다른 프로그래밍 언어와 마찬가지로, Rust 의 부울린 타입은 두 가지 가능한 값, 즉 `true`와 `false`를 가집니다. 부울린은 크기가 1 바이트입니다. Rust 의 부울린 타입은 `bool`을 사용하여 지정됩니다. 예를 들어:

파일 이름: `src/main.rs`

```rust
fn main() {
    let t = true;

    let f: bool = false; // 명시적 타입 어노테이션 (explicit type annotation)
}
```

부울린 값을 사용하는 주요 방법은 `if` 표현식과 같은 조건문을 통하는 것입니다. "제어 흐름 (Control Flow)"에서 Rust 의 `if` 표현식이 어떻게 작동하는지 다룰 것입니다.
