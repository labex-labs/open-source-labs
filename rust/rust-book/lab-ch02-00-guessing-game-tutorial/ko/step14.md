# 추측을 비밀 번호와 비교하기

이제 사용자 입력과 난수가 있으므로 이를 비교할 수 있습니다. 해당 단계는 Listing 2-4 에 나와 있습니다. 이 코드는 아직 컴파일되지 않으며, 그 이유는 곧 설명하겠습니다.

파일 이름: `src/main.rs`

```rust
use rand::Rng;
1 use std::cmp::Ordering;
use std::io;

fn main() {
    --snip--

    println!("You guessed: {guess}");

  2 match guess.3 cmp(&secret_number) {
        Ordering::Less => println!("Too small!"),
        Ordering::Greater => println!("Too big!"),
        Ordering::Equal => println!("You win!"),
    }
}
```

Listing 2-4: 두 숫자를 비교하여 가능한 반환 값 처리하기

먼저 `std::cmp::Ordering`이라는 유형을 표준 라이브러리에서 범위 내로 가져오는 또 다른 `use` 문 \[1]을 추가합니다. `Ordering` 유형은 또 다른 열거형 (enum) 이며 `Less`, `Greater`, `Equal` 변형을 갖습니다. 이는 두 값을 비교할 때 가능한 세 가지 결과입니다.

그런 다음 `Ordering` 유형을 사용하는 다섯 줄을 추가합니다. `cmp` 메서드 \[3]는 두 값을 비교하며 비교할 수 있는 모든 항목에서 호출할 수 있습니다. 비교하려는 항목에 대한 참조를 사용합니다. 여기서는 `guess`를 `secret_number`와 비교합니다. 그런 다음 `use` 문으로 범위 내로 가져온 `Ordering` 열거형의 변형을 반환합니다. `match` 표현식 \[2]을 사용하여 `guess`와 `secret_number`의 값으로 `cmp`를 호출하여 반환된 `Ordering`의 변형에 따라 다음에 수행할 작업을 결정합니다.

`match` 표현식은 *arm*으로 구성됩니다. arm 은 일치시킬 *pattern*과 `match`에 제공된 값이 해당 arm 의 패턴에 맞는 경우 실행해야 하는 코드로 구성됩니다. Rust 는 `match`에 제공된 값을 가져와 각 arm 의 패턴을 차례로 확인합니다. 패턴과 `match` 구문은 강력한 Rust 기능입니다. 이를 통해 코드가 발생할 수 있는 다양한 상황을 표현하고 모든 상황을 처리할 수 있습니다. 이러한 기능은 각각 6 장과 18 장에서 자세히 다룰 것입니다.

여기서 사용하는 `match` 표현식의 예제를 살펴보겠습니다. 사용자가 50 을 추측했고 이번에 무작위로 생성된 비밀 번호가 38 이라고 가정해 보겠습니다.

코드가 50 을 38 과 비교하면 `cmp` 메서드는 50 이 38 보다 크기 때문에 `Ordering::Greater`를 반환합니다. `match` 표현식은 `Ordering::Greater` 값을 가져와 각 arm 의 패턴을 확인하기 시작합니다. 첫 번째 arm 의 패턴인 `Ordering::Less`를 보고 `Ordering::Greater` 값이 `Ordering::Less`와 일치하지 않으므로 해당 arm 의 코드를 무시하고 다음 arm 으로 이동합니다. 다음 arm 의 패턴은 `Ordering::Greater`이며, 이는 `Ordering::Greater`와 *일치*합니다! 해당 arm 의 관련 코드가 실행되어 화면에 `Too big!`을 출력합니다. `match` 표현식은 첫 번째 성공적인 일치 후 종료되므로 이 시나리오에서는 마지막 arm 을 보지 않습니다.

그러나 Listing 2-4 의 코드는 아직 컴파일되지 않습니다. 시도해 보겠습니다.

```bash
$ cargo build
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
error[E0308]: mismatched types
  --> src/main.rs:22:21
   |
22 |     match guess.cmp(&secret_number) {
   |                     ^^^^^^^^^^^^^^ expected struct `String`, found integer
   |
   = note: expected reference `&String`
              found reference `&{integer}`
```

오류의 핵심은 *유형 불일치*가 있다는 것입니다. Rust 는 강력하고 정적인 유형 시스템을 가지고 있습니다. 그러나 유형 추론도 있습니다. `let mut guess = String::new()`을 작성했을 때 Rust 는 `guess`가 `String`이어야 함을 추론할 수 있었고 유형을 작성하지 않아도 되었습니다. 반면에 `secret_number`는 숫자 유형입니다. Rust 의 몇 가지 숫자 유형은 1 과 100 사이의 값을 가질 수 있습니다. `i32`는 32 비트 숫자, `u32`는 부호 없는 32 비트 숫자, `i64`는 64 비트 숫자 등입니다. 달리 지정하지 않는 한 Rust 는 `i32`를 기본값으로 사용하며, 이는 Rust 가 다른 숫자 유형을 추론하도록 하는 다른 유형 정보를 추가하지 않는 한 `secret_number`의 유형입니다. 오류의 이유는 Rust 가 문자열과 숫자 유형을 비교할 수 없기 때문입니다.

궁극적으로 프로그램이 입력으로 읽는 `String`을 실제 숫자 유형으로 변환하여 비밀 번호와 수치적으로 비교하려고 합니다. 이를 위해 `main` 함수 본문에 다음 줄을 추가합니다.

파일 이름: `src/main.rs`

```rust
use std::io;
use rand::Rng;
use std::cmp::Ordering;

fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1..=100);

    println!("The secret number is: {secret_number}");

    println!("Please input your guess.");

    let mut guess = String::new();

    io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");

    let guess: u32 = guess
        .trim()
        .parse()
        .expect("Please type a number!");

    println!("You guessed: {guess}");

    match guess.cmp(&secret_number) {
        Ordering::Less => println!("Too small!"),
        Ordering::Greater => println!("Too big!"),
        Ordering::Equal => println!("You win!"),
    }
}
```

`guess`라는 변수를 만듭니다. 하지만 잠깐, 프로그램에 이미 `guess`라는 변수가 있지 않습니까? 그렇습니다. 하지만 Rust 는 이전 `guess` 값을 새 값으로 섀도잉할 수 있습니다. *섀도잉*을 사용하면 예를 들어 `guess_str` 및 `guess`와 같이 두 개의 고유한 변수를 만들 필요 없이 `guess` 변수 이름을 재사용할 수 있습니다. 이에 대해서는 3 장에서 자세히 다루겠지만, 지금은 이 기능이 한 유형의 값을 다른 유형으로 변환하려는 경우에 자주 사용된다는 것을 알아두십시오.

이 새 변수를 표현식 `guess.trim().parse()`에 바인딩합니다. 표현식의 `guess`는 입력을 문자열로 포함하는 원래 `guess` 변수를 참조합니다. `String` 인스턴스의 `trim` 메서드는 시작과 끝의 모든 공백을 제거합니다. 이는 문자열을 숫자 데이터만 포함할 수 있는 `u32`와 비교하기 위해 수행해야 합니다. 사용자는 `read_line`을 충족하고 추측을 입력하기 위해 Enter 키를 눌러야 하며, 이는 문자열에 줄 바꿈 문자를 추가합니다. 예를 들어 사용자가 `5`를 입력하고 Enter 키를 누르면 `guess`는 다음과 같습니다. `5\n`. `\n`은 "줄 바꿈"을 나타냅니다. (Windows 에서는 Enter 키를 누르면 캐리지 리턴과 줄 바꿈, `\r\n`이 발생합니다.) `trim` 메서드는 `\n` 또는 `\r\n`을 제거하여 `5`만 남습니다.

문자열의 `parse` 메서드는 문자열을 다른 유형으로 변환합니다. 여기서는 문자열에서 숫자로 변환하는 데 사용합니다. `let guess: u32`를 사용하여 원하는 정확한 숫자 유형을 Rust 에 알려야 합니다. `guess` 뒤의 콜론 (`:`) 은 Rust 에 변수의 유형을 주석 처리하라고 알려줍니다. Rust 에는 몇 가지 내장 숫자 유형이 있습니다. 여기서 보이는 `u32`는 부호 없는 32 비트 정수입니다. 작은 양수에 대한 좋은 기본 선택입니다. 3 장에서 다른 숫자 유형에 대해 배우게 됩니다.

또한 이 예제 프로그램의 `u32` 주석과 `secret_number`와의 비교는 Rust 가 `secret_number`도 `u32`여야 함을 추론한다는 것을 의미합니다. 이제 비교는 동일한 유형의 두 값 사이에서 이루어집니다!

`parse` 메서드는 논리적으로 숫자로 변환할 수 있는 문자에 대해서만 작동하므로 쉽게 오류가 발생할 수 있습니다. 예를 들어 문자열에 `A`👍`%`가 포함된 경우 이를 숫자로 변환할 방법이 없습니다. 실패할 수 있으므로 `parse` 메서드는 `read_line` 메서드와 마찬가지로 `Result` 유형을 반환합니다 ("Result 로 잠재적 실패 처리"에서 설명). `expect` 메서드를 다시 사용하여 이 `Result`를 동일하게 처리합니다. `parse`가 문자열에서 숫자를 만들 수 없기 때문에 `Err` `Result` 변형을 반환하면 `expect` 호출이 게임을 중단하고 제공한 메시지를 출력합니다. `parse`가 문자열을 숫자로 성공적으로 변환할 수 있으면 `Result`의 `Ok` 변형을 반환하고 `expect`는 `Ok` 값에서 원하는 숫자를 반환합니다.

이제 프로그램을 실행해 보겠습니다.

```bash
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 0.43s
     Running `target/debug/guessing_game`
Guess the number!
The secret number is: 58
Please input your guess.
  76
You guessed: 76
Too big!
```

좋아요! 추측 앞에 공백이 추가되었지만 프로그램은 사용자가 76 을 추측했다는 것을 여전히 알아냈습니다. 프로그램을 몇 번 실행하여 다양한 종류의 입력에 대한 다른 동작을 확인하십시오. 숫자를 올바르게 추측하고, 너무 높은 숫자를 추측하고, 너무 낮은 숫자를 추측합니다.

이제 게임의 대부분이 작동하지만 사용자는 한 번만 추측할 수 있습니다. 루프를 추가하여 변경해 보겠습니다!
