# Retornos tempranos

En el ejemplo anterior, manejamos explícitamente los errores usando combinadores. Otra forma de abordar este análisis de casos es usar una combinación de declaraciones `match` y _retornos tempranos_.

Es decir, podemos simplemente detener la ejecución de la función y devolver el error si ocurre uno. Para algunos, esta forma de código puede ser más fácil de leer y escribir. Considere esta versión del ejemplo anterior, reescrita usando retornos tempranos:

```rust
use std::num::ParseIntError;

fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    let first_number = match first_number_str.parse::<i32>() {
        Ok(first_number)  => first_number,
        Err(e) => return Err(e),
    };

    let second_number = match second_number_str.parse::<i32>() {
        Ok(second_number)  => second_number,
        Err(e) => return Err(e),
    };

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

Hasta este punto, hemos aprendido a manejar explícitamente los errores usando combinadores y retornos tempranos. Si bien generalmente queremos evitar causar un `panic`, manejar explícitamente todos nuestros errores es engorroso.

En la siguiente sección, introduciremos el `?` para los casos en los que simplemente necesitamos `desempaquetar` sin correr el riesgo de causar un `panic`.
