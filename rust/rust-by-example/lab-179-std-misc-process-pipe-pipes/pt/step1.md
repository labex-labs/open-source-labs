# Pipes

A estrutura `std::Child` representa um processo filho em execução e expõe as manipulações `stdin`, `stdout` e `stderr` para interação com o processo subjacente por meio de pipes.

```rust
use std::io::prelude::*;
use std::process::{Command, Stdio};

static PANGRAM: &'static str =
"the quick brown fox jumped over the lazy dog\n";

fn main() {
    // Inicia o comando `wc`
    let process = match Command::new("wc")
                                .stdin(Stdio::piped())
                                .stdout(Stdio::piped())
                                .spawn() {
        Err(why) => panic!("não foi possível iniciar wc: {}", why),
        Ok(process) => process,
    };

    // Escreve uma string no `stdin` de `wc`.
    //
    // `stdin` tem tipo `Option<ChildStdin>`, mas como sabemos que esta instância
    // deve ter um, podemos descompactá-lo diretamente.
    match process.stdin.unwrap().write_all(PANGRAM.as_bytes()) {
        Err(why) => panic!("não foi possível escrever no stdin de wc: {}", why),
        Ok(_) => println!("pangrama enviado para wc"),
    }

    // Como `stdin` não persiste após as chamadas acima, ele é descartado
    // e o pipe é fechado.
    //
    // Isso é muito importante, caso contrário, `wc` não processaria a
    // entrada que acabamos de enviar.

    // O campo `stdout` também tem tipo `Option<ChildStdout>`, portanto, deve ser descompactado.
    let mut s = String::new();
    match process.stdout.unwrap().read_to_string(&mut s) {
        Err(why) => panic!("não foi possível ler o stdout de wc: {}", why),
        Ok(_) => print!("wc respondeu com:\n{}", s),
    }
}
```
