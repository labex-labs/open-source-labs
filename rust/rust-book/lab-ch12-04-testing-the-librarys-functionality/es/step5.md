# Buscando la consulta en cada línea

A continuación, comprobaremos si la línea actual contiene la cadena de consulta. Afortunadamente, las cadenas tienen un método útil llamado `contains` que lo hace por nosotros. Agregue una llamada al método `contains` en la función `search`, como se muestra en la Lista 12-18. Tenga en cuenta que esto todavía no se compilará.

Nombre del archivo: `src/lib.rs`

```rust
pub fn search<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    for line in contents.lines() {
        if line.contains(query) {
            // hacer algo con line
        }
    }
}
```

Lista 12-18: Agregando funcionalidad para ver si la línea contiene la cadena en `query`

En este momento, estamos construyendo funcionalidad. Para que el código se compile, necesitamos devolver un valor del cuerpo como indicamos que haríamos en la firma de la función.
