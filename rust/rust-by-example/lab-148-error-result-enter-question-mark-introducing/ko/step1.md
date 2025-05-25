# `?` 소개

때로는 `panic`의 가능성 없이 `unwrap`의 단순함을 원할 때가 있습니다. 지금까지 `unwrap`은 우리가 실제로 변수를 _밖으로_ 가져오고 싶었을 때, 우리를 점점 더 깊이 중첩하게 만들었습니다. 이것이 바로 `?`의 목적입니다.

`Err`을 발견하면 두 가지 유효한 조치를 취할 수 있습니다.

1.  `panic!` (가능하면 피하려고 이미 결정했습니다)
2.  `return` ( `Err`은 처리할 수 없음을 의미하기 때문입니다)

`?`는 `Err`에서 `panic`하는 대신 `return`하는 `unwrap`과 _거의_\[\^†\] 정확히 동일합니다. 컴비네이터 (combinator) 를 사용했던 이전 예제를 어떻게 간소화할 수 있는지 살펴보겠습니다.

```rust
use std::num::ParseIntError;

fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    let first_number = first_number_str.parse::<i32>()?;
    let second_number = second_number_str.parse::<i32>()?;

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

## `try!` 매크로

`?`가 있기 전에는 `try!` 매크로로 동일한 기능을 구현했습니다. 이제 `?` 연산자가 권장되지만, 이전 코드를 볼 때 `try!`를 여전히 발견할 수 있습니다. 이전 예제의 동일한 `multiply` 함수는 `try!`를 사용하면 다음과 같습니다.

```rust
// To compile and run this example without errors, while using Cargo, change the value
// of the `edition` field, in the `[package]` section of the `Cargo.toml` file, to "2015".

use std::num::ParseIntError;

fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    let first_number = try!(first_number_str.parse::<i32>());
    let second_number = try!(second_number_str.parse::<i32>());

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
