# 벡터 업데이트하기

벡터를 생성한 다음 요소를 추가하려면 Listing 8-3 에 표시된 대로 `push` 메서드를 사용할 수 있습니다.

```rust
let mut v = Vec::new();

v.push(5);
v.push(6);
v.push(7);
v.push(8);
```

Listing 8-3: `push` 메서드를 사용하여 벡터에 값 추가

다른 변수와 마찬가지로, 값을 변경할 수 있도록 하려면 3 장에서 설명한 대로 `mut` 키워드를 사용하여 가변 (mutable) 으로 만들어야 합니다. 안에 넣는 숫자는 모두 `i32` 타입이며, Rust 는 데이터에서 이를 추론하므로 `Vec<i32>` 어노테이션은 필요하지 않습니다.
