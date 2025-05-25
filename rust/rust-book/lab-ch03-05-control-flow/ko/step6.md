# loop 를 사용한 코드 반복

`loop` 키워드는 Rust 에게 코드 블록을 영원히 또는 명시적으로 중지하라고 지시할 때까지 반복해서 실행하도록 지시합니다.

예를 들어, `loops` 디렉토리의 `src/main.rs` 파일을 다음과 같이 변경하십시오.

파일 이름: `src/main.rs`

```rust
fn main() {
    loop {
        println!("again!");
    }
}
```

이 프로그램을 실행하면 프로그램을 수동으로 중지할 때까지 `again!`이 계속해서 반복적으로 출력되는 것을 볼 수 있습니다. 대부분의 터미널은 지속적인 루프에 갇힌 프로그램을 중단하기 위해 키보드 단축키 ctrl-C 를 지원합니다. 시도해 보십시오.

```bash
$ cargo run
   Compiling loops v0.1.0 (file:///projects/loops)
    Finished dev [unoptimized + debuginfo] target(s) in 0.29s
     Running `target/debug/loops`
again!
again!
again!
again!
^Cagain!
```

기호 `^C`는 ctrl-C 를 누른 위치를 나타냅니다. 인터럽트 신호를 받았을 때 코드가 루프의 어디에 있었는지에 따라 `^C` 뒤에 `again!`이라는 단어가 표시될 수도 있고 그렇지 않을 수도 있습니다.

다행히 Rust 는 코드 사용을 통해 루프에서 벗어나는 방법도 제공합니다. `break` 키워드를 루프 안에 배치하여 프로그램에 루프 실행을 중지할 시점을 알릴 수 있습니다. "정답 추측 후 종료"에서 사용자가 정답을 맞춰 게임에서 이겼을 때 프로그램을 종료하기 위해 이 작업을 수행했음을 기억하십시오.

또한 추측 게임에서 `continue`를 사용했는데, 루프에서 이 키워드는 프로그램에 루프의 이 반복에서 남은 코드를 건너뛰고 다음 반복으로 이동하도록 지시합니다.
