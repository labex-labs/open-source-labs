# 루프를 사용하여 여러 번 추측 허용하기

`loop` 키워드는 무한 루프를 생성합니다. 사용자가 숫자를 추측할 수 있는 더 많은 기회를 제공하기 위해 루프를 추가하겠습니다.

파일 이름: `src/main.rs`

```rust
use std::io;
use rand::Rng;
use std::cmp::Ordering;

fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1..=100);

    println!("The secret number is: {secret_number}");

    loop {
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
}
```

보시다시피, 추측 입력 프롬프트부터 모든 것을 루프로 이동했습니다. 루프 내부의 줄을 각각 4 칸 더 들여쓰고 프로그램을 다시 실행하십시오. 이제 프로그램은 영원히 다른 추측을 요청할 것이며, 실제로 새로운 문제를 야기합니다. 사용자가 종료할 수 없는 것처럼 보입니다!

사용자는 항상 키보드 단축키 ctrl-C 를 사용하여 프로그램을 중단할 수 있습니다. 하지만 "추측을 비밀 번호와 비교하기"의 `parse` 토론에서 언급했듯이, 이 만족할 줄 모르는 괴물을 탈출하는 또 다른 방법이 있습니다. 사용자가 숫자가 아닌 답을 입력하면 프로그램이 충돌합니다. 이를 활용하여 사용자가 종료할 수 있도록 할 수 있습니다.

```bash
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 1.50s
     Running `target/debug/guessing_game`
Guess the number!
The secret number is: 59
Please input your guess.
45
You guessed: 45
Too small!
Please input your guess.
60
You guessed: 60
Too big!
Please input your guess.
59
You guessed: 59
You win!
Please input your guess.
quit
thread 'main' panicked at 'Please type a number!: ParseIntError
{ kind: InvalidDigit }', src/main.rs:28:47
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
```

`quit`을 입력하면 게임이 종료되지만, 아시다시피 다른 숫자가 아닌 입력을 입력해도 마찬가지입니다. 이는 최적이라고 할 수 없습니다. 올바른 숫자를 추측했을 때도 게임이 중단되기를 원합니다.
