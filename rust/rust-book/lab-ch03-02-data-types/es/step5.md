# Operaciones Numéricas

Rust admite las operaciones matemáticas básicas que esperarías para todos los tipos de números: suma, resta, multiplicación, división y residuo. La división entera se trunca hacia cero al entero más cercano. El siguiente código muestra cómo usar cada operación numérica en una declaración `let`:

Nombre del archivo: `src/main.rs`

```rust
fn main() {
    // suma
    let sum = 5 + 10;

    // resta
    let difference = 95.5 - 4.3;

    // multiplicación
    let product = 4 * 30;

    // división
    let quotient = 56.7 / 32.2;
    let truncated = -5 / 3; // Da como resultado -1

    // residuo
    let remainder = 43 % 5;
}
```

Cada expresión en estas declaraciones utiliza un operador matemático y se evalúa a un solo valor, que luego se asocia a una variable. El Apéndice B contiene una lista de todos los operadores que Rust proporciona.
