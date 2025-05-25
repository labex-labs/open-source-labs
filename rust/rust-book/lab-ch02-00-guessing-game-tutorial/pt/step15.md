# Permitindo Vários Palpites com Loops

A palavra-chave `loop` cria um loop infinito. Adicionaremos um loop para dar aos usuários mais chances de adivinhar o número:

Nome do arquivo: `src/main.rs`

```rust
use std::io;
use rand::Rng;
use std::cmp::Ordering;

fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1..=100);

    println!("The secret number is: {secret_number}");

    loop {
        println!("Please input your guess.");
        let mut guess = String::new();

        io::stdin()
            .read_line(&mut guess)
            .expect("Failed to read line");

        let guess: u32 = guess
            .trim()
            .parse()
            .expect("Please type a number!");

        println!("You guessed: {guess}");

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => println!("You win!"),
        }
    }
}
```

Como você pode ver, movemos tudo, desde o prompt de entrada do palpite em diante, para um loop. Certifique-se de indentar as linhas dentro do loop mais quatro espaços cada e execute o programa novamente. O programa agora pedirá outro palpite para sempre, o que na verdade introduz um novo problema. Não parece que o usuário pode sair!

O usuário sempre pode interromper o programa usando o atalho de teclado Ctrl-C. Mas há outra maneira de escapar desse monstro insaciável, como mencionado na discussão `parse` em "Comparando o Palpite com o Número Secreto": se o usuário inserir uma resposta que não seja um número, o programa travará. Podemos tirar proveito disso para permitir que o usuário saia, como mostrado aqui:

```bash
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 1.50s
     Running `target/debug/guessing_game`
Guess the number!
The secret number is: 59
Please input your guess.
45
You guessed: 45
Too small!
Please input your guess.
60
You guessed: 60
Too big!
Please input your guess.
59
You guessed: 59
You win!
Please input your guess.
quit
thread 'main' panicked at 'Please type a number!: ParseIntError
{ kind: InvalidDigit }', src/main.rs:28:47
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
```

Digitar `quit` encerrará o jogo, mas, como você notará, também fará com que qualquer outra entrada que não seja um número seja encerrada. Isso é subótimo, para dizer o mínimo; queremos que o jogo também pare quando o número correto for adivinhado.
