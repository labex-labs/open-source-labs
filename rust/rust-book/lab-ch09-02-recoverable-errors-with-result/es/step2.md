# Coincidir con diferentes errores

El código de la Lista 9-4 hará `panic!` sin importar por qué falló `File::open`. Sin embargo, queremos tomar diferentes acciones para diferentes razones de falla. Si `File::open` falla porque el archivo no existe, queremos crear el archivo y devolver el manejador al nuevo archivo. Si `File::open` falla por cualquier otra razón, por ejemplo, porque no tenemos permiso para abrir el archivo, todavía queremos que el código haga `panic!` de la misma manera que lo hizo en la Lista 9-4. Para esto, agregamos una expresión `match` interna, como se muestra en la Lista 9-5.

Nombre del archivo: `src/main.rs`

```rust
use std::fs::File;
use std::io::ErrorKind;

fn main() {
    let greeting_file_result = File::open("hello.txt");

    let greeting_file = match greeting_file_result {
        Ok(file) => file,
        Err(error) => match error.kind() {
            ErrorKind::NotFound => {
                match File::create("hello.txt") {
                    Ok(fc) => fc,
                    Err(e) => panic!(
                        "Problem creating the file: {:?}",
                        e
                    ),
                }
            }
            other_error => {
                panic!(
                    "Problem opening the file: {:?}",
                    other_error
                );
            }
        },
    };
}
```

Lista 9-5: Manejar diferentes tipos de errores de diferentes maneras

El tipo del valor que devuelve `File::open` dentro de la variante `Err` es `io::Error`, que es un struct proporcionado por la biblioteca estándar. Este struct tiene un método `kind` que podemos llamar para obtener un valor `io::ErrorKind`. El enum `io::ErrorKind` es proporcionado por la biblioteca estándar y tiene variantes que representan los diferentes tipos de errores que pueden resultar de una operación `io`. La variante que queremos usar es `ErrorKind::NotFound`, que indica que el archivo que estamos intentando abrir todavía no existe. Entonces coincidimos en `greeting_file_result`, pero también tenemos una coincidencia interna en `error.kind()`.

La condición que queremos comprobar en la coincidencia interna es si el valor devuelto por `error.kind()` es la variante `NotFound` del enum `ErrorKind`. Si es así, intentamos crear el archivo con `File::create`. Sin embargo, debido a que `File::create` también podría fallar, necesitamos un segundo brazo en la expresión `match` interna. Cuando el archivo no se puede crear, se imprime un mensaje de error diferente. El segundo brazo de la `match` externa permanece igual, por lo que el programa se detiene en cualquier error aparte del error de archivo faltante.
