# 필드가 없는 유닛과 유사한 구조체

필드가 없는 구조체도 정의할 수 있습니다! 이러한 구조체는 "튜플 타입"에서 언급한 유닛 타입 `()`과 유사하게 동작하기 때문에 *유닛과 유사한 구조체 (unit-like structs)*라고 합니다. 유닛과 유사한 구조체는 일부 타입에 대해 트레이트 (trait) 를 구현해야 하지만 타입 자체에 저장할 데이터가 없을 때 유용할 수 있습니다. 트레이트는 10 장에서 논의할 것입니다. 다음은 `AlwaysEqual`이라는 유닛 구조체를 선언하고 인스턴스화하는 예입니다.

파일 이름: `src/main.rs`

```rust
struct AlwaysEqual;

fn main() {
    let subject = AlwaysEqual;
}
```

`AlwaysEqual`을 정의하려면 `struct` 키워드, 원하는 이름, 세미콜론을 사용합니다. 중괄호나 괄호는 필요하지 않습니다! 그런 다음 정의한 이름을 사용하여 중괄호나 괄호 없이 `subject` 변수에서 `AlwaysEqual`의 인스턴스를 얻을 수 있습니다. 나중에 이 타입에 대한 동작을 구현하여 `AlwaysEqual`의 모든 인스턴스가 다른 타입의 모든 인스턴스와 항상 같도록 할 수 있다고 상상해 보세요. 아마도 테스트 목적으로 알려진 결과를 얻기 위해서일 것입니다. 해당 동작을 구현하는 데는 어떤 데이터도 필요하지 않을 것입니다! 10 장에서 유닛과 유사한 구조체를 포함하여 모든 타입에 대해 트레이트를 정의하고 구현하는 방법을 볼 수 있습니다.

> **구조체 데이터의 소유권**
>
> Listing 5-1 의 `User` 구조체 정의에서 `&str` 문자열 슬라이스 타입 대신 소유된 `String` 타입을 사용했습니다. 이는 이 구조체의 각 인스턴스가 모든 데이터를 소유하고 전체 구조체가 유효한 동안 해당 데이터가 유효하도록 하기 위한 의도적인 선택입니다.
>
> 구조체가 다른 항목이 소유한 데이터에 대한 참조를 저장하는 것도 가능하지만, 그렇게 하려면 10 장에서 논의할 Rust 기능인 *라이프타임 (lifetimes)*을 사용해야 합니다. 라이프타임은 구조체가 참조하는 데이터가 구조체가 유효한 동안 유효하도록 보장합니다. `src/main.rs`에서 다음과 같이 라이프타임을 지정하지 않고 구조체에 참조를 저장하려고 하면 작동하지 않습니다.
>
>     struct User {
>         active: bool,
>         username: &str,
>         email: &str,
>         sign_in_count: u64,
>     }
>
>     fn main() {
>         let user1 = User {
>             active: true,
>             username: "someusername123",
>             email: "someone@example.com",
>             sign_in_count: 1,
>         };
>     }
>
> 컴파일러는 라이프타임 지정자가 필요하다고 불평할 것입니다.
>
>     $ `cargo run`
>        Compiling structs v0.1.0 (file:///projects/structs)
>     error[E0106]: missing lifetime specifier
>      --> src/main.rs:3:15
>       |
>     3 |     username: &str,
>       |               ^ expected named lifetime parameter
>       |
>     help: consider introducing a named lifetime parameter
>       |
>     1 ~ struct User<'a> {
>     2 |     active: bool,
>     3 ~     username: &'a str,
>       |
>
>     error[E0106]: missing lifetime specifier
>      --> src/main.rs:4:12
>       |
>     4 |     email: &str,
>       |            ^ expected named lifetime parameter
>       |
>     help: consider introducing a named lifetime parameter
>       |
>     1 ~ struct User<'a> {
>     2 |     active: bool,
>     3 |     username: &str,
>     4 ~     email: &'a str,
>       |
>
> 10 장에서는 이러한 오류를 수정하여 구조체에 참조를 저장할 수 있도록 하는 방법을 논의하지만, 지금은 `&str`과 같은 참조 대신 `String`과 같은 소유된 타입을 사용하여 이러한 오류를 수정할 것입니다.
