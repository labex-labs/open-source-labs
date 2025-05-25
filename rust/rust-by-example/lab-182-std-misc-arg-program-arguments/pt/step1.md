# Argumentos do Programa

## Biblioteca Padrão

Os argumentos da linha de comando podem ser acessados usando `std::env::args`, que retorna um iterador que gera uma `String` para cada argumento:

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    // O primeiro argumento é o caminho usado para chamar o programa.
    println!("Meu caminho é {}.", args[0]);

    // O restante dos argumentos são os parâmetros passados na linha de comando.
    // Chame o programa assim:
    //   $ ./args arg1 arg2
    println!("Recebi {:?} argumentos: {:?}.", args.len() - 1, &args[1..]);
}
```

```shell
$ ./args 1 2 3
Meu caminho é ./args.
Recebi 3 argumentos: ["1", "2", "3"].
```

## Pacotes (Crates)

Alternativamente, existem vários pacotes (crates) que podem fornecer funcionalidades extras ao criar aplicações de linha de comando. O [Livro de Receitas de Rust](https://doc.rust-lang.org/rust-by-example/std/os/args.html) demonstra boas práticas sobre como usar um dos pacotes mais populares para argumentos de linha de comando, `clap`.
