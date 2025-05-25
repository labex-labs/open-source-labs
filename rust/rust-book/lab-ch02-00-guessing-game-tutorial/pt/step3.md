# Processando um Palpite

A primeira parte do programa do jogo de adivinhação solicitará a entrada do usuário, processará essa entrada e verificará se ela está na forma esperada. Para começar, permitiremos que o jogador insira um palpite. Insira o código da Listagem 2-1 em `src/main.rs`.

Nome do arquivo: `src/main.rs`

```rust
use std::io;

fn main() {
    println!("Guess the number!");

    println!("Please input your guess.");

    let mut guess = String::new();

    io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");

    println!("You guessed: {guess}");
}
```

Listagem 2-1: Código que obtém um palpite do usuário e o imprime

Este código contém muitas informações, então vamos analisá-lo linha por linha. Para obter a entrada do usuário e, em seguida, imprimir o resultado como saída, precisamos trazer a biblioteca `io` de entrada/saída para o escopo. A biblioteca `io` vem da biblioteca padrão, conhecida como `std`:

```rust
use std::io;
```

Por padrão, o Rust tem um conjunto de itens definidos na biblioteca padrão que ele traz para o escopo de cada programa. Este conjunto é chamado de _prelude_ (preâmbulo), e você pode ver tudo nele em *https://doc.rust-lang.org/std/prelude/index.html*.

Se um tipo que você deseja usar não estiver no preâmbulo, você deve trazer esse tipo para o escopo explicitamente com uma declaração `use`. Usar a biblioteca `std::io` fornece uma série de recursos úteis, incluindo a capacidade de aceitar a entrada do usuário.

Como você viu no Capítulo 1, a função `main` é o ponto de entrada no programa:

```rust
fn main() {
```

A sintaxe `fn` declara uma nova função; os parênteses, `()`, indicam que não há parâmetros; e a chave, `{`, inicia o corpo da função.

Como você também aprendeu no Capítulo 1, `println!` é uma macro que imprime uma string na tela:

```rust
println!("Guess the number!");

println!("Please input your guess.");
```

Este código está imprimindo um prompt que informa qual é o jogo e solicitando a entrada do usuário.
