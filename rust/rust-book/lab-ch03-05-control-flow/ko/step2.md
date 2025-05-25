# if 표현식 (Expressions)

`if` 표현식을 사용하면 조건에 따라 코드를 분기할 수 있습니다. 조건을 제공한 다음 "이 조건이 충족되면 이 코드 블록을 실행합니다. 조건이 충족되지 않으면 이 코드 블록을 실행하지 않습니다."라고 명시합니다.

`if` 표현식을 탐색하기 위해 `project` 디렉토리에서 `branches`라는 새 프로젝트를 만듭니다. `src/main.rs` 파일에 다음을 입력합니다.

```bash
cd ~/project
cargo new branches
```

파일 이름: `src/main.rs`

```rust
fn main() {
    let number = 3;

    if number < 5 {
        println!("condition was true");
    } else {
        println!("condition was false");
    }
}
```

모든 `if` 표현식은 키워드 `if`로 시작하고, 그 뒤에 조건이 옵니다. 이 경우 조건은 변수 `number`의 값이 5 미만인지 확인합니다. 조건이 `true`인 경우 실행할 코드 블록을 중괄호 안에 조건 바로 뒤에 배치합니다. `if` 표현식의 조건과 관련된 코드 블록은 때때로 "Guess 를 Secret Number 와 비교하기"에서 논의한 `match` 표현식의 arm 과 마찬가지로 *arm*이라고도 합니다.

선택적으로, 조건이 `false`로 평가될 경우 실행할 대체 코드 블록을 프로그램에 제공하기 위해 여기에서 선택한 `else` 표현식을 포함할 수도 있습니다. `else` 표현식을 제공하지 않고 조건이 `false`이면 프로그램은 `if` 블록을 건너뛰고 다음 코드 비트로 이동합니다.

이 코드를 실행해 보십시오. 다음 출력이 표시됩니다.

```bash
$ cargo run
   Compiling branches v0.1.0 (file:///projects/branches)
    Finished dev [unoptimized + debuginfo] target(s) in 0.31s
     Running `target/debug/branches`
condition was true
```

`number`의 값을 조건이 `false`가 되도록 변경하여 어떤 일이 발생하는지 살펴보겠습니다.

```rust
    let number = 7;
```

프로그램을 다시 실행하고 출력을 확인합니다.

```bash
$ cargo run
   Compiling branches v0.1.0 (file:///projects/branches)
    Finished dev [unoptimized + debuginfo] target(s) in 0.31s
     Running `target/debug/branches`
condition was false
```

또한 이 코드의 조건은 _반드시_ `bool`이어야 한다는 점에 유의해야 합니다. 조건이 `bool`이 아니면 오류가 발생합니다. 예를 들어, 다음 코드를 실행해 보십시오.

파일 이름: `src/main.rs`

```rust
fn main() {
    let number = 3;

    if number {
        println!("number was three");
    }
}
```

`if` 조건은 이번에는 `3`의 값으로 평가되고 Rust 는 오류를 발생시킵니다.

```bash
$ cargo run
   Compiling branches v0.1.0 (file:///projects/branches)
error[E0308]: mismatched types
 --> src/main.rs:4:8
  |
4 |     if number {
  |        ^^^^^^ expected `bool`, found integer
```

오류는 Rust 가 `bool`을 예상했지만 정수를 받았음을 나타냅니다. Ruby 및 JavaScript 와 같은 언어와 달리 Rust 는 부울이 아닌 유형을 자동으로 부울로 변환하려고 시도하지 않습니다. 명시적으로 항상 `if`에 부울을 조건으로 제공해야 합니다. 예를 들어, 숫자가 `0`과 같지 않을 때만 `if` 코드 블록이 실행되도록 하려면 `if` 표현식을 다음과 같이 변경할 수 있습니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let number = 3;

    if number != 0 {
        println!("number was something other than zero");
    }
}
```

이 코드를 실행하면 `number was something other than zero`가 출력됩니다.
