# Almacenando las líneas que coinciden

Para terminar esta función, necesitamos una forma de almacenar las líneas que coinciden y que queremos devolver. Para eso, podemos crear un vector mutable antes del bucle `for` y llamar al método `push` para almacenar una `line` en el vector. Después del bucle `for`, devolvemos el vector, como se muestra en la Lista 12-19.

Nombre del archivo: `src/lib.rs`

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

Lista 12-19: Almacenando las líneas que coinciden para poder devolverlas

Ahora, la función `search` debería devolver solo las líneas que contienen `query`, y nuestra prueba debería pasar. Vamos a ejecutar la prueba:

```bash
$ cargo test
--snip--
running 1 test
test tests::one_result... ok

test result: ok. 1 passed
0 failed
0 ignored
0 measured
0
filtered out
finished in 0.00s
```

Nuestra prueba pasó, ¡por lo que sabemos que funciona!

En este punto, podríamos considerar oportunidades para refactorizar la implementación de la función de búsqueda mientras mantenemos las pruebas pasando para mantener la misma funcionalidad. El código en la función de búsqueda no está demasiado mal, pero no aprovecha algunas características útiles de los iteradores. Volveremos a este ejemplo en el Capítulo 13, donde exploraremos en detalle los iteradores y veremos cómo mejorarlo.
