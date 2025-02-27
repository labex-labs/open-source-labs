# while let

Similar a `if let`, `while let` puede hacer que las secuencias `match` incómodas sean más tolerables. Considere la siguiente secuencia que incrementa `i`:

```rust
// Hacer `optional` del tipo `Option<i32>`
let mut optional = Some(0);

// Intentar repetidamente esta prueba.
loop {
    match optional {
        // Si `optional` se desestructura, evaluar el bloque.
        Some(i) => {
            if i > 9 {
                println!("Mayor que 9, salir!");
                optional = None;
            } else {
                println!("`i` es `{:?}`. Intentar de nuevo.", i);
                optional = Some(i + 1);
            }
            // ^ Requiere 3 sangrías!
        },
        // Salir del bucle cuando la desestructuración falla:
        _ => { break; }
        // ^ ¿Por qué debería ser necesario esto? Debe haber una mejor manera!
    }
}
```

Usar `while let` hace que esta secuencia sea mucho mejor:

```rust
fn main() {
    // Hacer `optional` del tipo `Option<i32>`
    let mut optional = Some(0);

    // Esto se lee: "mientras `let` desestructura `optional` en
    // `Some(i)`, evaluar el bloque (`{}`). En caso contrario `break`.
    while let Some(i) = optional {
        if i > 9 {
            println!("Mayor que 9, salir!");
            optional = None;
        } else {
            println!("`i` es `{:?}`. Intentar de nuevo.", i);
            optional = Some(i + 1);
        }
        // ^ Menos desplazamiento hacia la derecha y no requiere
        // manejar explícitamente el caso de falla.
    }
    // ^ `if let` tenía cláusulas `else`/`else if` adicionales opcionales. `while let` no tiene estas.
}
```
