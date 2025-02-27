# Leyendo los Valores de los Argumentos

Para permitir que `minigrep` lea los valores de los argumentos de línea de comandos que le pasamos, necesitaremos la función `std::env::args` proporcionada en la biblioteca estándar de Rust. Esta función devuelve un iterador de los argumentos de línea de comandos pasados a `minigrep`. Cubriremos los iteradores en detalle en el Capítulo 13. Por ahora, solo necesitas saber dos detalles sobre los iteradores: los iteradores producen una serie de valores, y podemos llamar al método `collect` en un iterador para convertirlo en una colección, como un vector, que contiene todos los elementos que produce el iterador.

El código de la Lista 12-1 permite que tu programa `minigrep` lea cualquier argumento de línea de comandos pasado a él, y luego recopile los valores en un vector.

Nombre del archivo: `src/main.rs`

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    dbg!(args);
}
```

Lista 12-1: Recopilando los argumentos de línea de comandos en un vector y mostrándolos

Primero traemos el módulo `std::env` al ámbito con una declaración `use` para poder usar su función `args`. Observe que la función `std::env::args` está anidada en dos niveles de módulos. Como discutimos en el Capítulo 7, en casos donde la función deseada está anidada en más de un módulo, hemos elegido traer el módulo padre al ámbito en lugar de la función. Al hacerlo, podemos usar fácilmente otras funciones de `std::env`. También es menos ambiguo que agregar `use std::env::args` y luego llamar a la función solo con `args`, porque `args` podría fácilmente ser confundido con una función que está definida en el módulo actual.

> **La función args y el Unicode no válido**
>
> Tenga en cuenta que `std::env::args` se interrumpirá si algún argumento contiene Unicode no válido. Si su programa necesita aceptar argumentos que contengan Unicode no válido, use `std::env::args_os` en su lugar. Esa función devuelve un iterador que produce valores `OsString` en lugar de valores `String`. Hemos elegido usar `std::env::args` aquí por simplicidad porque los valores `OsString` difieren según la plataforma y son más complejos de trabajar que los valores `String`.

En la primera línea de `main`, llamamos a `env::args`, y inmediatamente usamos `collect` para convertir el iterador en un vector que contiene todos los valores producidos por el iterador. Podemos usar la función `collect` para crear muchos tipos de colecciones, por lo que anotamos explícitamente el tipo de `args` para especificar que queremos un vector de cadenas. Aunque rara vez necesites anotar tipos en Rust, `collect` es una función que a menudo necesitas anotar porque Rust no puede inferir el tipo de colección que quieres.

Finalmente, imprimimos el vector usando la macro de depuración. Intentemos ejecutar el código primero sin argumentos y luego con dos argumentos:

```bash
$ cargo run
--snip--
[src/main.rs:5] args = [
"target/debug/minigrep",
]
$ cargo run -- needle haystack
--snip--
[src/main.rs:5] args = [
"target/debug/minigrep",
"needle",
"haystack",
]
```

Observe que el primer valor en el vector es `"target/debug/minigrep"`, que es el nombre de nuestro binario. Esto coincide con el comportamiento de la lista de argumentos en C, permitiendo que los programas usen el nombre con el que se invocaron en su ejecución. A menudo es conveniente tener acceso al nombre del programa en caso de que desees imprimirlo en mensajes o cambiar el comportamiento del programa según el alias de línea de comandos que se usó para invocar el programa. Pero con fines de este capítulo, lo ignoraremos y guardaremos solo los dos argumentos que necesitamos.
