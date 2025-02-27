# Conversiones a y desde cadenas

## Conversión a String

Convertir cualquier tipo a un `String` es tan sencillo como implementar el trato \[`ToString`\] para el tipo. En lugar de hacerlo directamente, deberías implementar el trato `fmt::Display` que automáticamente proporciona \[`ToString`\] y también permite imprimir el tipo como se discutió en la sección sobre `print!`.

```rust
use std::fmt;

struct Circle {
    radius: i32
}

impl fmt::Display for Circle {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "Circle of radius {}", self.radius)
    }
}

fn main() {
    let circle = Circle { radius: 6 };
    println!("{}", circle.to_string());
}
```

## Análisis de una cadena

Uno de los tipos más comunes es convertir una cadena en un número. La forma idiómatica de hacer esto es usar la función \[`parse`\] y ya sea hacer que se infiera el tipo o especificar el tipo a analizar usando la sintaxis 'turbofish'. Ambas alternativas se muestran en el siguiente ejemplo.

Esto convertirá la cadena al tipo especificado siempre y cuando el trato \[`FromStr`\] esté implementado para ese tipo. Esto está implementado para numerosos tipos dentro de la biblioteca estándar. Para obtener esta funcionalidad en un tipo definido por el usuario simplemente implementa el trato \[`FromStr`\] para ese tipo.

```rust
fn main() {
    let parsed: i32 = "5".parse().unwrap();
    let turbo_parsed = "10".parse::<i32>().unwrap();

    let sum = parsed + turbo_parsed;
    println!("Sum: {:?}", sum);
}
```
