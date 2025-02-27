# Tuberías

La estructura `std::Child` representa un proceso hijo en ejecución y expone los manejadores `stdin`, `stdout` y `stderr` para interactuar con el proceso subyacente a través de tuberías.

```rust
use std::io::prelude::*;
use std::process::{Command, Stdio};

static PANGRAM: &'static str =
"the quick brown fox jumped over the lazy dog\n";

fn main() {
    // Lanzar el comando `wc`
    let proceso = match Command::new("wc")
                             .stdin(Stdio::piped())
                             .stdout(Stdio::piped())
                             .spawn() {
        Err(porqué) => panic!("no se pudo lanzar wc: {}", porqué),
        Ok(proceso) => proceso,
    };

    // Escribir una cadena en el `stdin` de `wc`.
    //
    // `stdin` tiene tipo `Option<ChildStdin>`, pero como sabemos que esta instancia
    // debe tener uno, podemos directamente `unwrap`arlo.
    match proceso.stdin.unwrap().write_all(PANGRAM.as_bytes()) {
        Err(porqué) => panic!("no se pudo escribir en el stdin de wc: {}", porqué),
        Ok(_) => println!("se envió el pangrama a wc"),
    }

    // Debido a que `stdin` no existe después de las llamadas anteriores, se `drop`ea,
    // y la tubería se cierra.
    //
    // Esto es muy importante, de lo contrario `wc` no comenzaría a procesar la
    // entrada que acabamos de enviar.

    // El campo `stdout` también tiene tipo `Option<ChildStdout>` por lo que debe ser desenvuelto.
    let mut s = String::new();
    match proceso.stdout.unwrap().read_to_string(&mut s) {
        Err(porqué) => panic!("no se pudo leer el stdout de wc: {}", porqué),
        Ok(_) => print!("wc respondió con:\n{}", s),
    }
}
```
