# Coincidencia con literales

Como viste en el Capítulo 6, puedes coincidir patrones contra literales directamente. El siguiente código da algunos ejemplos:

Nombre de archivo: `src/main.rs`

```rust
let x = 1;

match x {
    1 => println!("uno"),
    2 => println!("dos"),
    3 => println!("tres"),
    _ => println!("cualquier cosa"),
}
```

Este código imprime `uno` porque el valor en `x` es `1`. Esta sintaxis es útil cuando quieres que tu código realice una acción si obtiene un valor concreto particular.
