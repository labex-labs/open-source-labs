# while let (while let) 조건 루프

`if let`과 유사하게 구성된 `while let` 조건 루프는 패턴이 계속 일치하는 동안 `while` 루프가 실행되도록 허용합니다. Listing 18-2 에서 우리는 벡터를 스택으로 사용하고 벡터의 값을 푸시된 반대 순서로 출력하는 `while let` 루프를 코딩합니다.

파일 이름: `src/main.rs`

```rust
let mut stack = Vec::new();

stack.push(1);
stack.push(2);
stack.push(3);

while let Some(top) = stack.pop() {
    println!("{top}");
}
```

Listing 18-2: `stack.pop()`이 `Some`을 반환하는 동안 값을 출력하기 위해 `while let` 루프 사용

이 예제는 `3`, `2`, 그리고 `1`을 출력합니다. `pop` 메서드는 벡터에서 마지막 요소를 가져와 `Some(value)`를 반환합니다. 벡터가 비어 있으면 `pop`은 `None`을 반환합니다. `while` 루프는 `pop`이 `Some`을 반환하는 동안 블록의 코드를 계속 실행합니다. `pop`이 `None`을 반환하면 루프가 중지됩니다. 우리는 `while let`을 사용하여 스택에서 모든 요소를 꺼낼 수 있습니다.
