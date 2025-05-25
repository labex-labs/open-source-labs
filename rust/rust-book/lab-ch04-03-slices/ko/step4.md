# String Slices as Parameters (매개변수로서의 문자열 슬라이스)

리터럴과 `String` 값의 슬라이스를 가져올 수 있다는 것을 알면 `first_word`에 대한 또 다른 개선 사항을 얻을 수 있으며, 그것은 바로 시그니처입니다.

```rust
fn first_word(s: &String) -> &str {
```

더 경험이 많은 Rust 개발자는 Listing 4-9 에 표시된 시그니처를 대신 작성할 것입니다. 이는 `&String` 값과 `&str` 값 모두에서 동일한 함수를 사용할 수 있도록 하기 때문입니다.

```rust
fn first_word(s: &str) -> &str {
```

Listing 4-9: `s` 매개변수의 유형으로 문자열 슬라이스를 사용하여 `first_word` 함수 개선

문자열 슬라이스가 있으면 이를 직접 전달할 수 있습니다. `String`이 있으면 `String`의 슬라이스 또는 `String`에 대한 참조를 전달할 수 있습니다. 이러한 유연성은 "함수 및 메서드를 사용한 암시적 Deref 강제 변환"에서 다룰 _Deref 강제 변환_ 기능을 활용합니다.

`String`에 대한 참조 대신 문자열 슬라이스를 사용하도록 함수를 정의하면 기능을 잃지 않고 API 를 더 일반적이고 유용하게 만들 수 있습니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let my_string = String::from("hello world");

    // `first_word` 는 부분적이든 전체이든 `String` 의 슬라이스에서 작동합니다.
    let word = first_word(&my_string[0..6]);
    let word = first_word(&my_string[..]);
    // `first_word` 는 또한 `String` 에 대한 참조에서도 작동하며, 이는
    // `String` 의 전체 슬라이스와 동일합니다.
    let word = first_word(&my_string);

    let my_string_literal = "hello world";

    // `first_word` 는 문자열 리터럴의 슬라이스에서 작동합니다.
    // 부분적이든 전체이든
    let word = first_word(&my_string_literal[0..6]);
    let word = first_word(&my_string_literal[..]);

    // 문자열 리터럴은 이미 문자열 슬라이스이므로
    // 슬라이스 구문 없이도 이것이 작동합니다!
    let word = first_word(my_string_literal);
}
```
