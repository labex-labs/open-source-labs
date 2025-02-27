# Repetición

Las macros pueden usar `+` en la lista de argumentos para indicar que un argumento puede repetirse al menos una vez, o `*`, para indicar que el argumento puede repetirse cero o más veces.

En el siguiente ejemplo, rodeando el coincidente con `$(...),+` coincidirá con una o más expresiones, separadas por comas. También observe que el punto y coma es opcional en el último caso.

```rust
// `find_min!` calculará el mínimo de cualquier número de argumentos.
macro_rules! find_min {
    // Caso base:
    ($x:expr) => ($x);
    // `$x` seguido de al menos un `$y,`
    ($x:expr, $($y:expr),+) => (
        // Llame a `find_min!` en la cola `$y`
        std::cmp::min($x, find_min!($($y),+))
    )
}

fn main() {
    println!("{}", find_min!(1));
    println!("{}", find_min!(1 + 2, 2));
    println!("{}", find_min!(5, 2 * 3, 4));
}
```
