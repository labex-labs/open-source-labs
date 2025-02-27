# Mutabilidad

Los enlaces de variables son inmutables por defecto, pero esto se puede anular utilizando el modificador `mut`.

```rust
fn main() {
    let _immutable_binding = 1;
    let mut mutable_binding = 1;

    println!("Before mutation: {}", mutable_binding);

    // Ok
    mutable_binding += 1;

    println!("After mutation: {}", mutable_binding);

    // Error! Cannot assign a new value to an immutable variable
    _immutable_binding += 1;
}
```

El compilador lanzará un diagnóstico detallado sobre los errores de mutabilidad.
