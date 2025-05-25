# 반환 값이 있는 함수 (Functions with Return Values)

함수는 자신을 호출하는 코드에 값을 반환할 수 있습니다. 반환 값의 이름을 지정하지 않지만, 화살표 (`->`) 뒤에 해당 유형을 선언해야 합니다. Rust 에서 함수의 반환 값은 함수 본문의 블록에 있는 마지막 표현식의 값과 동일합니다. `return` 키워드를 사용하고 값을 지정하여 함수에서 조기에 반환할 수 있지만, 대부분의 함수는 마지막 표현식을 암시적으로 반환합니다. 다음은 값을 반환하는 함수의 예입니다.

파일 이름: `src/main.rs`

```rust
fn five() -> i32 {
    5
}

fn main() {
    let x = five();

    println!("The value of x is: {x}");
}
```

`five` 함수에는 함수 호출, 매크로 또는 `let` 문조차 없습니다. 단지 숫자 `5`만 있습니다. 이것은 Rust 에서 완벽하게 유효한 함수입니다. 함수의 반환 유형도 `-> i32`로 지정되어 있습니다. 이 코드를 실행해 보세요. 출력은 다음과 같아야 합니다.

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
    Finished dev [unoptimized + debuginfo] target(s) in 0.30s
     Running `target/debug/functions`
The value of x is: 5
```

`five`의 `5`는 함수의 반환 값이며, 반환 유형이 `i32`인 이유입니다. 이를 자세히 살펴보겠습니다. 두 가지 중요한 부분이 있습니다. 먼저, `let x = five();` 줄은 함수의 반환 값을 사용하여 변수를 초기화하고 있음을 보여줍니다. `five` 함수가 `5`를 반환하므로 해당 줄은 다음과 같습니다.

```rust
let x = 5;
```

둘째, `five` 함수에는 매개변수가 없고 반환 값의 유형을 정의하지만, 함수 본문은 세미콜론이 없는 외로운 `5`입니다. 왜냐하면 반환하려는 값인 표현식이기 때문입니다.

다른 예를 살펴보겠습니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let x = plus_one(5);

    println!("The value of x is: {x}");
}

fn plus_one(x: i32) -> i32 {
    x + 1
}
```

이 코드를 실행하면 `The value of x is: 6`이 출력됩니다. 그러나 `x + 1`을 포함하는 줄의 끝에 세미콜론을 배치하여 표현식에서 문으로 변경하면 오류가 발생합니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let x = plus_one(5);

    println!("The value of x is: {x}");
}

fn plus_one(x: i32) -> i32 {
    x + 1;
}
```

이 코드를 컴파일하면 다음과 같은 오류가 발생합니다.

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
error[E0308]: mismatched types
 --> src/main.rs:7:24
  |
7 | fn plus_one(x: i32) -> i32 {
  |    --------            ^^^ expected `i32`, found `()`
  |    |
  |    implicitly returns `()` as its body has no tail or `return` expression
8 |     x + 1;
  |          - help: remove this semicolon
```

주요 오류 메시지인 `mismatched types`는 이 코드의 핵심 문제를 드러냅니다. `plus_one` 함수의 정의는 `i32`를 반환한다고 말하지만, 문은 값으로 평가되지 않으며, 이는 유닛 타입인 `()`로 표현됩니다. 따라서 아무것도 반환되지 않아 함수 정의와 모순되어 오류가 발생합니다. 이 출력에서 Rust 는 이 문제를 해결하는 데 도움이 되는 메시지를 제공합니다. 세미콜론을 제거하라고 제안하며, 그러면 오류가 수정됩니다.
