# 난수 생성하기

`rand`를 사용하여 추측할 숫자를 생성해 보겠습니다. 다음 단계는 Listing 2-3 에 표시된 대로 `src/main.rs`를 업데이트하는 것입니다.

파일 이름: `src/main.rs`

```rust
use std::io;
1 use rand::Rng;

fn main() {
    println!("Guess the number!");

  2 let secret_number = rand::thread_rng().gen_range(1..=100);

  3 println!("The secret number is: {secret_number}");

    println!("Please input your guess.");

    let mut guess = String::new();

    io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");

    println!("You guessed: {guess}");
}
```

Listing 2-3: 난수를 생성하는 코드 추가

먼저 `use rand::Rng;` 라인 \[1]을 추가합니다. `Rng` 트레이트는 난수 생성기가 구현하는 메서드를 정의하며, 이러한 메서드를 사용하려면 이 트레이트가 범위 내에 있어야 합니다. 10 장에서 트레이트에 대해 자세히 다룰 것입니다.

다음으로, 중간에 두 줄을 추가하고 있습니다. 첫 번째 줄 \[2]에서, 사용할 특정 난수 생성기를 제공하는 `rand::thread_rng` 함수를 호출합니다. 이 함수는 현재 실행 스레드에 로컬이며 운영 체제에 의해 시드됩니다. 그런 다음 난수 생성기에서 `gen_range` 메서드를 호출합니다. 이 메서드는 `use rand::Rng;` 문을 사용하여 범위 내로 가져온 `Rng` 트레이트에 의해 정의됩니다. `gen_range` 메서드는 범위 표현식을 인수로 받아 해당 범위 내에서 난수를 생성합니다. 여기서 사용하는 범위 표현식은 `start..=end` 형식을 취하며 하한 및 상한을 포함하므로 1 과 100 사이의 숫자를 요청하려면 `1..=100`을 지정해야 합니다.

> 참고: 어떤 트레이트를 사용하고 어떤 메서드와 함수를 크레이트에서 호출해야 하는지 정확히 알 수는 없으므로, 각 크레이트에는 사용 지침이 포함된 문서가 있습니다. Cargo 의 또 다른 멋진 기능은 `cargo doc --open` 명령을 실행하면 모든 종속성에서 제공하는 문서를 로컬로 빌드하여 브라우저에서 열어준다는 것입니다. 예를 들어, `rand` 크레이트의 다른 기능에 관심이 있다면 `cargo doc --open`을 실행하고 왼쪽 사이드바에서 `rand`를 클릭하십시오.

두 번째 새 줄 \[3]은 비밀 번호를 출력합니다. 프로그램을 테스트할 수 있도록 프로그램을 개발하는 동안 유용하지만, 최종 버전에서는 삭제할 것입니다. 프로그램이 시작하자마자 답을 출력한다면 게임으로서의 의미가 없을 것입니다!

프로그램을 몇 번 실행해 보십시오.

```bash
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 2.53s
     Running `target/debug/guessing_game`
Guess the number!
The secret number is: 7
Please input your guess.
4
You guessed: 4

$ cargo run
    Finished dev [unoptimized + debuginfo] target(s) in 0.02s
     Running `target/debug/guessing_game`
Guess the number!
The secret number is: 83
Please input your guess.
5
You guessed: 5
```

서로 다른 난수를 얻어야 하며, 모두 1 과 100 사이의 숫자여야 합니다. 잘하셨습니다!
