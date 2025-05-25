# Tipos de Ponto Flutuante

Rust também possui dois tipos primitivos para _números de ponto flutuante_ (floating-point numbers), que são números com casas decimais. Os tipos de ponto flutuante do Rust são `f32` e `f64`, que têm 32 bits e 64 bits de tamanho, respectivamente. O tipo padrão é `f64` porque em CPUs modernas, é aproximadamente a mesma velocidade que `f32`, mas é capaz de mais precisão. Todos os tipos de ponto flutuante são com sinal.

Crie um novo projeto chamado `data-types`:

```bash
cargo new data-types
cd data-types
```

Aqui está um exemplo que mostra números de ponto flutuante em ação:

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let x = 2.0; // f64

    let y: f32 = 3.0; // f32
}
```

Números de ponto flutuante são representados de acordo com o padrão IEEE-754. O tipo `f32` é um float de precisão simples, e `f64` tem precisão dupla.
