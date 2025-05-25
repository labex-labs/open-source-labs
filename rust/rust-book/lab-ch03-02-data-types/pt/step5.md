# Operações Numéricas

Rust suporta as operações matemáticas básicas que você esperaria para todos os tipos de números: adição, subtração, multiplicação, divisão e resto. A divisão de inteiros trunca em direção a zero para o inteiro mais próximo. O código a seguir mostra como você usaria cada operação numérica em uma declaração `let`:

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    // adição
    let sum = 5 + 10;

    // subtração
    let difference = 95.5 - 4.3;

    // multiplicação
    let product = 4 * 30;

    // divisão
    let quotient = 56.7 / 32.2;
    let truncated = -5 / 3; // Resulta em -1

    // resto
    let remainder = 43 % 5;
}
```

Cada expressão nestas declarações usa um operador matemático e é avaliada como um único valor, que é então vinculado a uma variável. O Apêndice B contém uma lista de todos os operadores que o Rust fornece.
