# 변수 바인딩

Rust 는 정적 타이핑을 통해 타입 안전성을 제공합니다. 변수 바인딩은 선언 시 타입을 주석으로 달 수 있습니다. 하지만 대부분의 경우 컴파일러는 컨텍스트로부터 변수의 타입을 추론할 수 있으므로 주석 부담을 크게 줄일 수 있습니다.

값 (예: 리터럴) 은 `let` 바인딩을 사용하여 변수에 바인딩될 수 있습니다.

```rust
fn main() {
    let an_integer = 1u32;
    let a_boolean = true;
    let unit = ();

    // `an_integer`를 `copied_integer`에 복사
    let copied_integer = an_integer;

    println!("An integer: {:?}", copied_integer);
    println!("A boolean: {:?}", a_boolean);
    println!("Meet the unit value: {:?}", unit);

    // 컴파일러는 사용되지 않은 변수 바인딩에 대한 경고를 표시합니다. 이 경고는 변수 이름 앞에 언더스코어를 붙여서 억제할 수 있습니다.
    let _unused_variable = 3u32;

    let noisy_unused_variable = 2u32;
    // FIXME ^ 경고를 억제하려면 언더스코어로 시작하세요.
    // 브라우저에서는 경고가 표시되지 않을 수 있습니다.
}
```
