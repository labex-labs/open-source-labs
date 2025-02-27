# constantes

Rust tiene dos tipos diferentes de constantes que se pueden declarar en cualquier ámbito, incluyendo el global. Ambos requieren una anotación de tipo explícita:

- `const`: Un valor inmutable (el caso común).
- `static`: Una variable posiblemente `mut`able con una duración de `'static`. La duración estática se infiere y no tiene que especificarse. Acceder o modificar una variable estática mutable es `unsafe`.

```rust
// Las variables globales se declaran fuera de todos los demás ámbitos.
static LANGUAGE: &str = "Rust";
const THRESHOLD: i32 = 10;

fn is_big(n: i32) -> bool {
    // Acceder a una constante en alguna función
    n > THRESHOLD
}

fn main() {
    let n = 16;

    // Acceder a una constante en el hilo principal
    println!("This is {}", LANGUAGE);
    println!("The threshold is {}", THRESHOLD);
    println!("{} is {}", n, if is_big(n) { "big" } else { "small" });

    // Error! No se puede modificar una `const`.
    THRESHOLD = 5;
    // FIXME ^ Comenta esta línea
}
```
