# 매개변수로서의 트레이트

이제 트레이트를 정의하고 구현하는 방법을 알았으므로, 다양한 타입을 허용하는 함수를 정의하기 위해 트레이트를 사용하는 방법을 살펴볼 수 있습니다. Listing 10-13 에서 `NewsArticle` 및 `Tweet` 타입에 구현한 `Summary` 트레이트를 사용하여, `Summary` 트레이트를 구현하는 타입인 `item` 매개변수에서 `summarize` 메서드를 호출하는 `notify` 함수를 정의합니다. 이를 위해 다음과 같이 `impl Trait` 구문을 사용합니다.

```rust
pub fn notify(item: &impl Summary) {
    println!("Breaking news! {}", item.summarize());
}
```

`item` 매개변수에 대한 구체적인 타입 대신, `impl` 키워드와 트레이트 이름을 지정합니다. 이 매개변수는 지정된 트레이트를 구현하는 모든 타입을 허용합니다. `notify`의 본문에서, `summarize`와 같이 `Summary` 트레이트에서 제공되는 `item`에 대한 모든 메서드를 호출할 수 있습니다. `notify`를 호출하고 `NewsArticle` 또는 `Tweet`의 모든 인스턴스를 전달할 수 있습니다. `String` 또는 `i32`와 같은 다른 타입으로 함수를 호출하는 코드는 해당 타입이 `Summary`를 구현하지 않으므로 컴파일되지 않습니다.
