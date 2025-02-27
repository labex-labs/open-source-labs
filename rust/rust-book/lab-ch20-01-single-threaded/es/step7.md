# Validando la solicitud y respondiendo selectivamente

En este momento, nuestro servidor web devolverá el HTML del archivo sin importar lo que el cliente haya solicitado. Agregemos funcionalidad para comprobar que el navegador está solicitando _/_ antes de devolver el archivo HTML, y devolver un error si el navegador solicita algo más. Para hacer esto, necesitamos modificar `handle_connection`, como se muestra en la Lista 20-6. Este nuevo código comprueba el contenido de la solicitud recibida en comparación con lo que sabemos que es una solicitud a _/_ y agrega bloques `if` y `else` para tratar las solicitudes de manera diferente.

Nombre del archivo: `src/main.rs`

```rust
--snip--

fn handle_connection(mut stream: TcpStream) {
    let buf_reader = BufReader::new(&mut stream);
  1 let request_line = buf_reader
      .lines()
      .next()
      .unwrap()
      .unwrap();

  2 if request_line == "GET / HTTP/1.1" {
        let status_line = "HTTP/1.1 200 OK";
        let contents = fs::read_to_string("hello.html").unwrap();
        let length = contents.len();

        let response = format!(
            "{status_line}\r\n\
             Content-Length: {length}\r\n\r\n\
             {contents}"
        );

        stream.write_all(response.as_bytes()).unwrap();
  3 } else {
        // alguna otra solicitud
    }
}
```

Lista 20-6: Manejando solicitudes a _/_ de manera diferente a otras solicitudes

Solo vamos a mirar la primera línea de la solicitud HTTP, por lo que en lugar de leer toda la solicitud en un vector, estamos llamando a `next` para obtener el primer elemento del iterador \[1\]. El primer `unwrap` se encarga de la `Option` y detiene el programa si el iterador no tiene elementos. El segundo `unwrap` maneja el `Result` y tiene el mismo efecto que el `unwrap` que estaba en el `map` agregado en la Lista 20-2.

Luego, comprobamos la `request_line` para ver si es igual a la línea de solicitud de una solicitud GET al camino _/_ \[2\]. Si es así, el bloque `if` devuelve el contenido de nuestro archivo HTML.

Si la `request_line` no es igual a la solicitud GET al camino _/_, significa que hemos recibido alguna otra solicitud. Agregaremos código al bloque `else` \[3\] en un momento para responder a todas las demás solicitudes.

Ejecute este código ahora y solicite _127.0.0.1:7878_; debería obtener el HTML en _hello.html_. Si realiza cualquier otra solicitud, como _127.0.0.1:7878/something-else_, obtendrá un error de conexión como los que vio al ejecutar el código en la Lista 20-1 y la Lista 20-2.

Ahora agregemos el código de la Lista 20-7 al bloque `else` para devolver una respuesta con el código de estado 404, que indica que no se encontró el contenido de la solicitud. También devolveremos algunos HTML para una página que se renderice en el navegador indicando la respuesta al usuario final.

Nombre del archivo: `src/main.rs`

```rust
--snip--
} else {
  1 let status_line = "HTTP/1.1 404 NOT FOUND";
  2 let contents = fs::read_to_string("404.html").unwrap();
    let length = contents.len();

    let response = format!(
        "{status_line}\r\n\
         Content-Length: {length}\r\n\r\n
         {contents}"
    );

    stream.write_all(response.as_bytes()).unwrap();
}
```

Lista 20-7: Respondiendo con código de estado 404 y una página de error si se solicita algo diferente a _/_

Aquí, nuestra respuesta tiene una línea de estado con código de estado 404 y la frase de motivo `NOT FOUND` \[1\]. El cuerpo de la respuesta será el HTML en el archivo _404.html_ \[1\]. Necesitará crear un archivo _404.html_ junto a _hello.html_ para la página de error; una vez más, puede usar cualquier HTML que desee, o use el HTML de ejemplo en la Lista 20-8.

Nombre del archivo: `404.html`

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>¡Hola!</title>
  </head>
  <body>
    <h1>Uy!</h1>
    <p>Lo siento, no sé lo que estás pidiendo.</p>
  </body>
</html>
```

Lista 20-8: Contenido de muestra para la página que se enviará de vuelta con cualquier respuesta 404

Con estos cambios, ejecute su servidor nuevamente. Solicitar _127.0.0.1:7878_ debería devolver el contenido de _hello.html_, y cualquier otra solicitud, como _127.0.0.1:7878/foo_, debería devolver el HTML de error de _404.html_.
