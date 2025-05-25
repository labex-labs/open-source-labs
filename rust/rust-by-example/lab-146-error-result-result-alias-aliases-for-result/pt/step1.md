# Aliases (Apelidos) para `Result`

E se quisermos reutilizar um tipo `Result` específico várias vezes? Lembre-se que o Rust nos permite criar aliases (apelidos). Convenientemente, podemos definir um para o `Result` específico em questão.

Em nível de módulo, a criação de aliases pode ser particularmente útil. Erros encontrados em um módulo específico frequentemente têm o mesmo tipo `Err`, então um único alias pode definir sucintamente _todos_ os `Results` associados. Isso é tão útil que a biblioteca `std` até fornece um: `io::Result`!

Aqui está um exemplo rápido para mostrar a sintaxe:

```rust
use std::num::ParseIntError;

// Define um alias genérico para um `Result` com o tipo de erro `ParseIntError`.
type AliasedResult<T> = Result<T, ParseIntError>;

// Use o alias acima para referenciar nosso tipo `Result` específico.
fn multiply(first_number_str: &str, second_number_str: &str) -> AliasedResult<i32> {
    first_number_str.parse::<i32>().and_then(|first_number| {
        second_number_str.parse::<i32>().map(|second_number| first_number * second_number)
    })
}

// Aqui, o alias novamente nos permite economizar algum espaço.
fn print(result: AliasedResult<i32>) {
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
