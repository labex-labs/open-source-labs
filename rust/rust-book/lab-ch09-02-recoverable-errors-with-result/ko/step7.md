# ? 연산자를 사용할 수 있는 곳

`?` 연산자는 반환 타입이 `?`가 사용되는 값과 호환되는 함수에서만 사용할 수 있습니다. 이는 `?` 연산자가 Listing 9-6 에서 정의한 `match` 표현식과 동일한 방식으로 함수에서 값을 조기에 반환하도록 정의되었기 때문입니다. Listing 9-6 에서 `match`는 `Result` 값을 사용했고, 조기 반환 분기는 `Err(e)` 값을 반환했습니다. 함수의 반환 타입은 이 `return`과 호환되도록 `Result`여야 합니다.

Listing 9-10 에서, `?` 연산자를 `main` 함수에서 사용하고 반환 타입이 `?`를 사용하는 값의 타입과 호환되지 않는 경우 발생하는 오류를 살펴보겠습니다.

파일 이름: `src/main.rs`

```rust
use std::fs::File;

fn main() {
    let greeting_file = File::open("hello.txt")?;
}
```

Listing 9-10: `()`를 반환하는 `main` 함수에서 `?`를 사용하려고 하면 컴파일되지 않습니다.

이 코드는 파일을 엽니다. 이는 실패할 수 있습니다. `?` 연산자는 `File::open`에서 반환된 `Result` 값을 따르지만, 이 `main` 함수는 `Result`가 아닌 `()`의 반환 타입을 가지고 있습니다. 이 코드를 컴파일하면 다음과 같은 오류 메시지가 나타납니다.

```bash
error[E0277]: the `?` operator can only be used in a function that returns
`Result` or `Option` (or another type that implements `FromResidual`)
 --> src/main.rs:4:48
  |
3 | / fn main() {
4 | |     let greeting_file = File::open("hello.txt")?;
  | |                                                ^ cannot use the `?`
operator in a function that returns `()`
5 | | }
  | |_- this function should return `Result` or `Option` to accept `?`
  |
  = help: the trait `FromResidual<Result<Infallible, std::io::Error>>` is not
implemented for `()`
```

이 오류는 `?` 연산자를 `Result`, `Option` 또는 `FromResidual`을 구현하는 다른 타입을 반환하는 함수에서만 사용할 수 있음을 지적합니다.

오류를 수정하려면 두 가지 선택지가 있습니다. 한 가지 선택지는 해당 작업을 방해하는 제한 사항이 없는 한, 함수의 반환 타입을 `?` 연산자를 사용하는 값과 호환되도록 변경하는 것입니다. 다른 선택지는 `match` 또는 `Result<T, E>` 메서드 중 하나를 사용하여 적절한 방식으로 `Result<T, E>`를 처리하는 것입니다.

오류 메시지는 또한 `?`가 `Option<T>` 값과 함께 사용될 수 있다고 언급했습니다. `Result`에 `?`를 사용하는 것과 마찬가지로, `Option`에 `?`를 사용하는 것은 `Option`을 반환하는 함수에서만 가능합니다. `Option<T>`에서 호출될 때 `?` 연산자의 동작은 `Result<T, E>`에서 호출될 때와 유사합니다. 값이 `None`이면, `None`은 해당 지점에서 함수에서 조기에 반환됩니다. 값이 `Some`이면, `Some` 내부의 값이 표현식의 결과 값이고 함수는 계속됩니다. Listing 9-11 은 주어진 텍스트에서 첫 번째 줄의 마지막 문자를 찾는 함수의 예시입니다.

```rust
fn last_char_of_first_line(text: &str) -> Option<char> {
    text.lines().next()?.chars().last()
}
```

Listing 9-11: `Option<T>` 값에 `?` 연산자 사용

이 함수는 문자가 있을 수도 있고 없을 수도 있기 때문에 `Option<char>`를 반환합니다. 이 코드는 `text` 문자열 슬라이스 인수를 가져와서 `lines` 메서드를 호출합니다. 이 메서드는 문자열의 줄에 대한 반복자를 반환합니다. 이 함수는 첫 번째 줄을 검사하려는 것이므로, 반복자에서 `next`를 호출하여 반복자에서 첫 번째 값을 가져옵니다. `text`가 빈 문자열이면, 이 `next` 호출은 `None`을 반환하며, 이 경우 `?`를 사용하여 멈추고 `last_char_of_first_line`에서 `None`을 반환합니다. `text`가 빈 문자열이 아니면, `next`는 `text`의 첫 번째 줄의 문자열 슬라이스를 포함하는 `Some` 값을 반환합니다.

`?`는 문자열 슬라이스를 추출하고, 해당 문자열 슬라이스에서 `chars`를 호출하여 문자의 반복자를 얻을 수 있습니다. 우리는 이 첫 번째 줄의 마지막 문자에 관심이 있으므로, `last`를 호출하여 반복자의 마지막 항목을 반환합니다. 이것은 `Option`입니다. 왜냐하면 첫 번째 줄이 빈 문자열일 가능성이 있기 때문입니다. 예를 들어, `text`가 빈 줄로 시작하지만 다른 줄에 문자가 있는 경우, `"\nhi"`와 같습니다. 그러나 첫 번째 줄에 마지막 문자가 있으면, `Some` 변형에서 반환됩니다. 중간의 `?` 연산자는 이 로직을 간결하게 표현하는 방법을 제공하여, 한 줄로 함수를 구현할 수 있도록 합니다. `Option`에서 `?` 연산자를 사용할 수 없다면, 더 많은 메서드 호출이나 `match` 표현식을 사용하여 이 로직을 구현해야 합니다.

`Result`를 반환하는 함수에서 `Result`에 `?` 연산자를 사용할 수 있으며, `Option`을 반환하는 함수에서 `Option`에 `?` 연산자를 사용할 수 있지만, 혼합하여 사용할 수는 없습니다. `?` 연산자는 자동으로 `Result`를 `Option`으로 또는 그 반대로 변환하지 않습니다. 이러한 경우, `Result`의 `ok` 메서드 또는 `Option`의 `ok_or` 메서드와 같은 메서드를 사용하여 명시적으로 변환할 수 있습니다.

지금까지 사용한 모든 `main` 함수는 `()`를 반환합니다. `main` 함수는 실행 가능한 프로그램의 진입점과 종료점이므로 특별하며, 프로그램이 예상대로 작동하기 위해 반환 타입에 대한 제한이 있습니다.

다행히, `main`은 `Result<(), E>`도 반환할 수 있습니다. Listing 9-12 는 Listing 9-10 의 코드를 가지고 있지만, `main`의 반환 타입을 `Result<(), Box<dyn Error>>`로 변경하고 마지막에 반환 값 `Ok(())`를 추가했습니다. 이 코드는 이제 컴파일됩니다.

파일 이름: `src/main.rs`

```rust
use std::error::Error;
use std::fs::File;

fn main() -> Result<(), Box<dyn Error>> {
    let greeting_file = File::open("hello.txt")?;

    Ok(())
}
```

Listing 9-12: `main`을 `Result<(), E>`로 변경하면 `Result` 값에 `?` 연산자를 사용할 수 있습니다.

`Box<dyn Error>` 타입은 *트레이트 객체*이며, "다양한 타입의 값을 허용하는 트레이트 객체 사용"에서 이에 대해 이야기할 것입니다. 지금은 `Box<dyn Error>`를 "모든 종류의 오류"로 읽을 수 있습니다. 오류 타입이 `Box<dyn Error>`인 `main` 함수에서 `Result` 값에 `?`를 사용하는 것은 모든 `Err` 값을 조기에 반환할 수 있기 때문에 허용됩니다. 이 `main` 함수의 본문은 `std::io::Error` 타입의 오류만 반환하더라도, `Box<dyn Error>`를 지정함으로써, 이 시그니처는 `main`의 본문에 다른 오류를 반환하는 코드가 더 추가되더라도 계속 정확하게 유지됩니다.

`main` 함수가 `Result<(), E>`를 반환하면, 실행 파일은 `main`이 `Ok(())`를 반환하면 값 `0`으로 종료되고, `main`이 `Err` 값을 반환하면 0 이 아닌 값으로 종료됩니다. C 로 작성된 실행 파일은 종료될 때 정수를 반환합니다. 성공적으로 종료되는 프로그램은 정수 `0`을 반환하고, 오류가 발생하는 프로그램은 `0`이 아닌 다른 정수를 반환합니다. Rust 도 이 규칙과 호환되도록 실행 파일에서 정수를 반환합니다.

`main` 함수는 `std::process::Termination` 트레이트를 구현하는 모든 타입을 반환할 수 있으며, 이 트레이트에는 `ExitCode`를 반환하는 함수 `report`가 포함되어 있습니다. 자체 타입에 대한 `Termination` 트레이트를 구현하는 방법에 대한 자세한 내용은 표준 라이브러리 문서를 참조하십시오.

이제 `panic!`을 호출하거나 `Result`를 반환하는 세부 사항에 대해 논의했으므로, 어떤 경우에 어떤 것을 사용하는 것이 적절한지 결정하는 방법에 대한 주제로 돌아가겠습니다.
