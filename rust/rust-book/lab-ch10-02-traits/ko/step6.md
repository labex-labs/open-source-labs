# 트레이트 바운드 구문

`impl Trait` 구문은 간단한 경우에 작동하지만, 실제로 *트레이트 바운드*라고 하는 더 긴 형식의 구문 설탕입니다. 다음과 같습니다.

```rust
pub fn notify<T: Summary>(item: &T) {
    println!("Breaking news! {}", item.summarize());
}
```

이 더 긴 형식은 이전 섹션의 예제와 동일하지만 더 장황합니다. 제네릭 타입 매개변수의 선언과 함께 콜론 뒤와 꺾쇠 괄호 안에 트레이트 바운드를 배치합니다.

`impl Trait` 구문은 편리하며 간단한 경우에 더 간결한 코드를 만들 수 있으며, 더 완전한 트레이트 바운드 구문은 다른 경우에 더 많은 복잡성을 표현할 수 있습니다. 예를 들어, `Summary`를 구현하는 두 개의 매개변수를 가질 수 있습니다. `impl Trait` 구문을 사용하여 그렇게 하면 다음과 같습니다.

```rust
pub fn notify(item1: &impl Summary, item2: &impl Summary) {
```

`impl Trait`를 사용하는 것은 이 함수가 `item1`과 `item2`가 서로 다른 타입을 갖도록 허용하려는 경우에 적합합니다 (두 타입 모두 `Summary`를 구현하는 한). 그러나 두 매개변수가 동일한 타입을 갖도록 강제하려면 다음과 같이 트레이트 바운드를 사용해야 합니다.

```rust
pub fn notify<T: Summary>(item1: &T, item2: &T) {
```

`item1` 및 `item2` 매개변수의 타입으로 지정된 제네릭 타입 `T`는 `item1` 및 `item2`에 대한 인수로 전달된 값의 구체적인 타입이 동일해야 하도록 함수를 제한합니다.
