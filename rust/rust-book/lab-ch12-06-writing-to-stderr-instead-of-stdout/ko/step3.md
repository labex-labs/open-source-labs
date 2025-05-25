# 오류를 표준 오류에 인쇄하기

Listing 12-24 의 코드를 사용하여 오류 메시지가 인쇄되는 방식을 변경합니다. 이 장의 앞부분에서 수행한 리팩토링으로 인해, 오류 메시지를 인쇄하는 모든 코드는 `main` 함수 하나에 있습니다. 표준 라이브러리는 표준 오류 스트림에 인쇄하는 `eprintln!` 매크로를 제공하므로, 오류를 인쇄하기 위해 `println!`을 호출했던 두 곳을 `eprintln!`을 사용하도록 변경해 보겠습니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

    let config = Config::build(&args).unwrap_or_else(|err| {
        eprintln!("Problem parsing arguments: {err}");
        process::exit(1);
    });

    if let Err(e) = minigrep::run(config) {
        eprintln!("Application error: {e}");
        process::exit(1);
    }
}
```

Listing 12-24: `eprintln!`을 사용하여 오류 메시지를 표준 출력 대신 표준 오류에 작성하기

이제 동일한 방식으로, 인수를 사용하지 않고 표준 출력을 `>`로 리디렉션하여 프로그램을 다시 실행해 보겠습니다.

```bash
$ cargo run > output.txt
Problem parsing arguments: not enough arguments
```

이제 오류가 화면에 표시되고 *output.txt*에는 아무것도 포함되어 있지 않습니다. 이는 명령줄 프로그램에서 예상되는 동작입니다.

오류를 발생시키지 않지만 표준 출력을 파일로 리디렉션하는 인수를 사용하여 프로그램을 다시 실행해 보겠습니다.

```bash
cargo run -- to poem.txt > output.txt
```

터미널에는 아무런 출력도 표시되지 않으며, *output.txt*에는 결과가 포함됩니다.

파일 이름: output.txt

```rust
Are you nobody, too?
How dreary to be somebody!
```

이는 이제 성공적인 출력에는 표준 출력을, 오류 출력에는 표준 오류를 적절하게 사용하고 있음을 보여줍니다.
