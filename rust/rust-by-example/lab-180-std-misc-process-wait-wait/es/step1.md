# Esperar

Si quieres esperar a que un `process::Child` termine, debes llamar a `Child::wait`, que devolverá un `process::ExitStatus`.

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
# `wait` sigue ejecutándose durante 5 segundos hasta que el comando `sleep 5` finaliza
reached end of main
```
