# `Result`에 대한 `map`

이전 예제의 `multiply`에서 패닉 (panicking) 하는 것은 견고한 코드를 만들지 못합니다. 일반적으로 오류에 적절하게 대응하는 방법을 결정할 수 있도록 오류를 호출자에게 반환하려고 합니다.

먼저 어떤 종류의 오류 타입 (error type) 을 다루고 있는지 알아야 합니다. `Err` 타입을 결정하기 위해 `i32`에 대해 `FromStr` 트레이트 (trait) 로 구현된 `parse()`를 살펴봅니다. 결과적으로 `Err` 타입은 `ParseIntError`로 지정됩니다.

아래 예제에서 간단한 `match` 문은 전체적으로 더 번거로운 코드로 이어집니다.

```rust
use std::num::ParseIntError;

// With the return type rewritten, we use pattern matching without `unwrap()`.
fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    match first_number_str.parse::<i32>() {
        Ok(first_number)  => {
            match second_number_str.parse::<i32>() {
                Ok(second_number)  => {
                    Ok(first_number * second_number)
                },
                Err(e) => Err(e),
            }
        },
        Err(e) => Err(e),
    }
}

fn print(result: Result<i32, ParseIntError>) {
    match result {
        Ok(n)  => println!("n is {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    // This still presents a reasonable answer.
    let twenty = multiply("10", "2");
    print(twenty);

    // The following now provides a much more helpful error message.
    let tt = multiply("t", "2");
    print(tt);
}
```

다행히 `Option`의 `map`, `and_then` 및 기타 많은 콤비네이터 (combinator) 가 `Result`에도 구현되어 있습니다. `Result`에는 전체 목록이 포함되어 있습니다.

```rust
use std::num::ParseIntError;

// As with `Option`, we can use combinators such as `map()`.
// This function is otherwise identical to the one above and reads:
// Multiply if both values can be parsed from str, otherwise pass on the error.
fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    first_number_str.parse::<i32>().and_then(|first_number| {
        second_number_str.parse::<i32>().map(|second_number| first_number * second_number)
    })
}

fn print(result: Result<i32, ParseIntError>) {
    match result {
        Ok(n)  => println!("n is {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    // This still presents a reasonable answer.
    let twenty = multiply("10", "2");
    print(twenty);

    // The following now provides a much more helpful error message.
    let tt = multiply("t", "2");
    print(tt);
}
```
