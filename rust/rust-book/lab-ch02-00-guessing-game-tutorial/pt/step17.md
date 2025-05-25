# Lidando com Entrada Inválida

Para refinar ainda mais o comportamento do jogo, em vez de travar o programa quando o usuário insere algo que não é um número, vamos fazer com que o jogo ignore a entrada que não é um número para que o usuário possa continuar adivinhando. Podemos fazer isso alterando a linha onde `guess` é convertido de uma `String` para um `u32`, conforme mostrado na Listagem 2-5.

Nome do arquivo: `src/main.rs`

```rust
--snip--

io::stdin()
    .read_line(&mut guess)
    .expect("Failed to read line");

let guess: u32 = match guess.trim().parse() {
    Ok(num) => num,
    Err(_) => continue,
};

println!("You guessed: {guess}");

--snip--
```

Listagem 2-5: Ignorando um palpite que não é um número e pedindo outro palpite em vez de travar o programa

Mudamos de uma chamada `expect` para uma expressão `match` para passar de travar em um erro para lidar com o erro. Lembre-se que `parse` retorna um tipo `Result` e `Result` é um enum que tem as variantes `Ok` e `Err`. Estamos usando uma expressão `match` aqui, como fizemos com o resultado `Ordering` do método `cmp`.

Se `parse` conseguir transformar a string em um número, ele retornará um valor `Ok` que contém o número resultante. Esse valor `Ok` corresponderá ao padrão do primeiro braço, e a expressão `match` apenas retornará o valor `num` que `parse` produziu e colocou dentro do valor `Ok`. Esse número acabará exatamente onde queremos, na nova variável `guess` que estamos criando.

Se `parse` _não_ conseguir transformar a string em um número, ele retornará um valor `Err` que contém mais informações sobre o erro. O valor `Err` não corresponde ao padrão `Ok(num)` no primeiro braço `match`, mas corresponde ao padrão `Err(_)` no segundo braço. O sublinhado, `_`, é um valor catchall; neste exemplo, estamos dizendo que queremos corresponder a todos os valores `Err`, não importa quais informações eles tenham dentro deles. Portanto, o programa executará o código do segundo braço, `continue`, que diz ao programa para ir para a próxima iteração do `loop` e pedir outro palpite. Então, efetivamente, o programa ignora todos os erros que `parse` pode encontrar!

Agora, tudo no programa deve funcionar como esperado. Vamos tentar:

```bash
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 4.45s
     Running `target/debug/guessing_game`
Guess the number!
The secret number is: 61
Please input your guess.
10
You guessed: 10
Too small!
Please input your guess.
99
You guessed: 99
Too big!
Please input your guess.
foo
Please input your guess.
61
You guessed: 61
You win!
```

Incrível! Com um pequeno ajuste final, terminaremos o jogo de adivinhação. Lembre-se que o programa ainda está imprimindo o número secreto. Isso funcionou bem para testes, mas estraga o jogo. Vamos deletar o `println!` que mostra o número secreto. A Listagem 2-6 mostra o código final.

Nome do arquivo: `src/main.rs`

```rust
use rand::Rng;
use std::cmp::Ordering;
use std::io;

fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1..=100);

    loop {
        println!("Please input your guess.");

        let mut guess = String::new();

        io::stdin()
            .read_line(&mut guess)
            .expect("Failed to read line");

        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        println!("You guessed: {guess}");

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => {
                println!("You win!");
                break;
            }
        }
    }
}
```

Listagem 2-6: Código completo do jogo de adivinhação

Neste ponto, você construiu com sucesso o jogo de adivinhação. Parabéns!
