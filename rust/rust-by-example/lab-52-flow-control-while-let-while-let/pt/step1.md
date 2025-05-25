# while let

Similar a `if let`, `while let` pode tornar sequências `match` incômodas mais toleráveis. Considere a seguinte sequência que incrementa `i`:

```rust
// Crie `optional` do tipo `Option<i32>`
let mut optional = Some(0);

// Tente este teste repetidamente.
loop {
    match optional {
        // Se `optional` desestruturar, avalie o bloco.
        Some(i) => {
            if i > 9 {
                println!("Maior que 9, pare!");
                optional = None;
            } else {
                println!("`i` é `{:?}`. Tente novamente.", i);
                optional = Some(i + 1);
            }
            // ^ Requer 3 níveis de indentação!
        },
        // Pare o loop quando a desestruturação falhar:
        _ => { break; }
        // ^ Por que isso é necessário? Deve haver uma maneira melhor!
    }
}
```

Usando `while let`, esta sequência fica muito melhor:

```rust
fn main() {
    // Crie `optional` do tipo `Option<i32>`
    let mut optional = Some(0);

    // Isso lê: "enquanto `let` desestruturar `optional` em
    // `Some(i)`, avalie o bloco (`{}`). Caso contrário, `break`.
    while let Some(i) = optional {
        if i > 9 {
            println!("Maior que 9, pare!");
            optional = None;
        } else {
            println!("`i` é `{:?}`. Tente novamente.", i);
            optional = Some(i + 1);
        }
        // ^ Menos desvio para a direita e não requer
        // o tratamento explícito do caso de falha.
    }
    // ^ `if let` tinha cláusulas opcionais adicionais `else`/`else if`. `while let` não tem essas.
}
```
