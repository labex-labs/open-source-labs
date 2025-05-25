# Acessando Elementos de Array

Um array é um único bloco de memória de um tamanho conhecido e fixo que pode ser alocado na pilha (stack). Você pode acessar elementos de um array usando indexação, assim:

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let a = [1, 2, 3, 4, 5];

    let first = a[0];
    let second = a[1];
}
```

Neste exemplo, a variável chamada `first` receberá o valor `1` porque esse é o valor no índice `[0]` no array. A variável chamada `second` receberá o valor `2` do índice `[1]` no array.
