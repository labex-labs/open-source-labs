# Escuchando la conexión TCP

Nuestro servidor web necesita escuchar una conexión TCP, por lo que esa es la primera parte en la que trabajaremos. La biblioteca estándar ofrece un módulo `std::net` que nos permite hacer esto. Vamos a crear un nuevo proyecto de la forma habitual:

```bash
$ cargo new hello
     Creado proyecto binario (aplicación) `hello`
$ cd hello
```

Ahora, ingrese el código de la Lista 20-1 en `src/main.rs` para comenzar. Este código escuchará en la dirección local `127.0.0.1:7878` para flujos TCP entrantes. Cuando reciba un flujo entrante, imprimirá `Conexión establecida!`.

Nombre del archivo: `src/main.rs`

```rust
use std::net::TcpListener;

fn main() {
  1 let listener = TcpListener::bind("127.0.0.1:7878").unwrap();

  2 for stream in listener.incoming() {
      3 let stream = stream.unwrap();

      4 println!("Conexión establecida!");
    }
}
```

Lista 20-1: Escuchando flujos entrantes y imprimiendo un mensaje cuando recibimos un flujo

Utilizando `TcpListener`, podemos escuchar conexiones TCP en la dirección `127.0.0.1:7878` \[1\]. En la dirección, la sección antes de los dos puntos es una dirección IP que representa su computadora (esto es lo mismo en cada computadora y no representa específicamente la computadora de los autores), y `7878` es el puerto. Hemos elegido este puerto por dos razones: HTTP normalmente no se acepta en este puerto, por lo que es improbable que nuestro servidor entre en conflicto con cualquier otro servidor web que pueda tener en su máquina, y 7878 es _rust_ tecleado en un teléfono.

La función `bind` en este escenario funciona como la función `new` en el sentido de que devolverá una nueva instancia de `TcpListener`. La función se llama `bind` porque, en red, conectarse a un puerto para escuchar se conoce como "enlazarse a un puerto".

La función `bind` devuelve un `Result<T, E>`, lo que indica que es posible que el enlace falle. Por ejemplo, conectarse al puerto 80 requiere privilegios de administrador (los no administradores solo pueden escuchar en puertos superiores a 1023), por lo que si intentamos conectarnos al puerto 80 sin ser administrador, el enlace no funcionará. El enlace también no funcionaría, por ejemplo, si ejecutamos dos instancias de nuestro programa y, por lo tanto, tenemos dos programas escuchando en el mismo puerto. Debido a que estamos escribiendo un servidor básico solo con fines de aprendizaje, no nos preocuparemos por manejar este tipo de errores; en cambio, usamos `unwrap` para detener el programa si ocurren errores.

El método `incoming` en `TcpListener` devuelve un iterador que nos da una secuencia de flujos \[2\] (más específicamente, flujos del tipo `TcpStream`). Un solo _flujo_ representa una conexión abierta entre el cliente y el servidor. Una _conexión_ es el nombre para todo el proceso de solicitud y respuesta en el que un cliente se conecta al servidor, el servidor genera una respuesta y el servidor cierra la conexión. En consecuencia, leeremos desde el `TcpStream` para ver lo que el cliente envió y luego escribiremos nuestra respuesta en el flujo para enviar datos de regreso al cliente. En general, este `for` loop procesará cada conexión por turnos y generará una serie de flujos para que los manejemos.

Por ahora, nuestro manejo del flujo consiste en llamar a `unwrap` para terminar nuestro programa si el flujo tiene algún error \[3\]; si no hay errores, el programa imprime un mensaje \[4\]. Agregaremos más funcionalidad para el caso de éxito en la siguiente lista. La razón por la que podríamos recibir errores del método `incoming` cuando un cliente se conecta al servidor es que en realidad no estamos iterando sobre conexiones. En cambio, estamos iterando sobre _intentos de conexión_. La conexión puede no tener éxito por una serie de razones, muchas de ellas específicas del sistema operativo. Por ejemplo, muchos sistemas operativos tienen un límite al número de conexiones abiertas simultáneas que pueden admitir; nuevos intentos de conexión más allá de ese número producirán un error hasta que se cierren algunas de las conexiones abiertas.

Vamos a probar a ejecutar este código! Invocar `cargo run` en la terminal y luego cargar _127.0.0.1:7878_ en un navegador web. El navegador debe mostrar un mensaje de error como "Conexión cerrada" porque el servidor actualmente no está enviando ningún dato de vuelta. Pero cuando mire su terminal, debería ver varios mensajes que se imprimieron cuando el navegador se conectó al servidor!

         Ejecutando `target/debug/hello`
    Conexión establecida!
    Conexión establecida!
    Conexión establecida!

A veces verá varios mensajes impresos para una sola solicitud del navegador; la razón podría ser que el navegador está realizando una solicitud para la página así como una solicitud para otros recursos, como el icono _favicon.ico_ que aparece en la pestaña del navegador.

También podría ser que el navegador esté intentando conectarse al servidor varias veces porque el servidor no está respondiendo con ningún dato. Cuando `stream` sale del ámbito y se elimina al final del bucle, la conexión se cierra como parte de la implementación de `drop`. Los navegadores a veces manejan las conexiones cerradas reintentando, porque el problema podría ser temporal. El factor importante es que hemos obtenido con éxito un controlador para una conexión TCP!

Recuerde detener el programa presionando ctrl-C cuando haya terminado de ejecutar una versión particular del código. Luego reinicie el programa invocando el comando `cargo run` después de haber realizado cada conjunto de cambios de código para asegurarse de que está ejecutando el código más reciente.
