# Empaquetar errores

Una forma de escribir código simple mientras se preservan los errores originales es empaquetarlos con `Box`. La desventaja es que el tipo de error subyacente solo es conocido en tiempo de ejecución y no se determina en tiempo de compilación.

La biblioteca estándar ayuda a empaquetar nuestros errores al hacer que `Box` implemente la conversión de cualquier tipo que implemente el trato `Error` al objeto de trato `Box<Error>`, a través de `From`.

```rust
use std::error;
use std::fmt;

// Cambia el alias a `Box<error::Error>`.
type Result<T> = std::result::Result<T, Box<dyn error::Error>>;

#[derive(Debug, Clone)]
struct EmptyVec;

impl fmt::Display for EmptyVec {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "invalid first item to double")
    }
}

impl error::Error for EmptyVec {}

fn double_first(vec: Vec<&str>) -> Result<i32> {
    vec.first()
     .ok_or_else(|| EmptyVec.into()) // Convierte a Box
     .and_then(|s| {
            s.parse::<i32>()
             .map_err(|e| e.into()) // Convierte a Box
             .map(|i| 2 * i)
        })
}

fn print(result: Result<i32>) {
    match result {
        Ok(n) => println!("The first doubled is {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    let numbers = vec!["42", "93", "18"];
    let empty = vec![];
    let strings = vec!["tofu", "93", "18"];

    print(double_first(numbers));
    print(double_first(empty));
    print(double_first(strings));
}
```
