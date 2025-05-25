# 벡터를 삭제하면 해당 요소도 삭제됩니다

다른 `struct`와 마찬가지로, Listing 8-10 에 주석으로 표시된 것처럼 벡터는 범위를 벗어날 때 해제됩니다.

```rust
{
    let v = vec![1, 2, 3, 4];

    // do stuff with v
} // <- v goes out of scope and is freed here
```

Listing 8-10: 벡터와 해당 요소가 삭제되는 위치 표시

벡터가 삭제되면 해당 내용도 모두 삭제됩니다. 즉, 벡터가 가지고 있는 정수가 정리됩니다. borrow checker 는 벡터 자체가 유효한 동안에만 벡터 내용에 대한 모든 참조가 사용되도록 보장합니다.

다음 컬렉션 타입인 `String`으로 넘어가 보겠습니다!
