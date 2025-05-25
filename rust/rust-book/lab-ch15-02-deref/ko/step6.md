# 함수 및 메서드에서 암시적 Deref 강제 변환

*Deref 강제 변환*은 `Deref` 트레이트를 구현하는 타입에 대한 참조를 다른 타입에 대한 참조로 변환합니다. 예를 들어, `String`이 `&str`을 반환하도록 `Deref` 트레이트를 구현하므로, Deref 강제 변환은 `&String`을 `&str`로 변환할 수 있습니다. Deref 강제 변환은 Rust 가 함수 및 메서드의 인수에 대해 수행하는 편의 기능이며, `Deref` 트레이트를 구현하는 타입에서만 작동합니다. 특정 타입의 값에 대한 참조를 함수 또는 메서드 정의의 매개변수 타입과 일치하지 않는 함수 또는 메서드에 대한 인수로 전달할 때 자동으로 발생합니다. `deref` 메서드에 대한 일련의 호출은 제공된 타입을 매개변수에 필요한 타입으로 변환합니다.

Deref 강제 변환은 프로그래머가 함수 및 메서드 호출을 작성할 때 `&` 및 `*`를 사용하여 명시적인 참조 및 역참조를 많이 추가할 필요가 없도록 Rust 에 추가되었습니다. Deref 강제 변환 기능을 사용하면 참조 또는 스마트 포인터 모두에 대해 작동할 수 있는 더 많은 코드를 작성할 수도 있습니다.

Deref 강제 변환을 실제로 확인하려면 Listing 15-8 에서 정의한 `MyBox<T>` 타입과 Listing 15-10 에서 추가한 `Deref`의 구현을 사용해 보겠습니다. Listing 15-11 은 문자열 슬라이스 매개변수를 갖는 함수의 정의를 보여줍니다.

파일 이름: `src/main.rs`

```rust
fn hello(name: &str) {
    println!("Hello, {name}!");
}
```

Listing 15-11: `&str` 타입의 매개변수 `name`을 갖는 `hello` 함수

예를 들어, `hello("Rust");`와 같이 문자열 슬라이스를 인수로 사용하여 `hello` 함수를 호출할 수 있습니다. Deref 강제 변환을 사용하면 Listing 15-12 에 표시된 것처럼 `MyBox<String>` 타입의 값에 대한 참조로 `hello`를 호출할 수 있습니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let m = MyBox::new(String::from("Rust"));
    hello(&m);
}
```

Listing 15-12: Deref 강제 변환으로 인해 작동하는 `MyBox<String>` 값에 대한 참조로 `hello` 호출하기

여기서는 `MyBox<String>` 값에 대한 참조인 인수 `&m`으로 `hello` 함수를 호출하고 있습니다. Listing 15-10 에서 `MyBox<T>`에 `Deref` 트레이트를 구현했으므로 Rust 는 `deref`를 호출하여 `&MyBox<String>`을 `&String`으로 변환할 수 있습니다. 표준 라이브러리는 문자열 슬라이스를 반환하는 `String`에 대한 `Deref`의 구현을 제공하며, 이는 `Deref`에 대한 API 문서에 있습니다. Rust 는 `deref`를 다시 호출하여 `&String`을 `&str`로 변환하며, 이는 `hello` 함수의 정의와 일치합니다.

Rust 가 Deref 강제 변환을 구현하지 않았다면, Listing 15-12 의 코드 대신 Listing 15-13 의 코드를 작성하여 `&MyBox<String>` 타입의 값으로 `hello`를 호출해야 합니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let m = MyBox::new(String::from("Rust"));
    hello(&(*m)[..]);
}
```

Listing 15-13: Rust 에 Deref 강제 변환이 없는 경우 작성해야 하는 코드

`(*m)`은 `MyBox<String>`을 `String`으로 역참조합니다. 그런 다음 `&`와 `[..]`는 `hello`의 시그니처와 일치하도록 전체 문자열과 동일한 `String`의 문자열 슬라이스를 가져옵니다. Deref 강제 변환이 없는 이 코드는 관련된 모든 기호로 인해 읽고, 쓰고, 이해하기가 더 어렵습니다. Deref 강제 변환을 사용하면 Rust 가 이러한 변환을 자동으로 처리할 수 있습니다.

관련 타입에 대해 `Deref` 트레이트가 정의되면 Rust 는 타입을 분석하고 매개변수의 타입과 일치하는 참조를 얻기 위해 필요한 만큼 `Deref::deref`를 사용합니다. `Deref::deref`를 삽입해야 하는 횟수는 컴파일 시간에 결정되므로 Deref 강제 변환을 활용하는 데 런타임 페널티가 없습니다!
