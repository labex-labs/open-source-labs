# 먼저 선언하기

변수 바인딩을 먼저 선언하고 나중에 초기화하는 것이 가능하지만, 초기화되지 않은 변수를 사용할 수 있으므로 이 형태는 거의 사용되지 않습니다.

```rust
fn main() {
    // 변수 바인딩을 선언합니다.
    let a_binding;

    {
        let x = 2;

        // 바인딩을 초기화합니다.
        a_binding = x * x;
    }

    println!("a binding: {}", a_binding);

    let another_binding;

    // 오류! 초기화되지 않은 바인딩 사용
    println!("another binding: {}", another_binding);
    // FIXME ^ 이 줄을 주석 처리하세요

    another_binding = 1;

    println!("another binding: {}", another_binding);
}
```

컴파일러는 초기화되지 않은 변수 사용을 금지합니다. 이는 정의되지 않은 동작을 초래하기 때문입니다.
