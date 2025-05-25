# 원시 식별자

Rust 는 많은 프로그래밍 언어와 마찬가지로 "키워드"라는 개념을 가지고 있습니다. 키워드는 언어에 특별한 의미를 가지므로 변수 이름, 함수 이름 등과 같은 곳에서 사용할 수 없습니다. 원시 식별자는 키워드를 일반적으로 허용되지 않는 곳에서 사용할 수 있도록 합니다. 이는 특히 Rust 가 새로운 키워드를 도입하고, 이전 버전의 Rust 를 사용하는 라이브러리가 새로운 버전에서 도입된 키워드와 같은 이름의 변수나 함수를 가지고 있는 경우에 유용합니다.

예를 들어, Rust 2015 에디션으로 컴파일된 `foo` 크레이트가 `try`라는 함수를 내보낸다고 가정해 보겠습니다. 이 키워드는 2018 에디션의 새로운 기능을 위해 예약되어 있으므로, 원시 식별자 없이는 함수 이름을 지정할 수 없습니다.

```rust
extern crate foo;

fn main() {
    foo::try();
}
```

다음과 같은 오류가 발생합니다.

```plaintext
error: expected identifier, found keyword `try`
 --> src/main.rs:4:4
  |
4 | foo::try();
  |      ^^^ expected identifier, found keyword
```

원시 식별자를 사용하여 다음과 같이 작성할 수 있습니다.

```rust
extern crate foo;

fn main() {
    foo::r#try();
}
```
