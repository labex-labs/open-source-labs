# Envolver errores

Una alternativa a empaquetar errores es envolverlos en un tipo de error propio.

```rust
use std::error;
use std::error::Error;
use std::num::ParseIntError;
use std::fmt;

type Result<T> = std::result::Result<T, DoubleError>;

#[derive(Debug)]
enum DoubleError {
    EmptyVec,
    // Dejaremos que la implementación de error de análisis se ocupe de su error.
    // Proporcionar información adicional requiere agregar más datos al tipo.
    Parse(ParseIntError),
}

impl fmt::Display for DoubleError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match *self {
            DoubleError::EmptyVec =>
                write!(f, "por favor, use un vector con al menos un elemento"),
            // El error envuelto contiene información adicional y está disponible
            // a través del método source().
            DoubleError::Parse(..) =>
                write!(f, "la cadena proporcionada no se pudo analizar como int"),
        }
    }
}

impl error::Error for DoubleError {
    fn source(&self) -> Option<&(dyn error::Error + 'static)> {
        match *self {
            DoubleError::EmptyVec => None,
            // La causa es el tipo de error de implementación subyacente. Se convierte implícitamente
            // en el objeto de tramo `&error::Error`. Esto funciona porque el
            // tipo subyacente ya implementa el tramo `Error`.
            DoubleError::Parse(ref e) => Some(e),
        }
    }
}

// Implemente la conversión de `ParseIntError` a `DoubleError`.
// Esto se llamará automáticamente por `?` si se necesita convertir un `ParseIntError`
// en un `DoubleError`.
impl From<ParseIntError> for DoubleError {
    fn from(err: ParseIntError) -> DoubleError {
        DoubleError::Parse(err)
    }
}

fn double_first(vec: Vec<&str>) -> Result<i32> {
    let first = vec.first().ok_or(DoubleError::EmptyVec)?;
    // Aquí usamos implícitamente la implementación de `From` de `ParseIntError` (que
    // definimos anteriormente) para crear un `DoubleError`.
    let parsed = first.parse::<i32>()?;

    Ok(2 * parsed)
}

fn print(result: Result<i32>) {
    match result {
        Ok(n)  => println!("El primer número duplicado es {}", n),
        Err(e) => {
            println!("Error: {}", e);
            if let Some(source) = e.source() {
                println!("  Causado por: {}", source);
            }
        },
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

Esto agrega un poco más de código repetitivo para manejar errores y puede no ser necesario en todas las aplicaciones. Hay algunas bibliotecas que pueden encargarse del código repetitivo por ti.
