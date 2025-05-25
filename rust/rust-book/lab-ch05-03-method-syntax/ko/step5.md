# 여러 impl 블록

각 구조체는 여러 개의 `impl` 블록을 가질 수 있습니다. 예를 들어, Listing 5-15 는 Listing 5-16 에 표시된 코드와 동일하며, 각 메서드가 자체 `impl` 블록에 있습니다.

```rust
impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
}

impl Rectangle {
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}
```

Listing 5-16: 여러 `impl` 블록을 사용하여 Listing 5-15 다시 작성하기

여기서는 이러한 메서드를 여러 `impl` 블록으로 분리할 이유가 없지만, 이것은 유효한 구문입니다. 제네릭 타입 (generic types) 과 트레이트 (traits) 에 대해 논의하는 챕터 10 에서 여러 `impl` 블록이 유용한 경우를 보게 될 것입니다.
