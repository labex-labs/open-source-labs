# Creating a New Thread with spawn

Para crear un nuevo hilo, llamamos a la función `thread::spawn` y le pasamos una clausura (hablamos de clausuras en el Capítulo 13) que contiene el código que queremos ejecutar en el nuevo hilo. El ejemplo de la Lista 16-1 imprime algunos textos desde el hilo principal y otros textos desde un nuevo hilo.

Nombre de archivo: `src/main.rs`

```rust
use std::thread;
use std::time::Duration;

fn main() {
    thread::spawn(|| {
        for i in 1..10 {
            println!("hi number {i} from the spawned thread!");
            thread::sleep(Duration::from_millis(1));
        }
    });

    for i in 1..5 {
        println!("hi number {i} from the main thread!");
        thread::sleep(Duration::from_millis(1));
    }
}
```

Lista 16-1: Creando un nuevo hilo para imprimir una cosa mientras el hilo principal imprime otra cosa

Tenga en cuenta que cuando el hilo principal de un programa Rust finaliza, todos los hilos creados se detienen, independientemente de si han terminado de ejecutarse o no. La salida de este programa puede ser un poco diferente cada vez, pero se verá similar a lo siguiente:

    hi number 1 from the main thread!
    hi number 1 from the spawned thread!
    hi number 2 from the main thread!
    hi number 2 from the spawned thread!
    hi number 3 from the main thread!
    hi number 3 from the spawned thread!
    hi number 4 from the main thread!
    hi number 4 from the spawned thread!
    hi number 5 from the spawned thread!

Las llamadas a `thread::sleep` forzaran a un hilo a detener su ejecución durante un corto período de tiempo, permitiendo que otro hilo se ejecute. Los hilos probablemente tomarán turnos, pero eso no está garantizado: depende de cómo su sistema operativo programa los hilos. En esta ejecución, el hilo principal imprimió primero, aunque la declaración de impresión del hilo creado aparece primero en el código. Y aunque le dijimos al hilo creado que imprimiera hasta que `i` es 9, solo llegó a 5 antes de que el hilo principal se detuviera.

Si ejecuta este código y solo ve la salida del hilo principal, o no ve ninguna superposición, intente aumentar los números en los rangos para crear más oportunidades para que el sistema operativo cambie entre los hilos.
