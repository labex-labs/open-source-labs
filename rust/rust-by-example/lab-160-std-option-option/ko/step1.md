# `Option`

때로는 `panic!`을 호출하는 대신 프로그램의 일부 부분에서 실패를 감지하는 것이 바람직합니다. 이는 `Option` 열거형을 사용하여 수행할 수 있습니다.

`Option<T>` 열거형은 두 가지 변형을 갖습니다.

- `None`: 실패 또는 값의 부재를 나타내며,
- `Some(value)`: `T` 타입의 `value`를 감싸는 튜플 구조체입니다.

```rust
// `panic!` 하지 않는 정수 나눗셈
fn checked_division(dividend: i32, divisor: i32) -> Option<i32> {
    if divisor == 0 {
        // 실패는 `None` 변형으로 표현됩니다.
        None
    } else {
        // 결과는 `Some` 변형으로 감싸집니다.
        Some(dividend / divisor)
    }
}

// 이 함수는 성공하지 못할 수 있는 나눗셈을 처리합니다.
fn try_division(dividend: i32, divisor: i32) {
    // `Option` 값은 다른 열거형과 마찬가지로 패턴 매칭될 수 있습니다.
    match checked_division(dividend, divisor) {
        None => println!("{} / {} failed!", dividend, divisor),
        Some(quotient) => {
            println!("{} / {} = {}", dividend, divisor, quotient)
        },
    }
}

fn main() {
    try_division(4, 2);
    try_division(1, 0);

    // `None` 을 변수에 바인딩하려면 타입 어노테이션이 필요합니다.
    let none: Option<i32> = None;
    let _equivalent_none = None::<i32>;

    let optional_float = Some(0f32);

    // `Some` 변형을 언래핑하면 감싸진 값을 추출합니다.
    println!("{:?} unwraps to {:?}", optional_float, optional_float.unwrap());

    // `None` 변형을 언래핑하면 `panic!` 이 발생합니다.
    println!("{:?} unwraps to {:?}", none, none.unwrap());
}
```
