# Devolviendo HTML real

Implementemos la funcionalidad para devolver más que una página en blanco. Cree el nuevo archivo _hello.html_ en la raíz de su directorio de proyecto, no en el directorio `src`. Puede ingresar cualquier HTML que desee; la Lista 20-4 muestra una posibilidad.

Nombre del archivo: `hello.html`

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>¡Hola!</title>
  </head>
  <body>
    <h1>¡Hola!</h1>
    <p>Hola desde Rust</p>
  </body>
</html>
```

Lista 20-4: Un archivo HTML de muestra para devolver en una respuesta

Este es un documento HTML5 mínimo con un encabezado y algunos textos. Para devolver esto desde el servidor cuando se recibe una solicitud, modificaremos `handle_connection` como se muestra en la Lista 20-5 para leer el archivo HTML, agregarlo a la respuesta como cuerpo y enviarlo.

Nombre del archivo: `src/main.rs`

```rust
use std::{
  1 fs,
    io::{prelude::*, BufReader},
    net::{TcpListener, TcpStream},
};
--snip--

fn handle_connection(mut stream: TcpStream) {
    let buf_reader = BufReader::new(&mut stream);
    let http_request: Vec<_> = buf_reader
       .lines()
       .map(|result| result.unwrap())
       .take_while(|line|!line.is_empty())
       .collect();

    let status_line = "HTTP/1.1 200 OK";
    let contents = fs::read_to_string("hello.html").unwrap();
    let length = contents.len();

  2 let response = format!(
        "{status_line}\r\n\
         Content-Length: {length}\r\n\r\n\
         {contents}"
    );

    stream.write_all(response.as_bytes()).unwrap();
}
```

Lista 20-5: Enviando el contenido de _hello.html_ como cuerpo de la respuesta

Hemos agregado `fs` a la declaración `use` para traer el módulo de sistema de archivos de la biblioteca estándar al alcance \[1\]. El código para leer el contenido de un archivo a una cadena debería sonar familiar; lo usamos cuando leímos el contenido de un archivo para nuestro proyecto de E/S en la Lista 12-4.

Luego, usamos `format!` para agregar el contenido del archivo como cuerpo de la respuesta de éxito \[2\]. Para garantizar una respuesta HTTP válida, agregamos el encabezado `Content-Length` que se establece en el tamaño de nuestro cuerpo de respuesta, en este caso el tamaño de `hello.html`.

Ejecute este código con `cargo run` y cargue _127.0.0.1:7878_ en su navegador; debería ver su HTML renderizado.

Actualmente, estamos ignorando los datos de la solicitud en `http_request` y solo devolviendo el contenido del archivo HTML incondicionalmente. Eso significa que si intenta solicitar _127.0.0.1:7878/something-else_ en su navegador, todavía recibirá esta misma respuesta HTML. En este momento, nuestro servidor es muy limitado y no hace lo que la mayoría de los servidores web hacen. Queremos personalizar nuestras respuestas dependiendo de la solicitud y solo devolver el archivo HTML para una solicitud bien formada a _/_.
