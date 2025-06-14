# `+` 연산자 또는 `format!` 매크로를 사용한 연결

종종 두 개의 기존 문자열을 결합해야 할 것입니다. 이를 수행하는 한 가지 방법은 Listing 8-18 에 표시된 것처럼 `+` 연산자를 사용하는 것입니다.

```rust
let s1 = String::from("Hello, ");
let s2 = String::from("world!");
let s3 = s1 + &s2; // note s1 has been moved here and can no longer be used
```

Listing 8-18: `+` 연산자를 사용하여 두 개의 `String` 값을 새로운 `String` 값으로 결합하기

문자열 `s3`는 `Hello, world!`를 포함하게 됩니다. 덧셈 후 `s1`이 더 이상 유효하지 않고, `s2`에 대한 참조를 사용한 이유는 `+` 연산자를 사용할 때 호출되는 메서드의 시그니처와 관련이 있습니다. `+` 연산자는 `add` 메서드를 사용하며, 해당 시그니처는 다음과 같습니다.

```rust
fn add(self, s: &str) -> String {
```

표준 라이브러리에서 제네릭 (generics) 과 연관된 타입 (associated types) 을 사용하여 정의된 `add`를 볼 수 있습니다. 여기서는 구체적인 타입을 대체했는데, 이는 `String` 값을 사용하여 이 메서드를 호출할 때 발생하는 일입니다. 제네릭에 대해서는 10 장에서 논의할 것입니다. 이 시그니처는 `+` 연산자의 까다로운 부분을 이해하는 데 필요한 단서를 제공합니다.

먼저, `s2`는 `&`를 가지고 있습니다. 이는 두 번째 문자열의 *참조*를 첫 번째 문자열에 추가한다는 의미입니다. 이는 `add` 함수의 `s` 매개변수 때문입니다. `String`에 `&str`만 추가할 수 있으며, 두 개의 `String` 값을 함께 추가할 수는 없습니다. 하지만 잠깐만요---`&s2`의 타입은 `&str`이 아니라 `&String`입니다. `add`의 두 번째 매개변수에 지정된 대로입니다. 그렇다면 Listing 8-18 이 컴파일되는 이유는 무엇일까요?

`add` 호출에서 `&s2`를 사용할 수 있는 이유는 컴파일러가 `&String` 인수를 `&str`로 *강제 변환 (coerce)*할 수 있기 때문입니다. `add` 메서드를 호출할 때 Rust 는 *역참조 강제 변환 (deref coercion)*을 사용하며, 여기서는 `&s2`를 `&s2[..]`로 변환합니다. 역참조 강제 변환에 대해서는 15 장에서 더 자세히 논의할 것입니다. `add`가 `s` 매개변수의 소유권을 가져가지 않기 때문에, 이 연산 후에도 `s2`는 여전히 유효한 `String`이 됩니다.

둘째, 시그니처에서 `add`가 `self`의 소유권을 가져가는 것을 볼 수 있습니다. 왜냐하면 `self`가 `&`를 _가지고 있지 않기_ 때문입니다. 이는 Listing 8-18 의 `s1`이 `add` 호출로 이동하고 그 이후에는 더 이상 유효하지 않다는 것을 의미합니다. 따라서 `let s3 = s1 + &s2;`가 두 문자열을 모두 복사하여 새 문자열을 생성하는 것처럼 보이지만, 이 문은 실제로 `s1`의 소유권을 가져와 `s2`의 내용을 복사하여 추가한 다음 결과의 소유권을 반환합니다. 즉, 많은 복사를 하는 것처럼 보이지만 그렇지 않습니다. 구현은 복사보다 더 효율적입니다.

여러 문자열을 연결해야 하는 경우, `+` 연산자의 동작은 다루기 어려워집니다.

```rust
let s1 = String::from("tic");
let s2 = String::from("tac");
let s3 = String::from("toe");

let s = s1 + "-" + &s2 + "-" + &s3;
```

이 시점에서 `s`는 `tic-tac-toe`가 됩니다. 모든 `+` 및 `"` 문자로 인해 무슨 일이 일어나고 있는지 파악하기 어렵습니다. 더 복잡한 방식으로 문자열을 결합하려면 대신 `format!` 매크로를 사용할 수 있습니다.

```rust
let s1 = String::from("tic");
let s2 = String::from("tac");
let s3 = String::from("toe");

let s = format!("{s1}-{s2}-{s3}");
```

이 코드는 또한 `s`를 `tic-tac-toe`로 설정합니다. `format!` 매크로는 `println!`과 유사하게 작동하지만, 출력을 화면에 인쇄하는 대신 내용을 포함하는 `String`을 반환합니다. `format!`을 사용하는 코드 버전은 훨씬 읽기 쉽고, `format!` 매크로에서 생성된 코드는 참조를 사용하므로 이 호출은 매개변수의 소유권을 가져가지 않습니다.
