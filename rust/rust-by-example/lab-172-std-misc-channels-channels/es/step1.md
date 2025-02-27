# Canales

Rust proporciona `canales` asincrónicos para la comunicación entre hilos. Los canales permiten un flujo unidireccional de información entre dos puntos finales: el `Sender` y el `Receiver`.

```rust
use std::sync::mpsc::{Sender, Receiver};
use std::sync::mpsc;
use std::thread;

static NTHREADS: i32 = 3;

fn main() {
    // Los canales tienen dos puntos finales: el `Sender<T>` y el `Receiver<T>`,
    // donde `T` es el tipo del mensaje que se va a transferir
    // (la anotación de tipo es superflua)
    let (tx, rx): (Sender<i32>, Receiver<i32>) = mpsc::channel();
    let mut children = Vec::new();

    for id in 0..NTHREADS {
        // El punto final del emisor se puede copiar
        let thread_tx = tx.clone();

        // Cada hilo enviará su id a través del canal
        let child = thread::spawn(move || {
            // El hilo toma posesión de `thread_tx`
            // Cada hilo encola un mensaje en el canal
            thread_tx.send(id).unwrap();

            // El envío es una operación no bloqueante, el hilo continuará
            // inmediatamente después de enviar su mensaje
            println!("hilo {} terminado", id);
        });

        children.push(child);
    }

    // Aquí, todos los mensajes se recopilan
    let mut ids = Vec::with_capacity(NTHREADS as usize);
    for _ in 0..NTHREADS {
        // El método `recv` elige un mensaje del canal
        // `recv` bloqueará el hilo actual si no hay mensajes disponibles
        ids.push(rx.recv());
    }

    // Espera a que los hilos terminen cualquier trabajo restante
    for child in children {
        child.join().expect("oops! el hilo hijo entró en pánico");
    }

    // Muestra el orden en el que se enviaron los mensajes
    println!("{:?}", ids);
}
```
