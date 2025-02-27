# Asegurándose de que el Contenido de una Publicación en Borrador Sea Vacio

Incluso después de haber llamado a `add_text` y agregado algún contenido a nuestra publicación, todavía queremos que el método `content` devuelva una porción de cadena vacía porque la publicación todavía está en el estado de borrador, como se muestra en \[3\] de la Lista 17-11. Por ahora, implementemos el método `content` con lo más simple que cumpla con este requisito: siempre devolver una porción de cadena vacía. Lo cambiaremos más adelante una vez que implementemos la capacidad de cambiar el estado de una publicación para que pueda publicarse. Hasta ahora, las publicaciones solo pueden estar en el estado de borrador, por lo que el contenido de la publicación siempre debe estar vacío. La Lista 17-14 muestra esta implementación temporal.

Nombre de archivo: `src/lib.rs`

```rust
impl Post {
    --snip--
    pub fn content(&self) -> &str {
        ""
    }
}
```

Lista 17-14: Agregando una implementación temporal para el método `content` en `Post` que siempre devuelve una porción de cadena vacía

Con este método `content` agregado, todo en la Lista 17-11 hasta la línea en \[3\] funciona como se esperaba.
