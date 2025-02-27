# Haciendo el código más claro con adaptadores de iterador

También podemos aprovechar los iteradores en la función `search` de nuestro proyecto de E/S, que se reproduce aquí en la Lista 13-21 tal como estaba en la Lista 12-19.

Nombre de archivo: `src/lib.rs`

```rust
pub fn search<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    let mut results = Vec::new();

    for line in contents.lines() {
        if line.contains(query) {
            results.push(line);
        }
    }

    results
}
```

Lista 13-21: La implementación de la función `search` de la Lista 12-19

Podemos escribir este código de manera más concisa utilizando métodos de adaptadores de iterador. Hacer esto también nos permite evitar tener un vector intermedio mutable `results`. El estilo de programación funcional prefiere minimizar la cantidad de estado mutable para hacer el código más claro. Eliminar el estado mutable podría permitir una mejora futura para que la búsqueda se realice en paralelo porque no tendríamos que manejar el acceso concurrente al vector `results`. La Lista 13-22 muestra este cambio.

Nombre de archivo: `src/lib.rs`

```rust
pub fn search<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    contents
     .lines()
     .filter(|line| line.contains(query))
     .collect()
}
```

Lista 13-22: Usando métodos de adaptadores de iterador en la implementación de la función `search`

Recuerde que el propósito de la función `search` es devolver todas las líneas en `contents` que contienen la `query`. Similar al ejemplo de `filter` en la Lista 13-16, este código utiliza el adaptador `filter` para conservar solo las líneas para las cuales `line.contains(query)` devuelve `true`. Luego recolectamos las líneas coincidentes en otro vector con `collect`. ¡Mucho más simple! Siéntase libre de hacer el mismo cambio para usar métodos de iterador en la función `search_case_insensitive` también.
