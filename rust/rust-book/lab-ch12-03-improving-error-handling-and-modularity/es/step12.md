# Manejo de Errores Devueltos por run en main

Verificaremos los errores y los manejaremos usando una técnica similar a la que usamos con `Config::build` en la Lista 12-10, pero con una pequeña diferencia:

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    --snip--

    println!("Buscando {}", config.query);
    println!("En el archivo {}", config.file_path);

    if let Err(e) = run(config) {
        println!("Error de la aplicación: {e}");
        process::exit(1);
    }
}
```

Usamos `if let` en lugar de `unwrap_or_else` para verificar si `run` devuelve un valor `Err` y para llamar a `process::exit(1)` si es el caso. La función `run` no devuelve un valor que queramos `desenvolver` de la misma manera que `Config::build` devuelve la instancia de `Config`. Dado que `run` devuelve `()` en el caso de éxito, solo nos importa detectar un error, por lo que no necesitamos `unwrap_or_else` para devolver el valor desenvolverido, que solo sería `()`.

Los cuerpos de las funciones `if let` y `unwrap_or_else` son los mismos en ambos casos: imprimimos el error y salimos.
