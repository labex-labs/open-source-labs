# Aguardar

Se desejar aguardar que um processo `process::Child` termine, você deve chamar `Child::wait`, que retornará um `process::ExitStatus`.

```rust
use std::process::Command;

fn main() {
    let mut child = Command::new("sleep").arg("5").spawn().unwrap();
    let _result = child.wait().unwrap();

    println!("alcançou o fim do main");
}
```

```bash
$ rustc wait.rs && ./wait
# `wait` continua em execução por 5 segundos até que o comando `sleep 5` termine
alcançou o fim do main
```
