# `Result` 반복 처리

`Iter::map` 연산은 실패할 수 있습니다. 예를 들어:

```rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let numbers: Vec<_> = strings
        .into_iter()
        .map(|s| s.parse::<i32>())
        .collect();
    println!("Results: {:?}", numbers);
}
```

이 문제를 처리하기 위한 전략을 살펴보겠습니다.

## `filter_map()`을 사용하여 실패한 항목 무시하기

`filter_map`은 함수를 호출하고 `None`인 결과를 필터링합니다.

```rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let numbers: Vec<_> = strings
        .into_iter()
        .filter_map(|s| s.parse::<i32>().ok())
        .collect();
    println!("Results: {:?}", numbers);
}
```

## `map_err()` 및 `filter_map()`을 사용하여 실패한 항목 수집하기

`map_err`은 오류와 함께 함수를 호출하므로, 이전 `filter_map` 솔루션에 추가하여 반복 처리하는 동안 오류를 따로 저장할 수 있습니다.

```rust
fn main() {
    let strings = vec!["42", "tofu", "93", "999", "18"];
    let mut errors = vec![];
    let numbers: Vec<_> = strings
        .into_iter()
        .map(|s| s.parse::<u8>())
        .filter_map(|r| r.map_err(|e| errors.push(e)).ok())
        .collect();
    println!("Numbers: {:?}", numbers);
    println!("Errors: {:?}", errors);
}
```

## `collect()`를 사용하여 전체 연산 실패시키기

`Result`는 `FromIterator`를 구현하므로 결과 벡터 (`Vec<Result<T, E>>`) 를 벡터가 있는 결과 (`Result<Vec<T>, E>`) 로 변환할 수 있습니다. `Result::Err`이 발견되면 반복 처리가 종료됩니다.

```rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let numbers: Result<Vec<_>, _> = strings
        .into_iter()
        .map(|s| s.parse::<i32>())
        .collect();
    println!("Results: {:?}", numbers);
}
```

이와 동일한 기술을 `Option`과 함께 사용할 수 있습니다.

## `partition()`을 사용하여 모든 유효한 값과 실패를 수집하기

```rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let (numbers, errors): (Vec<_>, Vec<_>) = strings
        .into_iter()
        .map(|s| s.parse::<i32>())
        .partition(Result::is_ok);
    println!("Numbers: {:?}", numbers);
    println!("Errors: {:?}", errors);
}
```

결과를 보면 모든 것이 여전히 `Result`로 래핑되어 있음을 알 수 있습니다. 이를 위해서는 약간의 추가 보일러플레이트가 필요합니다.

```rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let (numbers, errors): (Vec<_>, Vec<_>) = strings
        .into_iter()
        .map(|s| s.parse::<i32>())
        .partition(Result::is_ok);
    let numbers: Vec<_> = numbers.into_iter().map(Result::unwrap).collect();
    let errors: Vec<_> = errors.into_iter().map(Result::unwrap_err).collect();
    println!("Numbers: {:?}", numbers);
    println!("Errors: {:?}", errors);
}
```
