# `map` para `Result`

Entrar em pânico no exemplo anterior de `multiply` não resulta em um código robusto. Geralmente, queremos retornar o erro ao chamador para que ele possa decidir qual é a maneira correta de responder aos erros.

Primeiro, precisamos saber com que tipo de erro estamos lidando. Para determinar o tipo `Err`, olhamos para `parse()`, que é implementado com a trait `FromStr` para `i32`. Como resultado, o tipo `Err` é especificado como `ParseIntError`.

No exemplo abaixo, a instrução `match` direta leva a um código que é, no geral, mais complicado.

```rust
use std::num::ParseIntError;

// Com o tipo de retorno reescrito, usamos correspondência de padrão sem `unwrap()`.
fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    match first_number_str.parse::<i32>() {
        Ok(first_number)  => {
            match second_number_str.parse::<i32>() {
                Ok(second_number)  => {
                    Ok(first_number * second_number)
                },
                Err(e) => Err(e),
            }
        },
        Err(e) => Err(e),
    }
}

fn print(result: Result<i32, ParseIntError>) {
    match result {
        Ok(n)  => println!("n is {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    // This still presents a reasonable answer.
    let twenty = multiply("10", "2");
    print(twenty);

    // The following now provides a much more helpful error message.
    let tt = multiply("t", "2");
    print(tt);
}
```

Felizmente, `map`, `and_then` e muitos outros combinadores de `Option` também são implementados para `Result`. `Result` contém uma lista completa.

```rust
use std::num::ParseIntError;

// Assim como com `Option`, podemos usar combinadores como `map()`.
// Esta função é idêntica à anterior e lê:
// Multiplica se ambos os valores podem ser analisados a partir de str, caso contrário, passa o erro.
fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    first_number_str.parse::<i32>().and_then(|first_number| {
        second_number_str.parse::<i32>().map(|second_number| first_number * second_number)
    })
}

fn print(result: Result<i32, ParseIntError>) {
    match result {
        Ok(n)  => println!("n is {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    // This still presents a reasonable answer.
    let twenty = multiply("10", "2");
    print(twenty);

    // The following now provides a much more helpful error message.
    let tt = multiply("t", "2");
    print(tt);
}
```
