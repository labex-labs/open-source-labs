# 가드

`match` *가드*를 추가하여 분기를 필터링할 수 있습니다.

```rust
#[allow(dead_code)]
enum Temperature {
    Celsius(i32),
    Fahrenheit(i32),
}

fn main() {
    let temperature = Temperature::Celsius(35);
    // ^ TODO `temperature` 의 다른 값을 시도해 보세요.

    match temperature {
        Temperature::Celsius(t) if t > 30 => println!("{}C 는 30 도 이상입니다", t),
        // ^ `if 조건` 부분이 가드입니다.
        Temperature::Celsius(t) => println!("{}C 는 30 도 미만입니다", t),

        Temperature::Fahrenheit(t) if t > 86 => println!("{}F 는 86 도 이상입니다", t),
        Temperature::Fahrenheit(t) => println!("{}F 는 86 도 미만입니다", t),
    }
}
```

컴파일러는 모든 패턴이 매치 표현식에 의해 커버되는지 확인할 때 가드 조건을 고려하지 않습니다.

```rust
fn main() {
    let number: u8 = 4;

    match number {
        i if i == 0 => println!("Zero"),
        i if i > 0 => println!("Zero 보다 큽니다"),
        // _ => unreachable!("Should never happen."),
        // TODO ^ 컴파일 오류를 해결하려면 주석을 해제하세요.
    }
}
```
