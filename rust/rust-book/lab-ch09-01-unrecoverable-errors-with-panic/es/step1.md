# Errores Irrecuperables con panic

A veces, cosas malas suceden en tu código y no hay nada que puedas hacer al respecto. En estos casos, Rust tiene la macro `panic!`. Hay dos maneras de causar un panic en la práctica: realizando una acción que hace que nuestro código se detenga abruptamente (como acceder a un array fuera de los límites) o llamando explícitamente a la macro `panic!`. En ambos casos, causamos un panic en nuestro programa. Por defecto, estos panics imprimirán un mensaje de error, deshacerán el seguimiento de las llamadas a funciones (unwind), limpiarán la pila y detendrán la ejecución. A través de una variable de entorno, también puedes hacer que Rust muestre la pila de llamadas cuando ocurre un panic para facilitar la búsqueda de la fuente del problema.

> **Deshaciendo la pila o abortando en respuesta a un panic**
>
> Por defecto, cuando ocurre un panic, el programa comienza a _deshacerse_ la pila, lo que significa que Rust recorre hacia atrás la pila y limpia los datos de cada función que encuentra. Sin embargo, recorrer hacia atrás y limpiar es un trabajo considerable. Por lo tanto, Rust te permite elegir la alternativa de _abortar_ inmediatamente, lo que finaliza el programa sin limpiar.
>
> En ese caso, la memoria que el programa estaba utilizando tendrá que ser limpiada por el sistema operativo. Si en tu proyecto necesitas hacer que el binario resultante sea lo más pequeño posible, puedes cambiar de deshacer la pila a abortar en caso de panic agregando `panic = 'abort'` a las secciones `[profile]` adecuadas en tu archivo `Cargo.toml`. Por ejemplo, si quieres abortar en caso de panic en modo de lanzamiento, agrega esto:
>
> ```toml
> [profile.release]
> panic = 'abort'
> ```

Intentemos llamar a `panic!` en un programa simple:

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    panic!("crash and burn");
}
```

Cuando ejecutes el programa, verás algo como esto:

    thread 'main' panicked at 'crash and burn', src/main.rs:2:5
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace

La llamada a `panic!` causa el mensaje de error contenido en las últimas dos líneas. La primera línea muestra nuestro mensaje de panic y el lugar en nuestro código fuente donde ocurrió el panic: _src/main.rs:2:5_ indica que es la segunda línea, quinta caracter del archivo `src/main.rs`.

En este caso, la línea indicada es parte de nuestro código, y si vamos a esa línea, vemos la llamada a la macro `panic!`. En otros casos, la llamada a `panic!` podría estar en el código que nuestro código llama, y el nombre de archivo y número de línea reportados por el mensaje de error serán el código de alguien más donde se llama a la macro `panic!`, no la línea de nuestro código que finalmente llevó a la llamada a `panic!`.

Podemos usar la traza de pila de las funciones de las que proviene la llamada a `panic!` para averiguar la parte de nuestro código que está causando el problema. Para entender cómo usar una traza de pila de `panic!`, veamos otro ejemplo y veamos cómo es cuando una llamada a `panic!` proviene de una biblioteca debido a un error en nuestro código en lugar de que provenga directamente de nuestro código llamando a la macro. La Lista 9-1 tiene un código que intenta acceder a un índice en un vector más allá del rango de índices válidos.

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let v = vec![1, 2, 3];

    v[99];
}
```

Lista 9-1: Intentando acceder a un elemento más allá del final de un vector, lo que causará una llamada a `panic!`

Aquí, estamos intentando acceder al centésimo elemento de nuestro vector (que está en el índice 99 porque el índice comienza en cero), pero el vector solo tiene tres elementos. En esta situación, Rust se detendrá abruptamente. Usar `[]` se supone que debe devolver un elemento, pero si pasas un índice no válido, no hay ningún elemento que Rust podría devolver aquí que sea correcto.

En C, intentar leer más allá del final de una estructura de datos es un comportamiento indefinido. Puedes obtener lo que sea que se encuentre en la ubicación de memoria que correspondería a ese elemento en la estructura de datos, aunque la memoria no pertenezca a esa estructura. Esto se llama _lectura excesiva de búfer_ y puede conducir a vulnerabilidades de seguridad si un atacante es capaz de manipular el índice de manera que lea datos que no debería tener acceso y que se almacenan después de la estructura de datos.

Para proteger tu programa de este tipo de vulnerabilidades, si intentas leer un elemento en un índice que no existe, Rust detendrá la ejecución y se negará a continuar. Intentémoslo y veamos:

    thread 'main' panicked at 'index out of bounds: the len is 3 but the index is
    99', src/main.rs:4:5
    note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

Este error apunta a la línea 4 de nuestro `main.rs` donde intentamos acceder al `índice`.

La línea `note:` nos dice que podemos establecer la variable de entorno `RUST_BACKTRACE` para obtener una traza de pila de exactamente lo que sucedió para causar el error. Una _traza de pila_ es una lista de todas las funciones que se han llamado para llegar a este punto. Las trazas de pila en Rust funcionan como en otros lenguajes: la clave para leer la traza de pila es comenzar desde el principio y leer hasta que veas archivos que hayas escrito. Ese es el lugar donde el problema se originó. Las líneas por encima de ese lugar son código que tu código ha llamado; las líneas por debajo son código que llamó a tu código. Estas líneas anteriores y posteriores pueden incluir código de Rust core, código de la biblioteca estándar o cajas que estés usando. Intentemos obtener una traza de pila estableciendo la variable de entorno `RUST_BACKTRACE` en cualquier valor diferente de `0`. La Lista 9-2 muestra una salida similar a la que verás.

```bash
$ RUST_BACKTRACE=1 cargo run
thread 'main' panicked at 'index out of bounds: the len is 3 but the index is
99', src/main.rs:4:5
stack backtrace:
0: rust_begin_unwind
at /rustc/e092d0b6b43f2de967af0887873151bb1c0b18d3/library/std
/src/panicking.rs:584:5
1: core::panicking::panic_fmt
at /rustc/e092d0b6b43f2de967af0887873151bb1c0b18d3/library/core
/src/panicking.rs:142:14
2: core::panicking::panic_bounds_check
at /rustc/e092d0b6b43f2de967af0887873151bb1c0b18d3/library/core
/src/panicking.rs:84:5
3: < usize as core::slice::index::SliceIndex < [T] >> ::index
at /rustc/e092d0b6b43f2de967af0887873151bb1c0b18d3/library/core
/src/slice/index.rs:242:10
4: core::slice::index:: core::ops::index::Index [T] < impl < I > for > ::index
at /rustc/e092d0b6b43f2de967af0887873151bb1c0b18d3/library/core
/src/slice/index.rs:18:9
5: < alloc::vec::Vec < T,A > as core::ops::index::Index < I >> ::index
at /rustc/e092d0b6b43f2de967af0887873151bb1c0b18d3/library/alloc
/src/vec/mod.rs:2591:9
6: panic::main
at./src/main.rs:4:5
7: core::ops::function::FnOnce::call_once
at /rustc/e092d0b6b43f2de967af0887873151bb1c0b18d3/library/core
/src/ops/function.rs:248:5
note: Some details are omitted, run with $(RUST_BACKTRACE=full) for a verbose
backtrace.
```

Lista 9-2: La traza de pila generada por una llamada a `panic!` mostrada cuando se establece la variable de entorno `RUST_BACKTRACE`

¡Esa es una gran cantidad de salida! La salida exacta que ves puede ser diferente dependiendo de tu sistema operativo y versión de Rust. Para obtener trazas de pila con esta información, los símbolos de depuración deben estar habilitados. Los símbolos de depuración se habilitan por defecto cuando se usa `cargo build` o `cargo run` sin la bandera `--release`, como tenemos aquí.

En la salida de la Lista 9-2, la línea 6 de la traza de pila apunta a la línea en nuestro proyecto que está causando el problema: la línea 4 de `src/main.rs`. Si no queremos que nuestro programa se detenga abruptamente, deberíamos comenzar nuestra investigación en la ubicación apuntada por la primera línea que menciona un archivo que hayamos escrito. En la Lista 9-1, donde deliberadamente escribimos código que causaría un panic, la forma de solucionar el panic es no solicitar un elemento más allá del rango de índices del vector. Cuando tu código se detenga abruptamente en el futuro, tendrás que averiguar qué acción está tomando el código con qué valores para causar el panic y qué debería hacer el código en su lugar.

Volveremos a `panic!` y cuándo debemos y no debemos usar `panic!` para manejar condiciones de error en "To panic! or Not to panic!". A continuación, veremos cómo recuperar de un error usando `Result`.
