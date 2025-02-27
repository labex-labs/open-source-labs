# Definiendo un tipo de error

A veces, simplifica el código enmascarar todos los diferentes errores con un solo tipo de error. Lo demostraremos con un error personalizado.

Rust nos permite definir nuestros propios tipos de error. En general, un "buen" tipo de error:

- Representa diferentes errores con el mismo tipo
- Muestra mensajes de error agradables al usuario
- Es fácil de comparar con otros tipos
  - Bueno: `Err(EmptyVec)`
  - Malo: `Err("Please use a vector with at least one element".to_owned())`
- Puede contener información sobre el error
  - Bueno: `Err(BadChar(c, position))`
  - Malo: `Err("+ cannot be used here".to_owned())`
- Se combina bien con otros errores

```rust
use std::fmt;

type Result<T> = std::result::Result<T, DoubleError>;

// Definimos nuestros tipos de error. Estos pueden ser personalizados para nuestros casos de manejo de errores.
// Ahora podremos escribir nuestros propios errores, delegar en una implementación de error subyacente
// o hacer algo intermedio.
#[derive(Debug, Clone)]
struct DoubleError;

// La generación de un error es completamente separada de cómo se muestra.
// No es necesario preocuparse por enredar la lógica compleja con el estilo de visualización.
//
// Nota que no almacenamos ninguna información adicional sobre los errores. Esto significa que no podemos
// indicar qué cadena falló al analizar sin modificar nuestros tipos para transportar esa información.
impl fmt::Display for DoubleError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "invalid first item to double")
    }
}

fn double_first(vec: Vec<&str>) -> Result<i32> {
    vec.first()
        // Cambiamos el error al nuestro nuevo tipo.
     .ok_or(DoubleError)
     .and_then(|s| {
            s.parse::<i32>()
                // Actualizamos también al nuevo tipo de error aquí.
             .map_err(|_| DoubleError)
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
