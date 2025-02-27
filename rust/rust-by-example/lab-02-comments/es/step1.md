# Comentarios

Todo programa requiere comentarios, y Rust admite varios tipos diferentes:

- _Comentarios regulares_ que son ignorados por el compilador:
  - `// Comentarios de línea que se extienden hasta el final de la línea.`
  - `/* Comentarios de bloque que se extienden hasta el delimitador de cierre. */`
- _Comentarios de documentación_ que se analizan en documentación de biblioteca en HTML:
  - `/// Genera documentación de biblioteca para el siguiente elemento.`
  - `//! Genera documentación de biblioteca para el elemento que los envuelve.`

```rust
fn main() {
    // Este es un ejemplo de un comentario de línea.
    // Hay dos barras diagonales al principio de la línea.
    // Y nada escrito después de estas no será leído por el compilador.

    // println!("Hello, world!");

    // Ejecútalo. ¿Ves? Ahora intenta eliminar las dos barras diagonales y ejecútalo de nuevo.

    /*
     * Este es otro tipo de comentario, un comentario de bloque. En general,
     * los comentarios de línea son el estilo de comentario recomendado. Pero los comentarios de bloque
     * son extremadamente útiles para deshabilitar temporalmente trozos de código.
     * /* Los comentarios de bloque pueden ser /* anidados, */ */ así que solo se necesitan unos pocos
     * pulsaciones de teclado para comentar todo el código de esta función main().
     * /*/*/* Prueba hacerlo tú mismo! */*/*/
     */

    /*
    Nota: La columna anterior de `*` era solo para estilo. No es realmente necesaria.
    */

    // Puedes manipular expresiones más fácilmente con comentarios de bloque
    // que con comentarios de línea. Intenta eliminar los delimitadores de comentario
    // para cambiar el resultado:
    let x = 5 + /* 90 + */ 5;
    println!("¿Es `x` 10 o 100? x = {}", x);
}
```
