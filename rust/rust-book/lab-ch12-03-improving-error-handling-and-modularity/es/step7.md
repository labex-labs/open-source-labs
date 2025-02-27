# Mejora del Mensaje de Error

En la Lista 12-8, agregamos una comprobación en la función `new` que verificará que la rebanada sea lo suficientemente larga antes de acceder a los índices 1 e índice 2. Si la rebanada no es lo suficientemente larga, el programa se detiene con un error y muestra un mensaje de error mejor.

Nombre de archivo: `src/main.rs`

```rust
--snip--
fn new(args: &[String]) -> Config {
    if args.len() < 3 {
        panic!("no hay suficientes argumentos");
    }
    --snip--
```

Lista 12-8: Adición de una comprobación para el número de argumentos

Este código es similar a la función `Guess::new` que escribimos en la Lista 9-13, donde llamamos a `panic!` cuando el argumento `value` estaba fuera del rango de valores válidos. En lugar de comprobar un rango de valores aquí, estamos comprobando que la longitud de `args` sea al menos `3` y el resto de la función puede operar bajo la suposición de que esta condición se ha cumplido. Si `args` tiene menos de tres elementos, esta condición será `true`, y llamamos a la macro `panic!` para terminar el programa inmediatamente.

Con estas pocas líneas adicionales de código en `new`, ejecutemos el programa sin ningún argumento nuevamente para ver cómo se ve el error ahora:

```bash
$ cargo run
   Compilando minigrep v0.1.0 (file:///projects/minigrep)
    Terminada la compilación en modo desarrollo [no optimizada + información de depuración] en 0.0s
     Ejecutando `target/debug/minigrep`
hilo'main' se detuvo con un error en 'no hay suficientes argumentos',
src/main.rs:26:13
nota: ejecuta con la variable de entorno `RUST_BACKTRACE=1` para mostrar una traza de pila
```

Esta salida es mejor: ahora tenemos un mensaje de error razonable. Sin embargo, también tenemos información extraña que no queremos dar a nuestros usuarios. Quizás la técnica que usamos en la Lista 9-13 no es la mejor para usar aquí: una llamada a `panic!` es más adecuada para un problema de programación que para un problema de uso, como se discutió en el Capítulo 9. En lugar de eso, usaremos la otra técnica que aprendiste en el Capítulo 9: devolver un `Result` que indique éxito o un error.
