# Otros usos de `?`

Tenga en cuenta que en el ejemplo anterior, nuestra reacción inmediata a llamar a `parse` es `map` el error de un error de biblioteca en un error empaquetado:

```rust
.and_then(|s| s.parse::<i32>())
 .map_err(|e| e.into())
```

Dado que esta es una operación simple y común, sería conveniente si se pudiera omitir. Lamentablemente, debido a que `and_then` no es lo suficientemente flexible, no se puede. Sin embargo, en su lugar podemos utilizar `?`.

Antes, se explicó que `?` era equivalente a `unwrap` o `return Err(err)`. Esto es solo en gran parte cierto. En realidad significa `unwrap` o `return Err(From::from(err))`. Dado que `From::from` es una utilidad de conversión entre diferentes tipos, esto significa que si utiliza `?` donde el error es convertible en el tipo de retorno, se convertirá automáticamente.

Aquí, reescribimos el ejemplo anterior utilizando `?`. Como resultado, el `map_err` desaparecerá cuando se implemente `From::from` para nuestro tipo de error:

```rust
use std::error;
use std::fmt;

// Cambie el alias a `Box<dyn error::Error>`.
type Result<T> = std::result::Result<T, Box<dyn error::Error>>;

#[derive(Debug)]
struct EmptyVec;

impl fmt::Display for EmptyVec {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "invalid first item to double")
    }
}

impl error::Error for EmptyVec {}

// La misma estructura que antes, pero en lugar de encadenar todos los `Result`
// y `Option` juntos, utilizamos `?` para obtener el valor interno inmediatamente.
fn double_first(vec: Vec<&str>) -> Result<i32> {
    let first = vec.first().ok_or(EmptyVec)?;
    let parsed = first.parse::<i32>()?;
    Ok(2 * parsed)
}

fn print(result: Result<i32>) {
    match result {
        Ok(n)  => println!("The first doubled is {}", n),
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

En realidad, esto es bastante limpio ahora. En comparación con el `panic` original, es muy similar a reemplazar las llamadas a `unwrap` con `?`, excepto que los tipos de retorno son `Result`. Como resultado, deben ser desestructurados en el nivel superior.
