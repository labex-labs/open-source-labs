# Saliendo después de una suposición correcta

Programemos el juego para que salga cuando el usuario gane, agregando una declaración `break`:

Nombre del archivo: `src/main.rs`

```rust
--snip--

match guess.cmp(&secret_number) {
    Ordering::Less => println!("Demasiado pequeño!"),
    Ordering::Greater => println!("Demasiado grande!"),
    Ordering::Equal => {
        println!("¡Ganaste!");
        break;
    }
}
```

Agregar la línea `break` después de `¡Ganaste!` hace que el programa salga del bucle cuando el usuario adivina correctamente el número secreto. Salir del bucle también significa salir del programa, porque el bucle es la última parte de `main`.
