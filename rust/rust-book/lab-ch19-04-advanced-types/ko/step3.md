# 타입 별칭 (Type Aliases) 을 사용하여 타입 동의어 생성하기

Rust 는 기존 타입에 다른 이름을 부여하기 위해 *타입 별칭 (type alias)*을 선언하는 기능을 제공합니다. 이를 위해 `type` 키워드를 사용합니다. 예를 들어, 다음과 같이 `Kilometers` 별칭을 `i32`에 대해 생성할 수 있습니다.

```rust
type Kilometers = i32;
```

이제 `Kilometers` 별칭은 `i32`의 *동의어 (synonym)*입니다. Listing 19-15 에서 생성한 `Millimeters` 및 `Meters` 타입과는 달리, `Kilometers`는 별도의 새로운 타입이 아닙니다. `Kilometers` 타입을 가진 값은 `i32` 타입의 값과 동일하게 처리됩니다.

    type Kilometers = i32;

    let x: i32 = 5;
    let y: Kilometers = 5;

    println!("x + y = {}", x + y);

`Kilometers`와 `i32`는 동일한 타입이므로, 두 타입의 값을 더할 수 있으며, `Kilometers` 값을 `i32` 매개변수를 받는 함수에 전달할 수 있습니다. 그러나 이 방법을 사용하면 앞서 논의한 newtype 패턴에서 얻을 수 있는 타입 검사 (type-checking) 의 이점을 얻을 수 없습니다. 즉, `Kilometers`와 `i32` 값을 어딘가에서 혼합하면 컴파일러는 오류를 발생시키지 않습니다.

타입 동의어의 주요 사용 사례는 반복을 줄이는 것입니다. 예를 들어, 다음과 같은 긴 타입을 가질 수 있습니다.

```rust
Box<dyn Fn() + Send + 'static>
```

이 긴 타입을 함수 시그니처 (function signatures) 와 코드 전체의 타입 어노테이션 (type annotations) 으로 작성하는 것은 지루하고 오류가 발생하기 쉽습니다. Listing 19-24 와 같은 코드로 가득 찬 프로젝트를 상상해 보십시오.

```rust
let f: Box<dyn Fn() + Send + 'static> = Box::new(|| {
    println!("hi");
});

fn takes_long_type(f: Box<dyn Fn() + Send + 'static>) {
    --snip--
}

fn returns_long_type() -> Box<dyn Fn() + Send + 'static> {
    --snip--
}
```

Listing 19-24: 여러 곳에서 긴 타입 사용

타입 별칭은 반복을 줄여 이 코드를 더 관리하기 쉽게 만듭니다. Listing 19-25 에서, 장황한 타입에 대한 `Thunk`라는 별칭을 도입했으며, 타입의 모든 사용을 더 짧은 별칭 `Thunk`로 대체할 수 있습니다.

    type Thunk = Box<dyn Fn() + Send + 'static>;

    let f: Thunk = Box::new(|| println!("hi"));

    fn takes_long_type(f: Thunk) {
        --snip--
    }

    fn returns_long_type() -> Thunk {
        --snip--
    }

Listing 19-25: 반복을 줄이기 위해 `Thunk` 타입 별칭 도입

이 코드는 훨씬 읽고 쓰기 쉽습니다! 타입 별칭에 의미 있는 이름을 선택하면 의도를 전달하는 데 도움이 될 수 있습니다 (*thunk*는 나중에 평가될 코드를 의미하는 단어이므로 저장되는 클로저에 적합한 이름입니다).

타입 별칭은 반복을 줄이기 위해 `Result<T, E>` 타입과 함께 자주 사용됩니다. 표준 라이브러리의 `std::io` 모듈을 고려해 보십시오. I/O 작업은 작업이 실패할 경우를 처리하기 위해 종종 `Result<T, E>`를 반환합니다. 이 라이브러리에는 모든 가능한 I/O 오류를 나타내는 `std::io::Error` 구조체가 있습니다. `std::io`의 많은 함수는 `E`가 `std::io::Error`인 `Result<T, E>`를 반환합니다. 예를 들어, `Write` 트레이트의 다음 함수와 같습니다.

```rust
use std::fmt;
use std::io::Error;

pub trait Write {
    fn write(&mut self, buf: &[u8]) -> Result<usize, Error>;
    fn flush(&mut self) -> Result<(), Error>;

    fn write_all(&mut self, buf: &[u8]) -> Result<(), Error>;
    fn write_fmt(
        &mut self,
        fmt: fmt::Arguments,
    ) -> Result<(), Error>;
}
```

`Result<..., Error>`가 많이 반복됩니다. 따라서 `std::io`에는 다음과 같은 타입 별칭 선언이 있습니다.

```rust
type Result<T> = std::result::Result<T, std::io::Error>;
```

이 선언은 `std::io` 모듈에 있으므로, 완전한 자격의 별칭 `std::io::Result<T>`를 사용할 수 있습니다. 즉, `E`가 `std::io::Error`로 채워진 `Result<T, E>`입니다. `Write` 트레이트 함수 시그니처는 다음과 같이 표시됩니다.

```rust
pub trait Write {
    fn write(&mut self, buf: &[u8]) -> Result<usize>;
    fn flush(&mut self) -> Result<()>;

    fn write_all(&mut self, buf: &[u8]) -> Result<()>;
    fn write_fmt(&mut self, fmt: fmt::Arguments) -> Result<()>;
}
```

타입 별칭은 두 가지 방식으로 도움이 됩니다. 코드를 더 쉽게 작성할 수 있게 해주고 `std::io` 전체에서 일관된 인터페이스를 제공합니다. 별칭이므로, 다른 `Result<T, E>`일 뿐이며, 이는 `Result<T, E>`에서 작동하는 모든 메서드를 사용할 수 있을 뿐만 아니라 `?` 연산자와 같은 특수 구문을 사용할 수 있음을 의미합니다.
