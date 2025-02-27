# Análisis de argumentos

La coincidencia se puede utilizar para analizar argumentos simples:

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
    Comprueba si la cadena dada es la respuesta.
match_args {{increase|decrease}} <integer>
    Incrementa o decrementa el entero dado en uno.");
}

fn main() {
    let args: Vec<String> = env::args().collect();

    match args.len() {
        // no se pasaron argumentos
        1 => {
            println!("Mi nombre es'match_args'. Intenta pasar algunos argumentos!");
        },
        // se pasó un solo argumento
        2 => {
            match args[1].parse() {
                Ok(42) => println!("This is the answer!"),
                _ => println!("This is not the answer."),
            }
        },
        // se pasó un comando y un argumento
        3 => {
            let cmd = &args[1];
            let num = &args[2];
            // analiza el número
            let number: i32 = match num.parse() {
                Ok(n) => {
                    n
                },
                Err(_) => {
                    eprintln!("error: segundo argumento no es un entero");
                    help();
                    return;
                },
            };
            // analiza el comando
            match &cmd[..] {
                "increase" => increase(number),
                "decrease" => decrease(number),
                _ => {
                    eprintln!("error: comando no válido");
                    help();
                },
            }
        },
        // todos los demás casos
        _ => {
            // muestra un mensaje de ayuda
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
error: segundo argumento no es un entero
uso:
match_args <string>
    Comprueba si la cadena dada es la respuesta.
match_args {increase|decrease} <integer>
    Incrementa o decrementa el entero dado en uno.
$./match_args do 42
error: comando no válido
uso:
match_args <string>
    Comprueba si la cadena dada es la respuesta.
match_args {increase|decrease} <integer>
    Incrementa o decrementa el entero dado en uno.
$./match_args increase 42
43
```
