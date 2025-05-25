# 문자열 변환

## 문자열로 변환

어떤 타입이든 `String`으로 변환하려면 해당 타입에 [`ToString`] 트레이트를 구현하는 것만큼 간단합니다. 직접 구현하는 대신 `fmt::Display` 트레이트를 구현하는 것이 좋습니다. `fmt::Display` 트레이트는 자동으로 [`ToString`] 트레이트를 제공하고 `print!` 섹션에서 논의된 것처럼 타입을 출력할 수 있도록 합니다.

```rust
use std::fmt;

struct Circle {
    radius: i32
}

impl fmt::Display for Circle {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "반지름이 {}인 원", self.radius)
    }
}

fn main() {
    let circle = Circle { radius: 6 };
    println!("{}", circle.to_string());
}
```

## 문자열 구문 분석

문자열을 숫자로 변환하는 가장 일반적인 유형 중 하나입니다. 이를 위한 표준적인 방법은 [`parse`] 함수를 사용하고 타입 추론을 사용하거나 'turbofish' 구문을 사용하여 변환할 타입을 명시적으로 지정하는 것입니다. 두 가지 방법 모두 다음 예제에서 보여줍니다.

이렇게 하면 해당 타입에 [`FromStr`] 트레이트가 구현되어 있는 한 문자열을 지정된 타입으로 변환합니다. 이는 표준 라이브러리 내의 여러 타입에 대해 구현되어 있습니다. 사용자 정의 타입에 대해 이 기능을 얻으려면 해당 타입에 [`FromStr`] 트레이트를 구현하면 됩니다.

```rust
fn main() {
    let parsed: i32 = "5".parse().unwrap();
    let turbo_parsed = "10".parse::<i32>().unwrap();

    let sum = parsed + turbo_parsed;
    println!("합계: {:?}", sum);
}
```
