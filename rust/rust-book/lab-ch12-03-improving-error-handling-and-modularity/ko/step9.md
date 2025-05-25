# Config::build 호출 및 오류 처리

오류 사례를 처리하고 사용자 친화적인 메시지를 인쇄하려면 목록 12-10 에 표시된 대로 `Config::build`에서 반환되는 `Result`를 처리하도록 `main`을 업데이트해야 합니다. 또한 `panic!`에서 벗어나 0 이 아닌 오류 코드로 명령줄 도구를 종료하는 책임을 직접 구현할 것입니다. 0 이 아닌 종료 상태는 프로그램이 오류 상태로 종료되었음을 우리 프로그램을 호출한 프로세스에 알리는 규칙입니다.

파일 이름: `src/main.rs`

```rust
1 use std::process;

fn main() {
    let args: Vec<String> = env::args().collect();

  2 let config = Config::build(&args).3 unwrap_or_else(|4 err| {
      5 println!("Problem parsing arguments: {err}");
      6 process::exit(1);
    });

    --snip--
```

목록 12-10: `Config` 빌드에 실패하면 오류 코드로 종료

이 목록에서는 아직 자세히 다루지 않은 메서드인 `unwrap_or_else`를 사용했습니다. 이 메서드는 표준 라이브러리 \[2]에 의해 `Result<T, E>`에서 정의됩니다. `unwrap_or_else`를 사용하면 일부 사용자 정의, 비-`panic!` 오류 처리를 정의할 수 있습니다. `Result`가 `Ok` 값인 경우 이 메서드의 동작은 `unwrap`과 유사합니다. 즉, `Ok`가 래핑하는 내부 값을 반환합니다. 그러나 값이 `Err` 값인 경우 이 메서드는 _클로저_(closure) 의 코드를 호출합니다. 클로저는 우리가 정의하고 `unwrap_or_else`에 인수로 전달하는 익명 함수입니다 \[3]. 클로저는 13 장에서 자세히 다룰 것입니다. 지금은 `unwrap_or_else`가 `Err`의 내부 값, 즉 이 경우 목록 12-9 에서 추가한 정적 문자열 `"not enough arguments"`를 수직 파이프 사이 \[4]에 나타나는 인수 `err`의 클로저에 전달한다는 것만 알면 됩니다. 그런 다음 클로저의 코드는 실행될 때 `err` 값을 사용할 수 있습니다.

표준 라이브러리에서 `process`를 범위 내로 가져오기 위해 새로운 `use` 줄을 추가했습니다 \[1]. 오류의 경우 실행될 클로저의 코드는 두 줄뿐입니다. `err` 값을 인쇄하고 \[5] `process::exit`를 호출합니다 \[6]. `process::exit` 함수는 프로그램을 즉시 중지하고 종료 상태 코드로 전달된 숫자를 반환합니다. 이는 목록 12-8 에서 사용한 `panic!` 기반 처리와 유사하지만 더 이상 모든 추가 출력을 얻지 않습니다. 시도해 보겠습니다.

```bash
$ cargo run
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.48s
     Running `target/debug/minigrep`
Problem parsing arguments: not enough arguments
```

훌륭합니다! 이 출력은 사용자에게 훨씬 더 친숙합니다.
