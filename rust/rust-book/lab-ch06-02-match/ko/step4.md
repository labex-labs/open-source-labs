# Match 는 완전해야 함

`match`에 대해 논의해야 할 또 다른 측면이 있습니다. arm 의 패턴은 모든 가능성을 다루어야 합니다. 버그가 있고 컴파일되지 않는 `plus_one` 함수의 이 버전을 고려해 보십시오.

```rust
fn plus_one(x: Option<i32>) -> Option<i32> {
    match x {
        Some(i) => Some(i + 1),
    }
}
```

`None` 케이스를 처리하지 않았으므로 이 코드는 버그를 유발합니다. 다행히 Rust 가 어떻게 잡아야 하는지 아는 버그입니다. 이 코드를 컴파일하려고 하면 다음과 같은 오류가 발생합니다.

```bash
error[E0004]: non-exhaustive patterns: `None` not covered
 --> src/main.rs:3:15
  |
3 |         match x {
  |               ^ pattern `None` not covered
  |
  note: `Option<i32>` defined here
      = note: the matched value is of type `Option<i32>`
help: ensure that all possible cases are being handled by adding
a match arm with a wildcard pattern or an explicit pattern as
shown
    |
4   ~             Some(i) => Some(i + 1),
5   ~             None => todo!(),
    |
```

Rust 는 모든 가능한 경우를 다루지 않았다는 것을 알고 있으며, 심지어 어떤 패턴을 잊었는지도 알고 있습니다! Rust 의 Match 는 *exhaustive(완전)*합니다. 코드가 유효하려면 모든 마지막 가능성을 소진해야 합니다. 특히 `Option<T>`의 경우 Rust 가 `None` 케이스를 명시적으로 처리하는 것을 잊지 못하게 할 때, null 이 있을 수 있는데 값을 가지고 있다고 가정하는 것을 방지하여 앞서 논의한 10 억 달러의 실수를 불가능하게 만듭니다.
