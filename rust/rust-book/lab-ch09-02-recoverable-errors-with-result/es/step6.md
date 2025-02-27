# Un atajo para la propagación de errores: el operador?

La Lista 9-7 muestra una implementación de `read_username_from_file` que tiene la misma funcionalidad que la de la Lista 9-6, pero esta implementación utiliza el operador `?`.

Nombre del archivo: `src/main.rs`

```rust
use std::fs::File;
use std::io::{self, Read};

fn read_username_from_file() -> Result<String, io::Error> {
    let mut username_file = File::open("hello.txt")?;
    let mut username = String::new();
    username_file.read_to_string(&mut username)?;
    Ok(username)
}
```

Lista 9-7: Una función que devuelve errores al código que llama usando el operador `?`

El `?` colocado después de un valor de `Result` está definido para funcionar de manera casi igual que las expresiones `match` que definimos para manejar los valores de `Result` en la Lista 9-6. Si el valor del `Result` es un `Ok`, el valor dentro del `Ok` se devolverá desde esta expresión y el programa continuará. Si el valor es un `Err`, el `Err` se devolverá desde la función completa como si hubiéramos usado la palabra clave `return`, de modo que el valor de error se propague al código que llama.

Hay una diferencia entre lo que hace la expresión `match` de la Lista 9-6 y lo que hace el operador `?`: los valores de error en los que se llama al operador `?` pasan por la función `from`, definida en el trato `From` de la biblioteca estándar, que se utiliza para convertir valores de un tipo a otro. Cuando el operador `?` llama a la función `from`, el tipo de error recibido se convierte en el tipo de error definido en el tipo de retorno de la función actual. Esto es útil cuando una función devuelve un tipo de error para representar todas las formas en que una función puede fallar, incluso si partes pueden fallar por muchas razones diferentes.

Por ejemplo, podríamos cambiar la función `read_username_from_file` de la Lista 9-7 para devolver un tipo de error personalizado llamado `OurError` que definimos. Si también definimos `impl From<io::Error> for OurError` para construir una instancia de `OurError` a partir de un `io::Error`, entonces las llamadas al operador `?` en el cuerpo de `read_username_from_file` llamarán a `from` y convertirán los tipos de error sin necesidad de agregar más código a la función.

En el contexto de la Lista 9-7, el `?` al final de la llamada a `File::open` devolverá el valor dentro de un `Ok` a la variable `username_file`. Si se produce un error, el operador `?` devolverá temprano de la función completa y dará cualquier valor `Err` al código que llama. Lo mismo se aplica al `?` al final de la llamada a `read_to_string`.

El operador `?` elimina mucha plantilla y hace que la implementación de esta función sea más simple. Incluso podríamos acortar este código aún más enlazando llamadas a métodos inmediatamente después del `?`, como se muestra en la Lista 9-8.

Nombre del archivo: `src/main.rs`

```rust
use std::fs::File;
use std::io::{self, Read};

fn read_username_from_file() -> Result<String, io::Error> {
    let mut username = String::new();

    File::open("hello.txt")?.read_to_string(&mut username)?;

    Ok(username)
}
```

Lista 9-8: Enlazando llamadas a métodos después del operador `?`

Hemos movido la creación del nuevo `String` en `username` al principio de la función; esa parte no ha cambiado. En lugar de crear una variable `username_file`, hemos enlazado la llamada a `read_to_string` directamente en el resultado de `File::open("hello.txt")?`. Todavía tenemos un `?` al final de la llamada a `read_to_string`, y todavía devolvemos un valor `Ok` que contiene `username` cuando tanto `File::open` como `read_to_string` tienen éxito en lugar de devolver errores. La funcionalidad es nuevamente la misma que en la Lista 9-6 y la Lista 9-7; esta es solo una forma diferente y más cómoda de escribirlo.

La Lista 9-9 muestra una forma de hacerlo aún más corto usando `fs::read_to_string`.

Nombre del archivo: `src/main.rs`

```rust
use std::fs;
use std::io;

fn read_username_from_file() -> Result<String, io::Error> {
    fs::read_to_string("hello.txt")
}
```

Lista 9-9: Usando `fs::read_to_string` en lugar de abrir y luego leer el archivo

Leer un archivo en una cadena es una operación bastante común, por lo que la biblioteca estándar proporciona la función conveniente `fs::read_to_string` que abre el archivo, crea un nuevo `String`, lee el contenido del archivo, coloca el contenido en ese `String` y lo devuelve. Por supuesto, usar `fs::read_to_string` no nos da la oportunidad de explicar todo el manejo de errores, así que lo hicimos de la manera más larga primero.
