# Comentários

Todos os programadores se esforçam para tornar seu código fácil de entender, mas às vezes uma explicação extra é justificada. Nesses casos, os programadores deixam _comentários_ em seu código-fonte que o compilador ignorará, mas que as pessoas que leem o código-fonte podem achar úteis.

Aqui está um comentário simples:

```rust
// hello, world
```

Em Rust, o estilo idiomático de comentário inicia um comentário com duas barras, e o comentário continua até o final da linha. Para comentários que se estendem além de uma única linha, você precisará incluir `//` em cada linha, assim:

    // Então, estamos fazendo algo complicado aqui, longo o suficiente para que precisemos
    // de várias linhas de comentários para fazê-lo! Ufa! Esperançosamente, este comentário irá
    // explicar o que está acontecendo.

Os comentários também podem ser colocados no final das linhas contendo código:

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let lucky_number = 7; // Estou com sorte hoje
}
```

Mas você os verá com mais frequência usados neste formato, com o comentário em uma linha separada acima do código que está anotando:

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    // Estou com sorte hoje
    let lucky_number = 7;
}
```

Rust também tem outro tipo de comentário, comentários de documentação, que discutiremos em "Publicando um Crate no Crates.io".
