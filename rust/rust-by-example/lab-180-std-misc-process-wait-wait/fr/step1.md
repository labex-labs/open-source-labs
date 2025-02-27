# Attendre

Si vous voulez attendre qu'un `process::Child` se termine, vous devez appeler `Child::wait`, qui renverra un `process::ExitStatus`.

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
# `wait` continue de s'exécuter pendant 5 secondes jusqu'à ce que la commande `sleep 5` se termine
reached end of main
```
