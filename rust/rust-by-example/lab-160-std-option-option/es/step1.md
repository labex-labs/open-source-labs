# `Option`

A veces es deseable capturar el fracaso de algunas partes de un programa en lugar de llamar a `panic!`; esto se puede lograr utilizando el enum `Option`.

El enum `Option<T>` tiene dos variantes:

- `None`, para indicar el fracaso o la ausencia de valor, y
- `Some(value)`, una struct tupla que envuelve un `value` con tipo `T`.

```rust
// Una división entera que no `panic!`
fn checked_division(dividendo: i32, divisor: i32) -> Option<i32> {
    if divisor == 0 {
        // El fracaso se representa como la variante `None`
        None
    } else {
        // El resultado se envuelve en una variante `Some`
        Some(dividendo / divisor)
    }
}

// Esta función maneja una división que puede no tener éxito
fn try_division(dividendo: i32, divisor: i32) {
    // Los valores de `Option` se pueden hacer match de patrones, al igual que otros enums
    match checked_division(dividendo, divisor) {
        None => println!("{} / {} fracasó!", dividendo, divisor),
        Some(cociente) => {
            println!("{} / {} = {}", dividendo, divisor, cociente)
        },
    }
}

fn main() {
    try_division(4, 2);
    try_division(1, 0);

    // Asignar `None` a una variable necesita ser anotada con tipo
    let none: Option<i32> = None;
    let _equivalente_none = None::<i32>;

    let optional_float = Some(0f32);

    // Desempaquetar una variante `Some` extraerá el valor envuelto.
    println!("{:?} se desempaqueta en {:?}", optional_float, optional_float.unwrap());

    // Desempaquetar una variante `None` hará `panic!`
    println!("{:?} se desempaqueta en {:?}", none, none.unwrap());
}
```
