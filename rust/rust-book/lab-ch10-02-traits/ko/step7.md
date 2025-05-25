# `+` 구문을 사용하여 여러 트레이트 바운드 지정하기

또한 둘 이상의 트레이트 바운드를 지정할 수 있습니다. `notify`가 `item`에 대해 `summarize`뿐만 아니라 표시 형식 (display formatting) 도 사용하도록 하려는 경우를 가정해 보겠습니다. `notify` 정의에서 `item`이 `Display`와 `Summary`를 모두 구현해야 한다고 지정합니다. `+` 구문을 사용하여 그렇게 할 수 있습니다.

```rust
pub fn notify(item: &(impl Summary + Display)) {
```

`+` 구문은 제네릭 타입에 대한 트레이트 바운드와 함께 사용할 수도 있습니다.

```rust
pub fn notify<T: Summary + Display>(item: &T) {
```

두 개의 트레이트 바운드가 지정되면, `notify`의 본문은 `summarize`를 호출하고 `{}`를 사용하여 `item`을 형식화할 수 있습니다.
