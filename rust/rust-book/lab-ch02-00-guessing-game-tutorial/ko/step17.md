# 잘못된 입력 처리

게임의 동작을 더욱 개선하기 위해 사용자가 숫자가 아닌 값을 입력할 때 프로그램을 충돌시키는 대신, 게임이 숫자가 아닌 값을 무시하여 사용자가 계속 추측할 수 있도록 하겠습니다. Listing 2-5 에 표시된 대로 `guess`가 `String`에서 `u32`로 변환되는 줄을 변경하여 이를 수행할 수 있습니다.

파일 이름: `src/main.rs`

```rust
--snip--

io::stdin()
    .read_line(&mut guess)
    .expect("Failed to read line");

let guess: u32 = match guess.trim().parse() {
    Ok(num) => num,
    Err(_) => continue,
};

println!("You guessed: {guess}");

--snip--
```

Listing 2-5: 프로그램 충돌 대신 숫자가 아닌 추측을 무시하고 다른 추측을 요청합니다.

`expect` 호출에서 `match` 표현식으로 전환하여 오류 발생 시 충돌하는 대신 오류를 처리합니다. `parse`가 `Result` 타입을 반환하고 `Result`는 `Ok`와 `Err` 변형을 갖는 열거형 (enum) 임을 기억하십시오. `cmp` 메서드의 `Ordering` 결과와 마찬가지로 여기에서 `match` 표현식을 사용하고 있습니다.

`parse`가 문자열을 숫자로 성공적으로 변환할 수 있다면 결과 숫자를 포함하는 `Ok` 값을 반환합니다. 해당 `Ok` 값은 첫 번째 arm 의 패턴과 일치하고, `match` 표현식은 `parse`가 생성하여 `Ok` 값 안에 넣은 `num` 값만 반환합니다. 해당 숫자는 우리가 만들고 있는 새로운 `guess` 변수에서 원하는 위치에 정확히 위치하게 됩니다.

`parse`가 문자열을 숫자로 변환할 수 _없다면_ 오류에 대한 더 많은 정보를 포함하는 `Err` 값을 반환합니다. `Err` 값은 첫 번째 `match` arm 의 `Ok(num)` 패턴과 일치하지 않지만 두 번째 arm 의 `Err(_)` 패턴과 일치합니다. 밑줄, `_`는 모든 값을 포괄하는 값입니다. 이 예에서는 모든 `Err` 값과 일치시키려고 합니다. 즉, 그 안에 어떤 정보가 있든 상관없이 일치시키려고 합니다. 따라서 프로그램은 두 번째 arm 의 코드인 `continue`를 실행합니다. 이는 프로그램이 `loop`의 다음 반복으로 이동하여 다른 추측을 요청하도록 지시합니다. 따라서 프로그램은 `parse`가 발생할 수 있는 모든 오류를 효과적으로 무시합니다!

이제 프로그램의 모든 것이 예상대로 작동해야 합니다. 시도해 보겠습니다.

```bash
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 4.45s
     Running `target/debug/guessing_game`
Guess the number!
The secret number is: 61
Please input your guess.
10
You guessed: 10
Too small!
Please input your guess.
99
You guessed: 99
Too big!
Please input your guess.
foo
Please input your guess.
61
You guessed: 61
You win!
```

훌륭합니다! 마지막 작은 조정을 통해 추측 게임을 완료할 것입니다. 프로그램이 여전히 비밀 번호를 출력하고 있음을 기억하십시오. 이는 테스트에는 좋았지만 게임을 망칩니다. 비밀 번호를 출력하는 `println!`을 삭제해 보겠습니다. Listing 2-6 은 최종 코드를 보여줍니다.

파일 이름: `src/main.rs`

```rust
use rand::Rng;
use std::cmp::Ordering;
use std::io;

fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1..=100);

    loop {
        println!("Please input your guess.");

        let mut guess = String::new();

        io::stdin()
            .read_line(&mut guess)
            .expect("Failed to read line");

        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        println!("You guessed: {guess}");

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => {
                println!("You win!");
                break;
            }
        }
    }
}
```

Listing 2-6: 완성된 추측 게임 코드

이 시점에서 추측 게임을 성공적으로 구축했습니다. 축하합니다!
