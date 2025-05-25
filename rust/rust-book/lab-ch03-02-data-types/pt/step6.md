# O Tipo Booleano

Como na maioria das outras linguagens de programação, um tipo booleano em Rust tem dois valores possíveis: `true` e `false`. Booleanos têm um byte de tamanho. O tipo booleano em Rust é especificado usando `bool`. Por exemplo:

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let t = true;

    let f: bool = false; // com anotação de tipo explícita
}
```

A principal forma de usar valores booleanos é através de condicionais, como uma expressão `if`. Abordaremos como as expressões `if` funcionam em Rust em "Fluxo de Controle".
