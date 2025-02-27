# alias para `Result`

¿Qué pasa cuando queremos reutilizar un tipo `Result` específico muchas veces? Recuerde que Rust nos permite crear alias. Convenientemente, podemos definir uno para el `Result` específico en cuestión.

A nivel de módulo, crear alias puede ser particularmente útil. Los errores encontrados en un módulo específico a menudo tienen el mismo tipo `Err`, por lo que un solo alias puede definir _todos_ los `Result` asociados de manera concisa. Esto es tan útil que la biblioteca `std` incluso proporciona uno: `io::Result`!

Aquí hay un ejemplo rápido para mostrar la sintaxis:

```rust
use std::num::ParseIntError;

// Defina un alias genérico para un `Result` con el tipo de error `ParseIntError`.
type AliasedResult<T> = Result<T, ParseIntError>;

// Utilice el alias anterior para referirse a nuestro tipo `Result` específico.
fn multiply(first_number_str: &str, second_number_str: &str) -> AliasedResult<i32> {
    first_number_str.parse::<i32>().and_then(|first_number| {
        second_number_str.parse::<i32>().map(|second_number| first_number * second_number)
    })
}

// Aquí, el alias nuevamente nos permite ahorrar algo de espacio.
fn print(result: AliasedResult<i32>) {
    match result {
        Ok(n)  => println!("n es {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    print(multiply("10", "2"));
    print(multiply("t", "2"));
}
```
