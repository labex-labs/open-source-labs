# Simulando una solicitud lenta

Veremos cómo una solicitud que tarda en procesarse puede afectar otras solicitudes hechas a nuestra implementación actual de servidor. La Lista 20-10 implementa el manejo de una solicitud a _/sleep_ con una respuesta simulada lenta que hará que el servidor duerma durante cinco segundos antes de responder.

Nombre de archivo: `src/main.rs`

```rust
use std::{
    fs,
    io::{prelude::*, BufReader},
    net::{TcpListener, TcpStream},
    thread,
    time::Duration,
};
--snip--

fn handle_connection(mut stream: TcpStream) {
    --snip--

    let (status_line, filename) = 1 match &request_line[..] {
      2 "GET / HTTP/1.1" => ("HTTP/1.1 200 OK", "hello.html"),
      3 "GET /sleep HTTP/1.1" => {
            thread::sleep(Duration::from_secs(5));
            ("HTTP/1.1 200 OK", "hello.html")
        }
      4 _ => ("HTTP/1.1 404 NOT FOUND", "404.html"),
    };

    --snip--
}
```

Lista 20-10: Simulando una solicitud lenta durmiendo durante cinco segundos

Hemos cambiado de `if` a `match` ahora que tenemos tres casos \[1\]. Necesitamos hacer coincidir explícitamente en un trozo de `request_line` para hacer coincidir con los valores literales de cadena; `match` no hace referencia automática y desreferenciación, como lo hace el método de igualdad.

El primer brazo \[2\] es el mismo que el bloque `if` de la Lista 20-9. El segundo brazo \[3\] coincide con una solicitud a _/sleep_. Cuando se recibe esa solicitud, el servidor dormirá durante cinco segundos antes de renderizar la página HTML exitosa. El tercer brazo \[4\] es el mismo que el bloque `else` de la Lista 20-9.

Puedes ver lo primitivo que es nuestro servidor: las bibliotecas reales manejarían el reconocimiento de múltiples solicitudes de manera mucho menos verbosa.

Inicie el servidor usando `cargo run`. Luego abra dos ventanas del navegador: una para *http://127.0.0.1:7878* y la otra para *http://127.0.0.1:7878/sleep*. Si ingresa la URI _/_ varias veces, como antes, verá que responde rápidamente. Pero si ingresa _/sleep_ y luego carga _/_, verá que _/_ espera hasta que `sleep` haya dormido durante sus cinco segundos completos antes de cargar.

Hay múltiples técnicas que podríamos usar para evitar que las solicitudes se acumulen detrás de una solicitud lenta; la que implementaremos es un grupo de subprocesos.
