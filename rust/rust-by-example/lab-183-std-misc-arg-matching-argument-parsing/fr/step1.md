# Analyse d'arguments

La correspondance peut être utilisée pour analyser des arguments simples :

```rust
use std::env;

fn increase(number: i32) {
    println!("{}", number + 1);
}

fn decrease(number: i32) {
    println!("{}", number - 1);
}

fn help() {
    println!("usage:
match_args <string>
    Vérifie si la chaîne donnée est la réponse.
match_args {{increase|decrease}} <integer>
    Augmente ou diminue l'entier donné de 1.");
}

fn main() {
    let args: Vec<String> = env::args().collect();

    match args.len() {
        // aucun argument passé
        1 => {
            println!("My name is'match_args'. Try passing some arguments!");
        },
        // un argument passé
        2 => {
            match args[1].parse() {
                Ok(42) => println!("This is the answer!"),
                _ => println!("This is not the answer."),
            }
        },
        // une commande et un argument passé
        3 => {
            let cmd = &args[1];
            let num = &args[2];
            // analyse le nombre
            let number: i32 = match num.parse() {
                Ok(n) => {
                    n
                },
                Err(_) => {
                    eprintln!("error: second argument not an integer");
                    help();
                    return;
                },
            };
            // analyse la commande
            match &cmd[..] {
                "increase" => increase(number),
                "decrease" => decrease(number),
                _ => {
                    eprintln!("error: invalid command");
                    help();
                },
            }
        },
        // tous les autres cas
        _ => {
            // affiche un message d'aide
            help();
        }
    }
}
```

```shell
$./match_args Rust
This is not the answer.
$./match_args 42
This is the answer!
$./match_args do something
error: second argument not an integer
usage:
match_args <string>
    Vérifie si la chaîne donnée est la réponse.
match_args {increase|decrease} <integer>
    Augmente ou diminue l'entier donné de 1.
$./match_args do 42
error: invalid command
usage:
match_args <string>
    Vérifie si la chaîne donnée est la réponse.
match_args {increase|decrease} <integer>
    Augmente ou diminue l'entier donné de 1.
$./match_args increase 42
43
```
