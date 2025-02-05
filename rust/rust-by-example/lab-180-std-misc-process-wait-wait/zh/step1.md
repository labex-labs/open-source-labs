# 等待

如果你想要等待一个 `process::Child` 进程结束，你必须调用 `Child::wait`，它会返回一个 `process::ExitStatus`。

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
# `wait` 会持续运行5秒钟，直到 `sleep 5` 命令完成
reached end of main
```
