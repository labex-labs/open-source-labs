# `Result`

`Result`는 가능한 _부재_ 대신 가능한 *오류*를 설명하는 `Option` 타입의 더 풍부한 버전입니다.

즉, `Result<T, E>`는 두 가지 결과 중 하나를 가질 수 있습니다.

- `Ok(T)`: 요소 `T`가 발견되었습니다.
- `Err(E)`: 요소 `E`와 함께 오류가 발견되었습니다.

관례적으로, 예상되는 결과는 `Ok`이고 예상치 못한 결과는 `Err`입니다.

`Option`과 마찬가지로, `Result`는 많은 관련 메서드를 가지고 있습니다. 예를 들어, `unwrap()`는 요소 `T`를 반환하거나 `panic`을 발생시킵니다. 케이스 처리를 위해, `Result`와 `Option` 사이에 중복되는 많은 컴비네이터 (combinator) 가 있습니다.

Rust 를 사용하면서, `parse()` 메서드와 같이 `Result` 타입을 반환하는 메서드를 접하게 될 것입니다. 문자열을 다른 타입으로 파싱 (parsing) 하는 것이 항상 가능하지 않으므로, `parse()`는 실패 가능성을 나타내는 `Result`를 반환합니다.

문자열을 성공적으로 그리고 실패적으로 `parse()`하는 경우 어떻게 되는지 살펴보겠습니다.

```rust
fn multiply(first_number_str: &str, second_number_str: &str) -> i32 {
    // Let's try using `unwrap()` to get the number out. Will it bite us?
    let first_number = first_number_str.parse::<i32>().unwrap();
    let second_number = second_number_str.parse::<i32>().unwrap();
    first_number * second_number
}

fn main() {
    let twenty = multiply("10", "2");
    println!("double is {}", twenty);

    let tt = multiply("t", "2");
    println!("double is {}", tt);
}
```

실패한 경우, `parse()`는 `unwrap()`이 `panic`을 발생시킬 오류를 남깁니다. 또한, `panic`은 프로그램을 종료하고 불쾌한 오류 메시지를 제공합니다.

오류 메시지의 품질을 향상시키기 위해, 반환 타입에 대해 더 구체적으로 설명하고 오류를 명시적으로 처리하는 것을 고려해야 합니다.

## `main`에서 `Result` 사용하기

`Result` 타입은 명시적으로 지정된 경우 `main` 함수의 반환 타입이 될 수도 있습니다. 일반적으로 `main` 함수는 다음과 같은 형태를 가집니다.

```rust
fn main() {
    println!("Hello World!");
}
```

그러나 `main`은 `Result`의 반환 타입을 가질 수도 있습니다. `main` 함수 내에서 오류가 발생하면 오류 코드를 반환하고 오류의 디버그 표현 (\[`Debug`\] 트레이트를 사용하여) 을 출력합니다. 다음 예제는 이러한 시나리오를 보여주고 \[다음 섹션]에서 다루는 측면에 대해 언급합니다.

```rust
use std::num::ParseIntError;

fn main() -> Result<(), ParseIntError> {
    let number_str = "10";
    let number = match number_str.parse::<i32>() {
        Ok(number)  => number,
        Err(e) => return Err(e),
    };
    println!("{}", number);
    Ok(())
}
```
