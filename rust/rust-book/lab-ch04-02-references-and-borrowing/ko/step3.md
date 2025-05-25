# Dangling References

포인터를 사용하는 언어에서는, 메모리를 해제하면서 해당 메모리에 대한 포인터를 보존함으로써 _댕글링 포인터 (dangling pointer)_---다른 사람에게 할당되었을 수 있는 메모리 위치를 참조하는 포인터---를 실수로 생성하기 쉽습니다. 반대로, Rust 에서는 컴파일러가 참조가 댕글링 참조가 되지 않도록 보장합니다. 즉, 어떤 데이터에 대한 참조가 있는 경우, 컴파일러는 데이터에 대한 참조가 데이터보다 먼저 범위를 벗어나지 않도록 보장합니다.

컴파일 시간 오류를 통해 Rust 가 댕글링 참조를 어떻게 방지하는지 확인하기 위해 댕글링 참조를 생성해 보겠습니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let reference_to_nothing = dangle();
}

fn dangle() -> &String {
    let s = String::from("hello");

    &s
}
```

다음은 오류입니다.

```bash
error[E0106]: missing lifetime specifier
 --> src/main.rs:5:16
  |
5 | fn dangle() -> &String {
  |                ^ expected named lifetime parameter
  |
  = help: this function's return type contains a borrowed value,
but there is no value for it to be borrowed from
help: consider using the `'static` lifetime
  |
5 | fn dangle() -> &'static String {
  |                ~~~~~~~~
```

이 오류 메시지는 아직 다루지 않은 기능인 수명 (lifetimes) 을 참조합니다. 10 장에서 수명에 대해 자세히 논의할 것입니다. 그러나 수명에 대한 부분을 무시하면, 메시지에는 이 코드가 문제인 이유에 대한 핵심 내용이 포함되어 있습니다.

```rust
this function's return type contains a borrowed value, but there
is no value for it to be borrowed from
```

`dangle` 코드의 각 단계에서 정확히 어떤 일이 발생하는지 자세히 살펴보겠습니다.

    // src/main.rs
    fn dangle() -> &String { // dangle returns a reference to a String

        let s = String::from("hello"); // s is a new String

        &s // we return a reference to the String, s
    } // Here, s goes out of scope and is dropped, so its memory goes away
      // Danger!

`s`가 `dangle` 내에서 생성되기 때문에, `dangle`의 코드가 완료되면 `s`는 할당 해제됩니다. 그러나 우리는 그것에 대한 참조를 반환하려고 했습니다. 즉, 이 참조는 유효하지 않은 `String`을 가리키게 됩니다. 좋지 않습니다! Rust 는 우리가 이것을 하도록 허용하지 않습니다.

여기서의 해결책은 `String`을 직접 반환하는 것입니다.

```rust
fn no_dangle() -> String {
    let s = String::from("hello");

    s
}
```

이것은 아무런 문제 없이 작동합니다. 소유권이 이동되고 아무것도 할당 해제되지 않습니다.
