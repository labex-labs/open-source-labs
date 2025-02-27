# Presentando `?`

A veces solo queremos la simplicidad de `unwrap` sin la posibilidad de un `panic`. Hasta ahora, `unwrap` nos ha obligado a anidar cada vez más profundamente cuando lo que realmente queríamos era obtener la variable _fuera_. Esto es exactamente el propósito de `?`.

Al encontrar un `Err`, hay dos acciones válidas que se pueden tomar:

1.  `panic!` que ya decidimos tratar de evitar si es posible
2.  `return` porque un `Err` significa que no se puede manejar

`?` es _casi_\[\^†\] exactamente equivalente a un `unwrap` que `return`s en lugar de `panic`ar en `Err`s. Veamos cómo podemos simplificar el ejemplo anterior que usaba combinadores:

```rust
use std::num::ParseIntError;

fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    let first_number = first_number_str.parse::<i32>()?;
    let second_number = second_number_str.parse::<i32>()?;

    Ok(first_number * second_number)
}

fn print(result: Result<i32, ParseIntError>) {
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

## La macro `try!`

Antes de que existiera `?`, la misma funcionalidad se lograba con la macro `try!`. Ahora se recomienda el operador `?`, pero es posible que aún encuentres `try!` al revisar código antiguo. La misma función `multiply` del ejemplo anterior se vería así usando `try!`:

```rust
// Para compilar y ejecutar este ejemplo sin errores, mientras se usa Cargo, cambia el valor
// del campo `edition`, en la sección `[package]` del archivo `Cargo.toml`, a "2015".

use std::num::ParseIntError;

fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    let first_number = try!(first_number_str.parse::<i32>());
    let second_number = try!(second_number_str.parse::<i32>());

    Ok(first_number * second_number)
}

fn print(result: Result<i32, ParseIntError>) {
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
