# 가변성 (Mutability)

변수 바인딩은 기본적으로 불변 (immutable) 입니다. 하지만 `mut` 수정자를 사용하여 이를 변경할 수 있습니다.

```rust
fn main() {
    let _immutable_binding = 1;
    let mut mutable_binding = 1;

    println!("변경 전: {}", mutable_binding);

    // 정상 동작
    mutable_binding += 1;

    println!("변경 후: {}", mutable_binding);

    // 오류! 불변 변수에 새로운 값을 할당할 수 없습니다.
    _immutable_binding += 1;
}
```

컴파일러는 가변성 오류에 대한 자세한 진단 메시지를 출력합니다.
