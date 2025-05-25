# Gerando um Número Aleatório

Vamos começar a usar `rand` para gerar um número para adivinhar. O próximo passo é atualizar `src/main.rs`, conforme mostrado na Listagem 2-3.

Nome do arquivo: `src/main.rs`

```rust
use std::io;
1 use rand::Rng;

fn main() {
    println!("Guess the number!");

  2 let secret_number = rand::thread_rng().gen_range(1..=100);

  3 println!("The secret number is: {secret_number}");

    println!("Please input your guess.");

    let mut guess = String::new();

    io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");

    println!("You guessed: {guess}");
}
```

Listagem 2-3: Adicionando código para gerar um número aleatório

Primeiro, adicionamos a linha `use rand::Rng;` \[1]. A trait `Rng` define métodos que os geradores de números aleatórios implementam, e essa trait deve estar no escopo para que possamos usar esses métodos. O Capítulo 10 cobrirá traits em detalhes.

Em seguida, estamos adicionando duas linhas no meio. Na primeira linha \[2], chamamos a função `rand::thread_rng` que nos dá o gerador de números aleatórios específico que vamos usar: um que é local para o thread de execução atual e é semeado pelo sistema operacional. Então, chamamos o método `gen_range` no gerador de números aleatórios. Este método é definido pela trait `Rng` que trouxemos para o escopo com a declaração `use rand::Rng;`. O método `gen_range` recebe uma expressão de intervalo como argumento e gera um número aleatório no intervalo. O tipo de expressão de intervalo que estamos usando aqui assume a forma `start..=end` e é inclusivo nos limites inferior e superior, então precisamos especificar `1..=100` para solicitar um número entre 1 e 100.

> Nota: Você não saberá apenas quais traits usar e quais métodos e funções chamar de um crate, então cada crate tem documentação com instruções para usá-lo. Outra característica interessante do Cargo é que a execução do comando `cargo doc --open` construirá a documentação fornecida por todas as suas dependências localmente e a abrirá em seu navegador. Se você estiver interessado em outras funcionalidades no crate `rand`, por exemplo, execute `cargo doc --open` e clique em `rand` na barra lateral esquerda.

A segunda linha nova \[3] imprime o número secreto. Isso é útil enquanto estamos desenvolvendo o programa para poder testá-lo, mas vamos excluí-lo da versão final. Não é muito um jogo se o programa imprimir a resposta assim que começar!

Tente executar o programa algumas vezes:

```bash
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 2.53s
     Running `target/debug/guessing_game`
Guess the number!
The secret number is: 7
Please input your guess.
4
You guessed: 4

$ cargo run
    Finished dev [unoptimized + debuginfo] target(s) in 0.02s
     Running `target/debug/guessing_game`
Guess the number!
The secret number is: 83
Please input your guess.
5
You guessed: 5
```

Você deve obter números aleatórios diferentes, e todos eles devem ser números entre 1 e 100. Ótimo trabalho!
