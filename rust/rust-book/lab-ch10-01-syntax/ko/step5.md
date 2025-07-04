# 열거형 정의에서

구조체와 마찬가지로, 열거형 (enum) 을 정의하여 변형 (variant) 에서 제네릭 데이터 타입을 저장할 수 있습니다. 6 장에서 사용했던 표준 라이브러리가 제공하는 `Option<T>` 열거형을 다시 살펴보겠습니다.

```rust
enum Option<T> {
    Some(T),
    None,
}
```

이제 이 정의가 더 이해가 될 것입니다. 보시다시피, `Option<T>` 열거형은 타입 `T`에 대해 제네릭이며 두 개의 변형을 갖습니다: 타입 `T`의 값을 하나 갖는 `Some`과 어떤 값도 갖지 않는 `None` 변형입니다. `Option<T>` 열거형을 사용함으로써, 선택적 값 (optional value) 의 추상적인 개념을 표현할 수 있으며, `Option<T>`가 제네릭이기 때문에 선택적 값의 타입이 무엇이든 이 추상화를 사용할 수 있습니다.

열거형은 여러 제네릭 타입을 사용할 수도 있습니다. 9 장에서 사용했던 `Result` 열거형의 정의가 그 예입니다.

```rust
enum Result<T, E> {
    Ok(T),
    Err(E),
}
```

`Result` 열거형은 두 개의 타입, `T`와 `E`에 대해 제네릭이며 두 개의 변형을 갖습니다: 타입 `T`의 값을 갖는 `Ok`와 타입 `E`의 값을 갖는 `Err`입니다. 이 정의는 성공할 수 있거나 (어떤 타입 `T`의 값을 반환) 실패할 수 있는 (어떤 타입 `E`의 오류를 반환) 연산이 있는 곳에서 `Result` 열거형을 편리하게 사용할 수 있도록 합니다. 실제로, 이것은 9-3 Listing 에서 파일을 열 때 사용했던 것으로, 파일이 성공적으로 열렸을 때 `T`는 `std::fs::File` 타입으로 채워지고, 파일을 여는 데 문제가 있을 때는 `E`가 `std::io::Error` 타입으로 채워졌습니다.

코드에서 여러 구조체 또는 열거형 정의가 있고, 그들이 저장하는 값의 타입만 다른 상황을 인식하면, 제네릭 타입을 사용하여 중복을 피할 수 있습니다.
