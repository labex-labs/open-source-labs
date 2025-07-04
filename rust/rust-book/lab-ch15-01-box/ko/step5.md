# 비재귀적 타입의 크기 계산

6 장에서 enum 정의에 대해 논의했을 때 Listing 6-2 에서 정의한 `Message` enum 을 기억하십시오:

```rust
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}
```

`Message` 값에 할당할 공간의 크기를 결정하기 위해 Rust 는 각 변형을 거쳐 어떤 변형이 가장 많은 공간을 필요로 하는지 확인합니다. Rust 는 `Message::Quit`이 어떤 공간도 필요로 하지 않고, `Message::Move`는 두 개의 `i32` 값을 저장할 공간이 필요하며, 기타 등등을 확인합니다. 하나의 변형만 사용되므로, `Message` 값이 필요로 하는 최대 공간은 가장 큰 변형을 저장하는 데 필요한 공간입니다.

Listing 15-2 의 `List` enum 과 같은 재귀적 타입이 필요로 하는 공간의 크기를 Rust 가 결정하려고 할 때 발생하는 상황과 대조해 보십시오. 컴파일러는 `Cons` 변형을 먼저 살펴봅니다. 이 변형은 `i32` 타입의 값과 `List` 타입의 값을 저장합니다. 따라서 `Cons`는 `i32`의 크기 더하기 `List`의 크기와 같은 양의 공간이 필요합니다. `List` 타입이 얼마나 많은 메모리를 필요로 하는지 파악하기 위해 컴파일러는 `Cons` 변형부터 시작하여 변형을 살펴봅니다. `Cons` 변형은 `i32` 타입의 값과 `List` 타입의 값을 저장하며, 이 과정은 그림 15-1 에 표시된 것처럼 무한히 계속됩니다.

그림 15-1: 무한한 `Cons` 변형으로 구성된 무한한 `List`
