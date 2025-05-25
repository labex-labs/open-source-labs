# 조기 반환 (Early returns)

이전 예제에서는 컴비네이터 (combinators) 를 사용하여 오류를 명시적으로 처리했습니다. 이 경우 분석을 처리하는 또 다른 방법은 `match` 문과 *조기 반환*을 함께 사용하는 것입니다.

즉, 오류가 발생하면 함수 실행을 중단하고 오류를 반환할 수 있습니다. 어떤 사람들에게는 이 형태의 코드가 읽고 쓰기 더 쉬울 수 있습니다. 조기 반환을 사용하여 다시 작성된 이전 예제를 살펴보겠습니다.

```rust
use std::num::ParseIntError;

fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    let first_number = match first_number_str.parse::<i32>() {
        Ok(first_number)  => first_number,
        Err(e) => return Err(e),
    };

    let second_number = match second_number_str.parse::<i32>() {
        Ok(second_number)  => second_number,
        Err(e) => return Err(e),
    };

    Ok(first_number * second_number)
}

fn print(result: Result<i32, ParseIntError>) {
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

이 시점에서 우리는 컴비네이터와 조기 반환을 사용하여 오류를 명시적으로 처리하는 방법을 배웠습니다. 일반적으로 패닉 (panicking) 을 피하고 싶지만, 모든 오류를 명시적으로 처리하는 것은 번거롭습니다.

다음 섹션에서는 `panic`을 유발할 가능성 없이 단순히 `unwrap`해야 하는 경우를 위해 `?`를 소개합니다.
