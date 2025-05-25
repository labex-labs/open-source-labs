# 문서화

`target/doc`에 문서를 생성하려면 `cargo doc`를 사용합니다.

모든 테스트 (문서 테스트 포함) 를 실행하려면 `cargo test`를 사용하고, 문서 테스트만 실행하려면 `cargo test --doc`를 사용합니다.

이러한 명령은 필요에 따라 `rustdoc` (및 `rustc`) 를 적절히 호출합니다.

## 문서 주석

문서화가 필요한 대규모 프로젝트에서 문서 주석은 매우 유용합니다. `rustdoc`를 실행할 때 이러한 주석이 문서로 컴파일됩니다. `///`로 표시되며 \[Markdown\]을 지원합니다.

````rust
#![crate_name = "doc"]

/// 여기서 사람을 나타냅니다.
pub struct Person {
    /// 줄리엣이 얼마나 싫어하든 사람은 이름을 가져야 합니다.
    name: String,
}

impl Person {
    /// 자신에게 주어진 이름을 가진 사람을 반환합니다.
    ///
    /// # 인수
    ///
    /// * `name` - 사람의 이름을 담고 있는 문자열 슬라이스
    ///
    /// # 예제
    ///
    /// ```
    /// // 주석 내부의 펜스 사이에 Rust 코드를 넣을 수 있습니다.
    /// // `rustdoc`에 --test를 전달하면 심지어 직접 테스트도 수행합니다!
    /// use doc::Person;
    /// let person = Person::new("name");
    /// ```
    pub fn new(name: &str) -> Person {
        Person {
            name: name.to_string(),
        }
    }

    /// 친절한 인사를 합니다!
    ///
    /// 자신에게 호출된 `Person`에게 "Hello, [이름](Person::name)"이라고 말합니다.
    pub fn hello(&self) {
        println!("Hello, {}!", self.name);
    }
}

fn main() {
    let john = Person::new("John");

    john.hello();
}
````

테스트를 실행하려면 먼저 코드를 라이브러리로 빌드한 다음, `rustdoc`에 라이브러리 위치를 알려서 각 doctest 프로그램에 연결해야 합니다.

```shell
$ rustc doc.rs --crate-type lib
$ rustdoc --test --extern doc="libdoc.rlib" doc.rs
```

## 문서 속성

`rustdoc`와 함께 사용되는 가장 일반적인 `#[doc]` 속성의 몇 가지 예는 다음과 같습니다.

## `inline`

개별 페이지로 링크하는 대신 문서를 내부에 포함하는 데 사용됩니다.

```rust
#[doc(inline)]
pub use bar::Bar;

/// bar 문서
mod bar {
    /// Bar 의 문서
    pub struct Bar;
}
```

## `no_inline`

개별 페이지 또는 어디에도 링크하지 않도록 방지하는 데 사용됩니다.

```rust
// libcore/prelude에서 가져온 예제
#[doc(no_inline)]
pub use crate::mem::drop;
```

## `hidden`

이를 사용하면 `rustdoc`가 문서에 포함되지 않도록 지정합니다.

```rust
// futures-rs 라이브러리에서 가져온 예제
#[doc(hidden)]
pub use self::async_await::*;
```

문서화를 위해 `rustdoc`는 커뮤니티에서 널리 사용됩니다. [표준 라이브러리 문서](https://doc.rust-lang.org/std/)를 생성하는 데 사용됩니다.
