# 추측 처리

숫자 맞추기 게임 프로그램의 첫 번째 부분은 사용자 입력을 요청하고, 해당 입력을 처리하며, 입력이 예상된 형식인지 확인합니다. 먼저 플레이어가 추측을 입력하도록 허용합니다. Listing 2-1 의 코드를 `src/main.rs`에 입력하십시오.

파일 이름: `src/main.rs`

```rust
use std::io;

fn main() {
    println!("Guess the number!");

    println!("Please input your guess.");

    let mut guess = String::new();

    io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");

    println!("You guessed: {guess}");
}
```

Listing 2-1: 사용자로부터 추측을 얻어 출력하는 코드

이 코드는 많은 정보를 포함하고 있으므로 한 줄씩 살펴보겠습니다. 사용자 입력을 얻은 다음 결과를 출력으로 인쇄하려면 `io` 입/출력 라이브러리를 범위 내로 가져와야 합니다. `io` 라이브러리는 `std`로 알려진 표준 라이브러리에서 제공됩니다.

```rust
use std::io;
```

기본적으로 Rust 에는 모든 프로그램의 범위 내로 가져오는 표준 라이브러리에 정의된 일련의 항목이 있습니다. 이 세트는 *prelude*라고 하며, *https://doc.rust-lang.org/std/prelude/index.html*에서 모든 것을 볼 수 있습니다.

사용하려는 타입이 prelude 에 없으면 `use` 문을 사용하여 해당 타입을 명시적으로 범위 내로 가져와야 합니다. `std::io` 라이브러리를 사용하면 사용자 입력을 허용하는 기능을 포함하여 여러 유용한 기능을 사용할 수 있습니다.

1 장에서 보았듯이 `main` 함수는 프로그램의 진입점입니다.

```rust
fn main() {
```

`fn` 구문은 새 함수를 선언합니다. 괄호, `()`,는 매개변수가 없음을 나타냅니다. 중괄호, `{`,는 함수의 본문을 시작합니다.

또한 1 장에서 배운 것처럼 `println!`은 화면에 문자열을 출력하는 매크로입니다.

```rust
println!("Guess the number!");

println!("Please input your guess.");
```

이 코드는 게임이 무엇인지 설명하고 사용자 입력을 요청하는 프롬프트를 출력합니다.
