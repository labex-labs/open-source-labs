# 대기

`process::Child`가 종료될 때까지 기다리려면 `Child::wait`를 호출해야 합니다. 이 함수는 `process::ExitStatus`를 반환합니다.

```rust
use std::process::Command;

fn main() {
    let mut child = Command::new("sleep").arg("5").spawn().unwrap();
    let _result = child.wait().unwrap();

    println!("reached end of main");
}
```

```bash
$ rustc wait.rs && ./wait
# `wait`는 `sleep 5` 명령이 완료될 때까지 5 초 동안 실행됩니다.
reached end of main
```
