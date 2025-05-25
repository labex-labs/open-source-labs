# 배열 요소 접근 (Accessing Array Elements)

배열은 스택에 할당될 수 있는 알려진 고정 크기의 단일 메모리 덩어리입니다. 다음과 같이 인덱싱 (indexing) 을 사용하여 배열의 요소에 접근할 수 있습니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let a = [1, 2, 3, 4, 5];

    let first = a[0];
    let second = a[1];
}
```

이 예제에서 `first`라는 변수는 배열의 인덱스 `[0]`에 있는 값이므로 값 `1`을 얻습니다. `second`라는 변수는 배열의 인덱스 `[1]`에서 값 `2`를 얻습니다.
