# 子プロセス

`process::Output` 構造体は、完了した子プロセスの出力を表し、`process::Command` 構造体はプロセスビルダーです。

```rust
use std::process::Command;

fn main() {
    let output = Command::new("rustc")
     .arg("--version")
     .output().unwrap_or_else(|e| {
            panic!("failed to execute process: {}", e)
    });

    if output.status.success() {
        let s = String::from_utf8_lossy(&output.stdout);

        print!("rustc succeeded and stdout was:\n{}", s);
    } else {
        let s = String::from_utf8_lossy(&output.stderr);

        print!("rustc failed and stderr was:\n{}", s);
    }
}
```

(`rustc` に渡される不正なフラグを使用して、前の例を試してみることをお勧めします)
