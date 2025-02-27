# 待機

`process::Child` が終了するのを待ちたい場合は、`Child::wait` を呼び出す必要があります。これにより、`process::ExitStatus` が返されます。

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
# `wait` は、`sleep 5` コマンドが終了するまで5秒間実行され続けます
reached end of main
```
