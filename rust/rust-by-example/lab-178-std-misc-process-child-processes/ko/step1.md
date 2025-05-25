# 자식 프로세스

`process::Output` 구조체는 완료된 자식 프로세스의 출력을 나타내고, `process::Command` 구조체는 프로세스 생성자입니다.

```rust
use std::process::Command;

fn main() {
    let output = Command::new("rustc")
        .arg("--version")
        .output().unwrap_or_else(|e| {
            panic!("프로세스 실행 실패: {}", e)
    });

    if output.status.success() {
        let s = String::from_utf8_lossy(&output.stdout);

        print!("rustc 성공적으로 실행되었으며 stdout 은 다음과 같습니다:\n{}", s);
    } else {
        let s = String::from_utf8_lossy(&output.stderr);

        print!("rustc 실행 실패했으며 stderr 은 다음과 같습니다:\n{}", s);
    }
}
```

(이전 예제를 `rustc`에 잘못된 플래그를 전달하여 실행해 보는 것을 권장합니다.)
