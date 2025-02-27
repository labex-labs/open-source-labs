# Atajos para panic en caso de error: unwrap y expect

Usar `match` funciona bastante bien, pero puede ser un poco verboso y no siempre comunica bien la intención. El tipo `Result<T, E>` tiene muchos métodos auxiliares definidos en él para realizar varias tareas más específicas. El método `unwrap` es un método atajo implementado de la misma manera que la expresión `match` que escribimos en la Lista 9-4. Si el valor de `Result` es la variante `Ok`, `unwrap` devolverá el valor dentro de `Ok`. Si el `Result` es la variante `Err`, `unwrap` llamará a la macro `panic!` por nosotros. Aquí hay un ejemplo de `unwrap` en acción:

Nombre del archivo: `src/main.rs`

```rust
use std::fs::File;

fn main() {
    let greeting_file = File::open("hello.txt").unwrap();
}
```

Si ejecutamos este código sin un archivo _hello.txt_, veremos un mensaje de error de la llamada a `panic!` que hace el método `unwrap`:

    thread 'main' panicked at 'called `Result::unwrap()` on an `Err` value: Os {
    code: 2, kind: NotFound, message: "No such file or directory" }',
    src/main.rs:4:49

Del mismo modo, el método `expect` nos permite también elegir el mensaje de error de `panic!`. Usar `expect` en lugar de `unwrap` y proporcionar buenos mensajes de error puede transmitir tu intención y facilitar la búsqueda de la fuente de un `panic`. La sintaxis de `expect` es la siguiente:

Nombre del archivo: `src/main.rs`

```rust
use std::fs::File;

fn main() {
    let greeting_file = File::open("hello.txt")
     .expect("hello.txt should be included in this project");
}
```

Usamos `expect` de la misma manera que `unwrap`: para devolver el manejador de archivo o llamar a la macro `panic!`. El mensaje de error usado por `expect` en su llamada a `panic!` será el parámetro que le pasamos a `expect`, en lugar del mensaje predeterminado de `panic!` que usa `unwrap`. Aquí es como se ve:

    thread 'main' panicked at 'hello.txt should be included in this project: Os {
    code: 2, kind: NotFound, message: "No such file or directory" }',
    src/main.rs:5:10

En código de calidad de producción, la mayoría de los rustaceos eligen `expect` en lugar de `unwrap` y dan más contexto sobre por qué se espera que la operación siempre tenga éxito. De esa manera, si tus suposiciones alguna vez resultan ser erróneas, tienes más información para usar en la depuración.
