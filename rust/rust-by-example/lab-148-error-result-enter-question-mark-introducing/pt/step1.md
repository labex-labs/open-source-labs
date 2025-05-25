# Apresentando `?`

Às vezes, queremos apenas a simplicidade de `unwrap` sem a possibilidade de um `panic`. Até agora, `unwrap` nos forçou a aninhar cada vez mais profundamente quando o que realmente queríamos era obter a variável _fora_. Este é exatamente o propósito de `?`.

Ao encontrar um `Err`, existem duas ações válidas a serem tomadas:

1.  `panic!` que já decidimos tentar evitar, se possível
2.  `return` porque um `Err` significa que não pode ser tratado

`?` é _quase_\[\^†] exatamente equivalente a um `unwrap` que `return`a em vez de entrar em `panic` em `Err`s. Vamos ver como podemos simplificar o exemplo anterior que usava combinadores:

```rust
use std::num::ParseIntError;

fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    let first_number = first_number_str.parse::<i32>()?;
    let second_number = second_number_str.parse::<i32>()?;

    Ok(first_number * second_number)
}

fn print(result: Result<i32, ParseIntError>) {
    match result {
        Ok(n)  => println!("n is {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    print(multiply("10", "2"));
    print(multiply("t", "2"));
}
```

## A macro `try!`

Antes de existir `?`, a mesma funcionalidade era alcançada com a macro `try!`. O operador `?` é agora recomendado, mas você ainda pode encontrar `try!` ao olhar para código mais antigo. A mesma função `multiply` do exemplo anterior ficaria assim usando `try!`:

```rust
// To compile and run this example without errors, while using Cargo, change the value
// of the `edition` field, in the `[package]` section of the `Cargo.toml` file, to "2015".

use std::num::ParseIntError;

fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    let first_number = try!(first_number_str.parse::<i32>());
    let second_number = try!(second_number_str.parse::<i32>());

    Ok(first_number * second_number)
}

fn print(result: Result<i32, ParseIntError>) {
    match result {
        Ok(n)  => println!("n is {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    print(multiply("10", "2"));
    print(multiply("t", "2"));
}
```
