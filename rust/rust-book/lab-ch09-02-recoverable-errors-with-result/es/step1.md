# Errores recuperables con Result

La mayoría de los errores no son lo suficientemente graves como para que el programa se detenga por completo. A veces, cuando una función falla, es por un motivo que se puede interpretar y responder fácilmente. Por ejemplo, si intentas abrir un archivo y esa operación falla porque el archivo no existe, es posible que desees crear el archivo en lugar de terminar el proceso.

Recuerda de "Manejar el fracaso potencial con Result" que el enum `Result` está definido como tener dos variantes, `Ok` y `Err`, de la siguiente manera:

```rust
enum Result<T, E> {
    Ok(T),
    Err(E),
}
```

Los parámetros de tipo genéricos `T` y `E`: discutiremos los genéricos con más detalle en el Capítulo 10. Lo que debes saber en este momento es que `T` representa el tipo del valor que se devolverá en un caso de éxito dentro de la variante `Ok`, y `E` representa el tipo del error que se devolverá en un caso de fracaso dentro de la variante `Err`. Debido a que `Result` tiene estos parámetros de tipo genéricos, podemos usar el tipo `Result` y las funciones definidas en él en muchas situaciones diferentes donde el valor de éxito y el valor de error que queremos devolver pueden variar.

Llamemos a una función que devuelve un valor `Result` porque la función podría fallar. En la Lista 9-3 intentamos abrir un archivo.

Nombre del archivo: `src/main.rs`

```rust
use std::fs::File;

fn main() {
    let greeting_file_result = File::open("hello.txt");
}
```

Lista 9-3: Abriendo un archivo

El tipo de retorno de `File::open` es un `Result<T, E>`. El parámetro genérico `T` ha sido rellenado por la implementación de `File::open` con el tipo del valor de éxito, `std::fs::File`, que es un manejador de archivo. El tipo de `E` usado en el valor de error es `std::io::Error`. Este tipo de retorno significa que la llamada a `File::open` podría tener éxito y devolver un manejador de archivo que podemos leer o escribir. La llamada a la función también podría fallar: por ejemplo, el archivo podría no existir, o no podríamos tener permiso para acceder al archivo. La función `File::open` necesita tener una manera de decirnos si tuvo éxito o fracasó y, al mismo tiempo, darnos ya sea el manejador de archivo o la información de error. Esta información es exactamente lo que el enum `Result` transmite.

En el caso en el que `File::open` tiene éxito, el valor en la variable `greeting_file_result` será una instancia de `Ok` que contiene un manejador de archivo. En el caso en el que falla, el valor en `greeting_file_result` será una instancia de `Err` que contiene más información sobre el tipo de error que ocurrió.

Necesitamos agregar al código de la Lista 9-3 para tomar diferentes acciones dependiendo del valor que devuelve `File::open`. La Lista 9-4 muestra una manera de manejar el `Result` usando una herramienta básica, la expresión `match` que discutimos en el Capítulo 6.

Nombre del archivo: `src/main.rs`

```rust
use std::fs::File;

fn main() {
    let greeting_file_result = File::open("hello.txt");

    let greeting_file = match greeting_file_result {
        Ok(file) => file,
        Err(error) => {
            panic!("Problem opening the file: {:?}", error);
        }
    };
}
```

Lista 9-4: Usando una expresión `match` para manejar las variantes `Result` que podrían ser devueltas

Tenga en cuenta que, al igual que el enum `Option`, el enum `Result` y sus variantes han sido traídos al ámbito por el preludio, por lo que no necesitamos especificar `Result::` antes de las variantes `Ok` y `Err` en los brazos de la `match`.

Cuando el resultado es `Ok`, este código devolverá el valor interno `file` de la variante `Ok`, y luego asignamos ese valor de manejador de archivo a la variable `greeting_file`. Después de la `match`, podemos usar el manejador de archivo para leer o escribir.

El otro brazo de la `match` maneja el caso en el que obtenemos un valor `Err` de `File::open`. En este ejemplo, hemos elegido llamar a la macro `panic!`. Si no hay un archivo llamado _hello.txt_ en nuestro directorio actual y ejecutamos este código, veremos la siguiente salida de la macro `panic!`:

    thread 'main' panicked at 'Problem opening the file: Os { code:
     2, kind: NotFound, message: "No such file or directory" }',
    src/main.rs:8:23

Como de costumbre, esta salida nos dice exactamente lo que ha salido mal.
