# Iterando a través de líneas con el método lines

Rust tiene un método útil para manejar la iteración línea por línea de cadenas, convenientemente nombrado `lines`, que funciona como se muestra en la Lista 12-17. Tenga en cuenta que esto aún no se compilará.

Nombre del archivo: `src/lib.rs`

```rust
pub fn search<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    for line in contents.lines() {
        // hacer algo con line
    }
}
```

Lista 12-17: Iterando a través de cada línea en `contents`

El método `lines` devuelve un iterador. Hablaremos de los iteradores en profundidad en el Capítulo 13, pero recuerde que vio esta forma de usar un iterador en la Lista 3-5, donde usamos un bucle `for` con un iterador para ejecutar un código en cada elemento de una colección.
