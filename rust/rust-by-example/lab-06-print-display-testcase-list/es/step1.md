# Caso de prueba: List

Implementar `fmt::Display` para una estructura donde los elementos deben ser manejados secuencialmente es complicado. El problema es que cada `write!` genera un `fmt::Result`. Manejar adecuadamente esto requiere lidiar con _todos_ los resultados. Rust proporciona el operador `?` precisamente para este propósito.

Usar `?` en `write!` se ve así:

```rust
// Intenta `write!` para ver si produce un error. Si produce un error, devuelve
// el error. De lo contrario, continúa.
write!(f, "{}", value)?;
```

Con `?` disponible, implementar `fmt::Display` para un `Vec` es sencillo:

```rust
use std::fmt; // Importa el módulo `fmt`.

// Define una estructura llamada `List` que contiene un `Vec`.
struct List(Vec<i32>);

impl fmt::Display for List {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // Extrae el valor usando indexación de tupla,
        // y crea una referencia a `vec`.
        let vec = &self.0;

        write!(f, "[")?;

        // Itera sobre `v` en `vec` mientras enumera el
        // contador de iteración en `count`.
        for (count, v) in vec.iter().enumerate() {
            // Para cada elemento excepto el primero, agrega una coma.
            // Usa el operador? para devolver en caso de errores.
            if count!= 0 { write!(f, ", ")?; }
            write!(f, "{}", v)?;
        }

        // Cierra el corchete abierto y devuelve un valor fmt::Result.
        write!(f, "]")
    }
}

fn main() {
    let v = List(vec![1, 2, 3]);
    println!("{}", v);
}
```

## Actividad

Intenta cambiar el programa para que también se imprima el índice de cada elemento en el vector. La nueva salida debería verse así:

```rust
[0: 1, 1: 2, 2: 3]
```
