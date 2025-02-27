# Almacenando el Texto del Contenido de la Publicación

Vimos en la Lista 17-11 que queremos poder llamar a un método llamado `add_text` y pasarle un `&str` que luego se agregue como el contenido de texto de la publicación de blog. Lo implementamos como un método, en lugar de exponer el campo `content` como `pub`, para que más adelante podamos implementar un método que controlará cómo se lee los datos del campo `content`. El método `add_text` es bastante sencillo, así que agreguemos la implementación en la Lista 17-13 al bloque `impl Post`.

Nombre de archivo: `src/lib.rs`

```rust
impl Post {
    --snip--
    pub fn add_text(&mut self, text: &str) {
        self.content.push_str(text);
    }
}
```

Lista 17-13: Implementando el método `add_text` para agregar texto al `content` de una publicación

El método `add_text` toma una referencia mutable a `self` porque estamos cambiando la instancia de `Post` en la que estamos llamando a `add_text`. Luego llamamos a `push_str` en la `String` en `content` y pasamos el argumento `text` para agregarlo al `content` guardado. Este comportamiento no depende del estado en el que se encuentra la publicación, por lo que no es parte del patrón de estado. El método `add_text` no interactúa con el campo `state` en absoluto, pero es parte del comportamiento que queremos admitir.
