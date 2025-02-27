# Procesos hijos

La estructura `process::Output` representa la salida de un proceso hijo finalizado, y la estructura `process::Command` es un constructor de procesos.

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

(Se le anima a probar el ejemplo anterior con una bandera incorrecta pasada a `rustc`)
