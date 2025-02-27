# Un toque de refactorización

En este momento, los bloques `if` y `else` tienen mucha repetición: ambos están leyendo archivos y escribiendo el contenido de los archivos en el flujo. Las únicas diferencias son la línea de estado y el nombre del archivo. Hagamos que el código sea más conciso extrayendo esas diferencias en líneas `if` y `else` separadas que asignarán los valores de la línea de estado y el nombre del archivo a variables; luego podemos usar esas variables incondicionalmente en el código para leer el archivo y escribir la respuesta. La Lista 20-9 muestra el código resultante después de reemplazar los grandes bloques `if` y `else`.

Nombre del archivo: `src/main.rs`

```rust
--snip--

fn handle_connection(mut stream: TcpStream) {
    --snip--

    let (status_line, filename) =
        if request_line == "GET / HTTP/1.1" {
            ("HTTP/1.1 200 OK", "hello.html")
        } else {
            ("HTTP/1.1 404 NOT FOUND", "404.html")
        };

    let contents = fs::read_to_string(filename).unwrap();
    let length = contents.len();

    let response = format!(
        "{status_line}\r\n\
         Content-Length: {length}\r\n\r\n\
         {contents}"
    );

    stream.write_all(response.as_bytes()).unwrap();
}
```

Lista 20-9: Refactorizando los bloques `if` y `else` para contener solo el código que difiere entre los dos casos

Ahora los bloques `if` y `else` solo devuelven los valores adecuados para la línea de estado y el nombre del archivo en una tupla; luego usamos la desestructuración para asignar estos dos valores a `status_line` y `filename` usando un patrón en la declaración `let`, como se discutió en el Capítulo 18.

El código previamente duplicado ahora está fuera de los bloques `if` y `else` y usa las variables `status_line` y `filename`. Esto hace que sea más fácil ver la diferencia entre los dos casos, y significa que solo tenemos un lugar para actualizar el código si queremos cambiar cómo funciona la lectura de archivos y la escritura de respuestas. El comportamiento del código en la Lista 20-9 será el mismo que el de la Lista 20-8.

¡Genial! Ahora tenemos un servidor web simple en aproximadamente 40 líneas de código de Rust que responde a una solicitud con una página de contenido y responde a todas las demás solicitudes con una respuesta 404.

Actualmente, nuestro servidor se ejecuta en un solo hilo, lo que significa que solo puede atender una solicitud a la vez. Vamos a examinar cómo eso puede ser un problema simulando algunas solicitudes lentas. Luego lo solucionaremos para que nuestro servidor pueda manejar múltiples solicitudes a la vez.
