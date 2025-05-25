# Inferência

O motor de inferência de tipos é bastante inteligente. Ele faz mais do que apenas verificar o tipo da expressão de valor durante a inicialização. Ele também analisa como a variável é usada posteriormente para inferir seu tipo. Aqui está um exemplo avançado de inferência de tipos:

```rust
fn main() {
    // Devido à anotação, o compilador sabe que `elem` tem o tipo u8.
    let elem = 5u8;

    // Cria um vetor vazio (uma matriz expansível).
    let mut vec = Vec::new();
    // Neste ponto, o compilador não conhece o tipo exato de `vec`, apenas sabe que é um vetor de algo (`Vec<_>`).

    // Insere `elem` no vetor.
    vec.push(elem);
    // Aha! Agora o compilador sabe que `vec` é um vetor de `u8`s (`Vec<u8>`)
    // TODO ^ Tente comentar a linha `vec.push(elem)`

    println!("{:?}", vec);
}
```

Nenhuma anotação de tipo de variáveis foi necessária, o compilador está feliz e o programador também!
