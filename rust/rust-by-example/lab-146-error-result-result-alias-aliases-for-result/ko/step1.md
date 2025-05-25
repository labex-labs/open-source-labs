# `Result`에 대한 별칭 (aliases)

특정 `Result` 타입을 여러 번 재사용하고 싶을 때는 어떻게 해야 할까요? Rust 에서는 별칭을 생성할 수 있다는 것을 기억하세요. 편리하게도, 문제의 특정 `Result`에 대한 별칭을 정의할 수 있습니다.

모듈 수준에서 별칭을 생성하는 것은 특히 유용할 수 있습니다. 특정 모듈에서 발견된 오류는 종종 동일한 `Err` 타입을 가지므로, 단일 별칭으로 _모든_ 관련 `Result`를 간결하게 정의할 수 있습니다. 이는 매우 유용하여 `std` 라이브러리에서도 `io::Result`를 제공합니다!

다음은 구문을 보여주는 간단한 예시입니다.

```rust
use std::num::ParseIntError;

// 오류 타입이 `ParseIntError` 인 `Result` 에 대한 일반적인 별칭을 정의합니다.
type AliasedResult<T> = Result<T, ParseIntError>;

// 위 별칭을 사용하여 특정 `Result` 타입을 참조합니다.
fn multiply(first_number_str: &str, second_number_str: &str) -> AliasedResult<i32> {
    first_number_str.parse::<i32>().and_then(|first_number| {
        second_number_str.parse::<i32>().map(|second_number| first_number * second_number)
    })
}

// 여기에서 별칭은 다시 공간을 절약할 수 있게 해줍니다.
fn print(result: AliasedResult<i32>) {
    match result {
        Ok(n)  => println!("n is {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    print(multiply("10", "2"));
    print(multiply("t", "2"));
}
```
