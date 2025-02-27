# Escribiendo una respuesta

Vamos a implementar el envío de datos como respuesta a una solicitud del cliente. Las respuestas tienen el siguiente formato:

    Versión-HTTP Código-de-estado Frase-de-motivo CRLF
    encabezados CRLF
    cuerpo-del-mensaje

La primera línea es una _línea de estado_ que contiene la versión de HTTP utilizada en la respuesta, un código de estado numérico que resume el resultado de la solicitud y una frase de motivo que proporciona una descripción textual del código de estado. Después de la secuencia CRLF están cualquier encabezado, otra secuencia CRLF y el cuerpo de la respuesta.

Aquí hay un ejemplo de respuesta que utiliza la versión 1.1 de HTTP, tiene un código de estado de 200, una frase de motivo OK, ningún encabezado y ningún cuerpo:

```rust
HTTP/1.1 200 OK\r\n\r\n
```

El código de estado 200 es la respuesta de éxito estándar. El texto es una pequeña respuesta HTTP exitosa. Vamos a escribir esto en el flujo como respuesta a una solicitud exitosa! Desde la función `handle_connection`, elimine la llamada `println!` que estaba imprimiendo los datos de la solicitud y reemplacela con el código de la Lista 20-3.

Nombre del archivo: `src/main.rs`

```rust
fn handle_connection(mut stream: TcpStream) {
    let buf_reader = BufReader::new(&mut stream);
    let http_request: Vec<_> = buf_reader
     .lines()
     .map(|result| result.unwrap())
     .take_while(|line|!line.is_empty())
     .collect();

  1 let response = "HTTP/1.1 200 OK\r\n\r\n";

  2 stream.write_all(response.3 as_bytes()).unwrap();
}
```

Lista 20-3: Escribiendo una pequeña respuesta HTTP exitosa en el flujo

La primera línea nueva define la variable `response` que contiene los datos del mensaje de éxito \[1\]. Luego llamamos a `as_bytes` en nuestra `response` para convertir los datos de cadena a bytes \[3\]. El método `write_all` en `stream` toma un `&[u8]` y envía esos bytes directamente a través de la conexión \[2\]. Debido a que la operación `write_all` podría fallar, usamos `unwrap` en cualquier resultado de error como antes. Una vez más, en una aplicación real agregaría manejo de errores aquí.

Con estos cambios, ejecutemos nuestro código y hagamos una solicitud. Ya no estamos imprimiendo ningún dato en la terminal, por lo que no veremos ninguna salida aparte de la salida de Cargo. Cuando cargue _127.0.0.1:7878_ en un navegador web, debería obtener una página en blanco en lugar de un error. ¡Acabas de codificar a mano la recepción de una solicitud HTTP y el envío de una respuesta!
