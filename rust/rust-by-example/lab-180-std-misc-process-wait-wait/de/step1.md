# Warten

Wenn Sie auf das Beenden eines `process::Child` warten möchten, müssen Sie `Child::wait` aufrufen, was einen `process::ExitStatus` zurückgeben wird.

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
# `wait` läuft 5 Sekunden lang, bis der Befehl `sleep 5` abgeschlossen ist
reached end of main
```
