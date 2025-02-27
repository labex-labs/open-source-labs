# Comentarios

Todos los programadores tratan de hacer que su código sea fácil de entender, pero a veces es necesario una explicación adicional. En estos casos, los programadores dejan _comentarios_ en su código fuente que el compilador ignorará, pero que las personas que lean el código fuente pueden encontrar útiles.

Aquí hay un comentario simple:

```rust
// hello, world
```

En Rust, el estilo de comentario idiómatizado comienza un comentario con dos barras diagonales, y el comentario continúa hasta el final de la línea. Para comentarios que se extienden más allá de una sola línea, tendrás que incluir `//` en cada línea, como esto:

    // Entonces, estamos haciendo algo complicado aquí, lo suficientemente largo como para que necesitemos
    // múltiples líneas de comentarios para hacerlo. ¡Uy! Espero que este comentario
    // explique lo que está pasando.

Los comentarios también se pueden colocar al final de las líneas que contienen código:

Nombre del archivo: `src/main.rs`

```rust
fn main() {
    let lucky_number = 7; // Estoy sintiéndome afortunado hoy
}
```

Pero más a menudo los verás utilizados en este formato, con el comentario en una línea separada encima del código que está anotando:

Nombre del archivo: `src/main.rs`

```rust
fn main() {
    // Estoy sintiéndome afortunado hoy
    let lucky_number = 7;
}
```

Rust también tiene otro tipo de comentario, los comentarios de documentación, que discutiremos en "Publicando un Caja a Crates.io".
