# Processos Filhos

A estrutura `process::Output` representa a saída de um processo filho concluído, e a estrutura `process::Command` é um construtor de processos.

```rust
use std::process::Command;

fn main() {
    let output = Command::new("rustc")
        .arg("--version")
        .output().unwrap_or_else(|e| {
            panic!("falha ao executar o processo: {}", e)
    });

    if output.status.success() {
        let s = String::from_utf8_lossy(&output.stdout);

        print!("rustc teve sucesso e a saída padrão foi:\n{}", s);
    } else {
        let s = String::from_utf8_lossy(&output.stderr);

        print!("rustc falhou e a saída de erro foi:\n{}", s);
    }
}
```

(É recomendado tentar o exemplo anterior com um sinalizador incorreto passado para `rustc`)
