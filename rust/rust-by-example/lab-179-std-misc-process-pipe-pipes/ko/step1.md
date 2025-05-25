# 파이프

`std::Child` 구조체는 실행 중인 자식 프로세스를 나타내며, 파이프를 통해 기본 프로세스와 상호 작용하기 위한 `stdin`, `stdout` 및 `stderr` 핸들을 노출합니다.

```rust
use std::io::prelude::*;
use std::process::{Command, Stdio};

static PANGRAM: &'static str =
"the quick brown fox jumped over the lazy dog\n";

fn main() {
    // `wc` 명령어를 생성합니다.
    let process = match Command::new("wc")
                                .stdin(Stdio::piped())
                                .stdout(Stdio::piped())
                                .spawn() {
        Err(why) => panic!("couldn't spawn wc: {}", why),
        Ok(process) => process,
    };

    // `wc` 의 `stdin` 에 문자열을 씁니다.
    //
    // `stdin` 은 `Option<ChildStdin>` 타입이지만, 이 인스턴스에는 반드시 하나가 있으므로 바로 `unwrap` 할 수 있습니다.
    match process.stdin.unwrap().write_all(PANGRAM.as_bytes()) {
        Err(why) => panic!("couldn't write to wc stdin: {}", why),
        Ok(_) => println!("wc 에 pangram 을 전송했습니다."),
    }

    // 위 호출 후 `stdin` 은 더 이상 존재하지 않으므로 `drop` 되고 파이프가 닫힙니다.
    //
    // 이것은 매우 중요하며, 그렇지 않으면 방금 전송한 입력을 `wc` 가 처리하지 않습니다.

    // `stdout` 필드도 `Option<ChildStdout>` 타입이므로 `unwrap` 해야 합니다.
    let mut s = String::new();
    match process.stdout.unwrap().read_to_string(&mut s) {
        Err(why) => panic!("couldn't read wc stdout: {}", why),
        Ok(_) => print!("wc 가 응답했습니다:\n{}", s),
    }
}
```
