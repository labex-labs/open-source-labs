# Análise de Argumentos

A correspondência de padrões pode ser usada para analisar argumentos simples:

```rust
use std::env;

fn increase(number: i32) {
    println!("{}", number + 1);
}

fn decrease(number: i32) {
    println!("{}", number - 1);
}

fn help() {
    println!("uso:
match_args <string>
    Verifica se a string fornecida é a resposta.
match_args {{increase|decrease}} <inteiro>
    Aumenta ou diminui o inteiro fornecido em um.");
}

fn main() {
    let args: Vec<String> = env::args().collect();

    match args.len() {
        // nenhum argumento passado
        1 => {
            println!("Meu nome é 'match_args'. Tente passar alguns argumentos!");
        },
        // um argumento passado
        2 => {
            match args[1].parse() {
                Ok(42) => println!("Esta é a resposta!"),
                _ => println!("Esta não é a resposta."),
            }
        },
        // um comando e um argumento passados
        3 => {
            let cmd = &args[1];
            let num = &args[2];
            // analisar o número
            let number: i32 = match num.parse() {
                Ok(n) => {
                    n
                },
                Err(_) => {
                    eprintln!("erro: segundo argumento não é um inteiro");
                    help();
                    return;
                },
            };
            // analisar o comando
            match &cmd[..] {
                "increase" => increase(number),
                "decrease" => decrease(number),
                _ => {
                    eprintln!("erro: comando inválido");
                    help();
                },
            }
        },
        // todos os outros casos
        _ => {
            // mostrar uma mensagem de ajuda
            help();
        }
    }
}
```

```shell
$ ./match_args Rust
Esta não é a resposta.
$ ./match_args 42
Esta é a resposta!
$ ./match_args fazer algo
erro: segundo argumento não é um inteiro
uso:
match_args <string>
    Verifica se a string fornecida é a resposta.
match_args {increase|decrease} <inteiro>
    Aumenta ou diminui o inteiro fornecido em um.
$ ./match_args fazer 42
erro: comando inválido
uso:
match_args <string>
    Verifica se a string fornecida é a resposta.
match_args {increase|decrease} <inteiro>
    Aumenta ou diminui o inteiro fornecido em um.
$ ./match_args increase 42
43
```
