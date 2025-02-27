# Creación de un subproceso para cada solicitud

Primero, exploremos cómo podría verse nuestro código si creara un nuevo subproceso para cada conexión. Como se mencionó anteriormente, este no es nuestro plan final debido a los problemas de la posible creación de un número ilimitado de subprocesos, pero es un punto de partida para obtener primero un servidor multihilo funcional. Luego agregaremos el grupo de subprocesos como una mejora, y contrastar las dos soluciones será más fácil.

La Lista 20-11 muestra los cambios que se deben hacer a `main` para crear un nuevo subproceso para manejar cada flujo dentro del bucle `for`.

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();

    for stream in listener.incoming() {
        let stream = stream.unwrap();

        thread::spawn(|| {
            handle_connection(stream);
        });
    }
}
```

Lista 20-11: Creación de un nuevo subproceso para cada flujo

Como aprendiste en el Capítulo 16, `thread::spawn` creará un nuevo subproceso y luego ejecutará el código en la clausura en el nuevo subproceso. Si ejecutas este código y cargas _/sleep_ en tu navegador, luego _/_ en dos pestañas más del navegador, realmente verás que las solicitudes a _/_ no tienen que esperar a que _/sleep_ termine. Sin embargo, como mencionamos, esto eventualmente sobrecargará el sistema porque estarías creando nuevos subprocesos sin ningún límite.
