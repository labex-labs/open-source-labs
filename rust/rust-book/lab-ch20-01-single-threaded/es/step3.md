# Leyendo la solicitud

¡Implementemos la funcionalidad para leer la solicitud del navegador! Para separar las preocupaciones de primero obtener una conexión y luego tomar alguna acción con la conexión, comenzaremos una nueva función para procesar conexiones. En esta nueva función `handle_connection`, leeremos datos del flujo TCP y los imprimiremos para que podamos ver los datos que el navegador está enviando. Cambie el código para que se vea como en la Lista 20-2.

Nombre del archivo: `src/main.rs`

```rust
1 use std::{
    io::{prelude::*, BufReader},
    net::{TcpListener, TcpStream},
};

fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();

    for stream in listener.incoming() {
        let stream = stream.unwrap();

      2 handle_connection(stream);
    }
}

fn handle_connection(mut stream: TcpStream) {
  3 let buf_reader = BufReader::new(&mut stream);
  4 let http_request: Vec<_> = buf_reader
      5.lines()
      6.map(|result| result.unwrap())
      7.take_while(|line|!line.is_empty())
       .collect();

  8 println!("Solicitud: {:#?}", http_request);
}
```

Lista 20-2: Leyendo del `TcpStream` e imprimiendo los datos

Traemos `std::io::prelude` y `std::io::BufReader` al alcance para tener acceso a los tratos y tipos que nos permiten leer y escribir en el flujo \[1\]. En el `for` loop de la función `main`, en lugar de imprimir un mensaje que diga que hemos establecido una conexión, ahora llamamos a la nueva función `handle_connection` y le pasamos el `stream` \[2\].

En la función `handle_connection`, creamos una nueva instancia de `BufReader` que envuelve una referencia mutable al `stream` \[3\]. `BufReader` agrega un buffer administrando las llamadas a los métodos del trato `std::io::Read` para nosotros.

Creamos una variable llamada `http_request` para recopilar las líneas de la solicitud que el navegador envía a nuestro servidor. Indicamos que queremos recopilar estas líneas en un vector agregando la anotación de tipo `Vec<_>` \[4\].

`BufReader` implementa el trato `std::io::BufRead`, que proporciona el método `lines` \[5\]. El método `lines` devuelve un iterador de `Result<String, std::io::Error>` dividiendo el flujo de datos cada vez que ve un byte de nueva línea. Para obtener cada `String`, mapeamos y `unwrap` cada `Result` \[6\]. El `Result` podría ser un error si los datos no son UTF-8 válidos o si hubo un problema al leer del flujo. Una vez más, un programa de producción debería manejar estos errores de manera más elegante, pero estamos eligiendo detener el programa en el caso de error por simplicidad.

El navegador señala el final de una solicitud HTTP enviando dos caracteres de nueva línea seguidos, por lo que para obtener una solicitud del flujo, tomamos líneas hasta que obtenemos una línea que es la cadena vacía \[7\]. Una vez que hemos recopilado las líneas en el vector, las estamos imprimiendo con un formato de depuración bonito \[8\] para que podamos ver las instrucciones que el navegador web está enviando a nuestro servidor.

¡Probemos este código! Inicie el programa y haga una solicitud en un navegador web nuevamente. Tenga en cuenta que todavía obtendremos una página de error en el navegador, pero la salida de nuestro programa en la terminal ahora se verá similar a esto:

```bash
$ cargo run
   Compilando hello v0.1.0 (file:///projects/hello)
    Terminada compilación en modo desarrollo [no optimizada + información de depuración] en 0.42s
     Ejecutando `target/debug/hello`
Solicitud: [
    "GET / HTTP/1.1",
    "Host: 127.0.0.1:7878",
    "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0)
Gecko/20100101 Firefox/99.0",
    "Accept:
text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*
;q=0.8",
    "Accept-Language: en-US,en;q=0.5",
    "Accept-Encoding: gzip, deflate, br",
    "DNT: 1",
    "Connection: keep-alive",
    "Upgrade-Insecure-Requests: 1",
    "Sec-Fetch-Dest: document",
    "Sec-Fetch-Mode: navegar",
    "Sec-Fetch-Site: ninguno",
    "Sec-Fetch-User:?1",
    "Cache-Control: max-age=0",
]
```

Dependiendo de su navegador, es posible que obtenga una salida ligeramente diferente. Ahora que estamos imprimiendo los datos de la solicitud, podemos ver por qué obtenemos múltiples conexiones a partir de una solicitud del navegador al ver la ruta después de `GET` en la primera línea de la solicitud. Si las conexiones repetidas están todas solicitando _/_, sabemos que el navegador está intentando obtener _/_ repetidamente porque no está recibiendo una respuesta de nuestro programa.

Analicemos estos datos de solicitud para entender lo que el navegador está pidiendo a nuestro programa.
