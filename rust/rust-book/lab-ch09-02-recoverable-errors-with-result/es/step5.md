# Propagación de errores

Cuando la implementación de una función llama a algo que podría fallar, en lugar de manejar el error dentro de la función misma, puedes devolver el error al código que la llama para que pueda decidir qué hacer. Esto se conoce como _propagar_ el error y le da más control al código que llama, donde puede haber más información o lógica que dicta cómo se debe manejar el error que la que tienes disponible en el contexto de tu código.

Por ejemplo, la Lista 9-6 muestra una función que lee un nombre de usuario de un archivo. Si el archivo no existe o no se puede leer, esta función devolverá esos errores al código que llamó a la función.

Nombre del archivo: `src/main.rs`

```rust
use std::fs::File;
use std::io::{self, Read};

1 fn read_username_from_file() -> Result<String, io::Error> {
  2 let username_file_result = File::open("hello.txt");

  3 let mut username_file = match username_file_result {
      4 Ok(file) => file,
      5 Err(e) => return Err(e),
    };

  6 let mut username = String::new();

  7 match username_file.read_to_string(&mut username) {
      8 Ok(_) => Ok(username),
      9 Err(e) => Err(e),
    }
}
```

Lista 9-6: Una función que devuelve errores al código que llama usando `match`

Esta función se puede escribir de manera mucho más corta, pero vamos a empezar haciéndola manualmente para explorar el manejo de errores; al final, mostraremos la forma más corta. Veamos primero el tipo de retorno de la función: `Result<String, io::Error>` \[1\]. Esto significa que la función está devolviendo un valor del tipo `Result<T, E>`, donde el parámetro genérico `T` ha sido rellenado con el tipo concreto `String` y el tipo genérico `E` ha sido rellenado con el tipo concreto `io::Error`.

Si esta función tiene éxito sin problemas, el código que llama a esta función recibirá un valor `Ok` que contiene un `String` - el `username` que esta función leyó del archivo \[8\]. Si esta función encuentra algún problema, el código que llama recibirá un valor `Err` que contiene una instancia de `io::Error` que contiene más información sobre cuáles fueron los problemas. Elegimos `io::Error` como el tipo de retorno de esta función porque ese es el tipo del valor de error devuelto por ambas operaciones que estamos llamando en el cuerpo de esta función que podrían fallar: la función `File::open` \[2\] y el método `read_to_string` \[7\].

El cuerpo de la función comienza llamando a la función `File::open` \[2\]. Luego manejamos el valor de `Result` con un `match` similar al `match` de la Lista 9-4. Si `File::open` tiene éxito, el manejador de archivo en la variable de patrón `file` \[4\] se convierte en el valor de la variable mutable `username_file` \[3\] y la función continúa. En el caso `Err`, en lugar de llamar a `panic!`, usamos la palabra clave `return` para salir temprano de la función por completo y pasar el valor de error de `File::open`, ahora en la variable de patrón `e`, de vuelta al código que llama como el valor de error de esta función \[5\].

Entonces, si tenemos un manejador de archivo en `username_file`, la función luego crea un nuevo `String` en la variable `username` \[6\] y llama al método `read_to_string` en el manejador de archivo en `username_file` para leer el contenido del archivo en `username` \[7\]. El método `read_to_string` también devuelve un `Result` porque podría fallar, aunque `File::open` tuvo éxito. Entonces necesitamos otro `match` para manejar ese `Result`: si `read_to_string` tiene éxito, entonces nuestra función ha tenido éxito, y devolvemos el nombre de usuario del archivo que ahora está en `username` envuelto en un `Ok`. Si `read_to_string` falla, devolvemos el valor de error de la misma manera que devolvemos el valor de error en el `match` que manejó el valor de retorno de `File::open`. Sin embargo, no necesitamos decir explícitamente `return`, porque esta es la última expresión en la función \[9\].

El código que llama a este código luego manejará recibir ya sea un valor `Ok` que contiene un nombre de usuario o un valor `Err` que contiene un `io::Error`. Es responsabilidad del código que llama decidir qué hacer con esos valores. Si el código que llama recibe un valor `Err`, podría llamar a `panic!` y detener el programa, usar un nombre de usuario predeterminado o buscar el nombre de usuario en algún lugar diferente al archivo, por ejemplo. No tenemos suficiente información sobre lo que el código que llama está realmente intentando hacer, así que propagamos toda la información de éxito o error hacia arriba para que la maneje adecuadamente.

Este patrón de propagación de errores es tan común en Rust que Rust proporciona el operador de interrogación `?` para hacerlo más fácil.
