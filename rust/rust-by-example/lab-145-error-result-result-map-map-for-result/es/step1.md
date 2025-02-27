# `map` para `Result`

Generar un `panic` en la función `multiply` del ejemplo anterior no es código robusto. En general, queremos devolver el error al llamador para que pueda decidir cómo responder correctamente a los errores.

Primero, necesitamos saber de qué tipo de error estamos hablando. Para determinar el tipo de `Err`, miramos a `parse()`, que está implementado con el trato `FromStr` para `i32`. Como resultado, el tipo de `Err` se especifica como `ParseIntError`.

En el ejemplo siguiente, la declaración `match` directa da lugar a código que es en general más engorroso.

```rust
use std::num::ParseIntError;

// Con el tipo de retorno reescrito, usamos coincidencia de patrones sin `unwrap()`.
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
        Ok(n)  => println!("n es {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    // Esto todavía da una respuesta razonable.
    let twenty = multiply("10", "2");
    print(twenty);

    // Ahora, lo siguiente proporciona un mensaje de error mucho más útil.
    let tt = multiply("t", "2");
    print(tt);
}
```

Afortunadamente, `map`, `and_then` y muchos otros combinadores de `Option` también se implementan para `Result`. `Result` contiene una lista completa.

```rust
use std::num::ParseIntError;

// Al igual que con `Option`, podemos usar combinadores como `map()`.
// Esta función es de otro modo idéntica a la anterior y se lee:
// Multiplica si ambos valores se pueden analizar a partir de str, de lo contrario pasa el error.
fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    first_number_str.parse::<i32>().and_then(|first_number| {
        second_number_str.parse::<i32>().map(|second_number| first_number * second_number)
    })
}

fn print(result: Result<i32, ParseIntError>) {
    match result {
        Ok(n)  => println!("n es {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    // Esto todavía da una respuesta razonable.
    let twenty = multiply("10", "2");
    print(twenty);

    // Ahora, lo siguiente proporciona un mensaje de error mucho más útil.
    let tt = multiply("t", "2");
    print(tt);
}
```
