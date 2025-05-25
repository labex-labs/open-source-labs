# 매개변수 (Parameters)

함수의 시그니처 (signature) 의 일부인 특수한 변수인 *매개변수 (parameters)*를 정의할 수 있습니다. 함수에 매개변수가 있는 경우 해당 매개변수에 대한 구체적인 값을 제공할 수 있습니다. 기술적으로 구체적인 값은 *인수 (arguments)*라고 하지만, 일상적인 대화에서는 함수 정의의 변수 또는 함수를 호출할 때 전달되는 구체적인 값에 대해 *매개변수*와 *인수*라는 단어를 서로 바꿔서 사용하는 경향이 있습니다.

`another_function`의 이 버전에서는 매개변수를 추가합니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    another_function(5);
}

fn another_function(x: i32) {
    println!("The value of x is: {x}");
}
```

이 프로그램을 실행해 보세요. 다음 출력을 얻을 수 있습니다.

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
    Finished dev [unoptimized + debuginfo] target(s) in 1.21s
     Running `target/debug/functions`
The value of x is: 5
```

`another_function`의 선언에는 `x`라는 매개변수가 하나 있습니다. `x`의 유형은 `i32`로 지정됩니다. `another_function`에 `5`를 전달하면 `println!` 매크로가 형식 문자열에서 `x`를 포함하는 중괄호 쌍이 있던 위치에 `5`를 넣습니다.

함수 시그니처에서는 각 매개변수의 유형을 _반드시_ 선언해야 합니다. 이것은 Rust 의 설계에서 의도적인 결정입니다. 함수 정의에서 유형 주석 (type annotations) 을 요구하면 컴파일러가 코드의 다른 곳에서 어떤 유형을 의미하는지 파악하기 위해 거의 사용하지 않아도 됩니다. 또한 컴파일러는 함수가 예상하는 유형을 알고 있는 경우 더 유용한 오류 메시지를 제공할 수 있습니다.

여러 매개변수를 정의할 때는 다음과 같이 쉼표로 매개변수 선언을 구분합니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    print_labeled_measurement(5, 'h');
}

fn print_labeled_measurement(value: i32, unit_label: char) {
    println!("The measurement is: {value}{unit_label}");
}
```

이 예제는 `print_labeled_measurement`라는 함수를 두 개의 매개변수로 만듭니다. 첫 번째 매개변수는 `value`이고 `i32`입니다. 두 번째는 `unit_label`이고 유형은 `char`입니다. 그런 다음 함수는 `value`와 `unit_label`을 모두 포함하는 텍스트를 인쇄합니다.

이 코드를 실행해 보겠습니다. _functions_ 프로젝트의 `src/main.rs` 파일에 현재 있는 프로그램을 앞의 예제로 바꾸고 `cargo run`을 사용하여 실행합니다.

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
    Finished dev [unoptimized + debuginfo] target(s) in 0.31s
     Running `target/debug/functions`
The measurement is: 5h
```

`value`의 값으로 `5`를, `unit_label`의 값으로 `'h'`를 사용하여 함수를 호출했으므로 프로그램 출력에는 해당 값이 포함됩니다.
