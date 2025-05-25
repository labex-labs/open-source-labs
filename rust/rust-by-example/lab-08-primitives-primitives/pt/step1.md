# Primitivas

O Rust fornece acesso a uma ampla variedade de `primitivas`. Uma amostra inclui:

## Tipos Escalares

- Inteiros com sinal: `i8`, `i16`, `i32`, `i64`, `i128` e `isize` (tamanho do ponteiro)
- Inteiros sem sinal: `u8`, `u16`, `u32`, `u64`, `u128` e `usize` (tamanho do ponteiro)
- Ponto flutuante: `f32`, `f64`
- `char` Valores escalares Unicode como `'a'`, `'α'` e `'∞'` (4 bytes cada)
- `bool` (booleano) - `true` ou `false`
- O tipo unitário `()`, cujo único valor possível é uma tupla vazia: `()`

Apesar do valor de um tipo unitário ser uma tupla, ele não é considerado um tipo composto porque não contém múltiplos valores.

## Tipos Compostos

- Arrays como `[1, 2, 3]`
- Tuplas como `(1, true)`

Variáveis podem sempre ser _anotadas com tipos_. Números podem, adicionalmente, ser anotados via um _sufixo_ ou _por padrão_. Inteiros são, por padrão, `i32` e floats, `f64`. Note que o Rust também pode inferir tipos a partir do contexto.

```rust
fn main() {
    // Variáveis podem ser anotadas com tipos.
    let logical: bool = true;

    let a_float: f64 = 1.0;  // Anotação regular
    let an_integer   = 5i32; // Anotação com sufixo

    // Ou um padrão será usado.
    let default_float   = 3.0; // `f64`
    let default_integer = 7;   // `i32`

    // Um tipo também pode ser inferido a partir do contexto.
    let mut inferred_type = 12; // Tipo i64 é inferido de outra linha.
    inferred_type = 4294967296i64;

    // O valor de uma variável mutável pode ser alterado.
    let mut mutable = 12; // Mutável `i32`
    mutable = 21;

    // Erro! O tipo de uma variável não pode ser alterado.
    mutable = true;

    // Variáveis podem ser sobrescritas com shadowing.
    let mutable = true;
}
```
