# 함수 (Functions)

함수는 Rust 코드에서 널리 사용됩니다. 이미 언어에서 가장 중요한 함수 중 하나인 `main` 함수를 보셨을 것입니다. 이는 많은 프로그램의 진입점입니다. 또한 새로운 함수를 선언할 수 있는 `fn` 키워드도 보셨습니다.

`functions`라는 새 프로젝트를 만듭니다.

```bash
cargo new functions
cd functions
```

Rust 코드는 함수 및 변수 이름에 대한 일반적인 스타일로 *snake case*를 사용합니다. 여기서 모든 문자는 소문자이고 밑줄 (\_) 은 단어를 구분합니다. 다음은 함수 정의의 예가 포함된 프로그램입니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    println!("Hello, world!");

    another_function();
}

fn another_function() {
    println!("Another function.");
}
```

Rust 에서 함수를 정의하려면 `fn`을 입력한 다음 함수 이름과 괄호 세트를 입력합니다. 중괄호는 컴파일러에게 함수 본문이 시작되고 끝나는 위치를 알려줍니다.

괄호 세트를 입력한 다음 이름을 입력하여 정의한 모든 함수를 호출할 수 있습니다. `another_function`이 프로그램에 정의되어 있으므로 `main` 함수 내에서 호출할 수 있습니다. `another_function`을 소스 코드에서 `main` 함수 _뒤에_ 정의했음을 유의하세요. 앞서 정의할 수도 있었습니다. Rust 는 함수를 어디에 정의했는지 신경 쓰지 않고, 호출자가 볼 수 있는 범위 내에서 정의되었는지 여부만 확인합니다.

함수를 더 자세히 탐구하기 위해 *functions*라는 새 바이너리 프로젝트를 시작해 보겠습니다. `another_function` 예제를 `src/main.rs`에 넣고 실행합니다. 다음 출력이 표시됩니다.

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
    Finished dev [unoptimized + debuginfo] target(s) in 0.28s
     Running `target/debug/functions`
Hello, world!
Another function.
```

줄은 `main` 함수에 나타나는 순서대로 실행됩니다. 먼저 "Hello, world!" 메시지가 인쇄된 다음 `another_function`이 호출되고 해당 메시지가 인쇄됩니다.
