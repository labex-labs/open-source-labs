# Señalando a los subprocesos para que dejen de escuchar trabajos

Con todos los cambios que hemos realizado, nuestro código se compila sin advertencias. Sin embargo, la mala noticia es que este código no funciona de la manera que queremos todavía. La clave está en la lógica de las clausuras ejecutadas por los subprocesos de las instancias de `Worker`: en este momento, llamamos a `join`, pero eso no detendrá los subprocesos, porque `loop` para siempre buscando trabajos. Si intentamos eliminar nuestro `ThreadPool` con nuestra implementación actual de `drop`, el subproceso principal se bloqueará para siempre, esperando a que el primer subproceso termine.

Para solucionar este problema, necesitaremos un cambio en la implementación de `drop` de `ThreadPool` y luego un cambio en el `Worker` loop.

Primero, cambiaremos la implementación de `drop` de `ThreadPool` para eliminar explícitamente el `sender` antes de esperar a que los subprocesos terminen. La Lista 20-23 muestra los cambios en `ThreadPool` para eliminar explícitamente `sender`. Usamos la misma técnica de `Option` y `take` que hicimos con el subproceso para poder mover `sender` fuera de `ThreadPool`.

Nombre de archivo: `src/lib.rs`

```rust
pub struct ThreadPool {
    workers: Vec<Worker>,
    sender: Option<mpsc::Sender<Job>>,
}
--snip--
impl ThreadPool {
    pub fn new(size: usize) -> ThreadPool {
        --snip--

        ThreadPool {
            workers,
            sender: Some(sender),
        }
    }

    pub fn execute<F>(&self, f: F)
    where
        F: FnOnce() + Send + 'static,
    {
        let job = Box::new(f);

        self.sender
           .as_ref()
           .unwrap()
           .send(job)
           .unwrap();
    }
}

impl Drop for ThreadPool {
    fn drop(&mut self) {
      1 drop(self.sender.take());

        for worker in &mut self.workers {
            println!("Apagando el trabajador {}", worker.id);

            if let Some(thread) = worker.thread.take() {
                thread.join().unwrap();
            }
        }
    }
}
```

Lista 20-23: Eliminando explícitamente `sender` antes de unir los subprocesos `Worker`

Eliminar `sender` \[1\] cierra el canal, lo que indica que no se enviarán más mensajes. Cuando eso sucede, todas las llamadas a `recv` que realizan las instancias de `Worker` en el bucle infinito devolverán un error. En la Lista 20-24, cambiamos el `Worker` loop para salir del bucle de manera adecuada en ese caso, lo que significa que los subprocesos terminarán cuando la implementación de `drop` de `ThreadPool` llame a `join` en ellos.

Nombre de archivo: `src/lib.rs`

```rust
impl Worker {
    fn new(
        id: usize,
        receiver: Arc<Mutex<mpsc::Receiver<Job>>>,
    ) -> Worker {
        let thread = thread::spawn(move || loop {
            let message = receiver.lock().unwrap().recv();

            match message {
                Ok(job) => {
                    println!(
                        "Worker {id} recibió un trabajo; ejecutando."
                    );

                    job();
                }
                Err(_) => {
                    println!(
                        "Worker {id} se está apagando."
                    );
                    break;
                }
            }
        });

        Worker {
            id,
            thread: Some(thread),
        }
    }
}
```

Lista 20-24: Saliendo explícitamente del bucle cuando `recv` devuelve un error

Para ver este código en acción, modificaremos `main` para aceptar solo dos solicitudes antes de apagar adecuadamente el servidor, como se muestra en la Lista 20-25.

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();
    let pool = ThreadPool::new(4);

    for stream in listener.incoming().take(2) {
        let stream = stream.unwrap();

        pool.execute(|| {
            handle_connection(stream);
        });
    }

    println!("Apagando.");
}
```

Lista 20-25: Apagando el servidor después de atender dos solicitudes saliendo del bucle

No querrías que un servidor web del mundo real se apagara después de atender solo dos solicitudes. Este código solo demuestra que el apagado adecuado y la limpieza están en funcionamiento.

El método `take` está definido en el trato `Iterator` y limita la iteración a los primeros dos elementos como máximo. El `ThreadPool` saldrá del ámbito al final de `main`, y la implementación de `drop` se ejecutará.

Inicia el servidor con `cargo run` y haz tres solicitudes. La tercera solicitud debe generar un error, y en tu terminal deberías ver una salida similar a esta:

```bash
$ cargo run
   Compilando hello v0.1.0 (file:///projects/hello)
    Finished dev [no optimizado + información de depuración] target(s) en 1.0s
     Ejecutando `target/debug/hello`
Worker 0 recibió un trabajo; ejecutando.
Apagando.
Apagando el trabajador 0
Worker 3 recibió un trabajo; ejecutando.
Worker 1 se desconectó; apagando.
Worker 2 se desconectó; apagando.
Worker 3 se desconectó; apagando.
Worker 0 se desconectó; apagando.
Apagando el trabajador 1
Apagando el trabajador 2
Apagando el trabajador 3
```

Es posible que veas un orden diferente de los IDs de `Worker` y los mensajes impresos. Podemos ver cómo funciona este código a partir de los mensajes: las instancias de `Worker` 0 y 3 recibieron las primeras dos solicitudes. El servidor dejó de aceptar conexiones después de la segunda conexión, y la implementación de `Drop` en `ThreadPool` comienza a ejecutarse antes de que `Worker` 3 incluso comience su trabajo. Eliminar el `sender` desconecta todas las instancias de `Worker` y les dice que se apaguen. Las instancias de `Worker` imprimen un mensaje cada vez que se desconectan, y luego el grupo de subprocesos llama a `join` para esperar a que cada subproceso de `Worker` termine.

Observa un aspecto interesante de esta ejecución en particular: el `ThreadPool` eliminó el `sender`, y antes de que cualquier `Worker` recibiera un error, intentamos unir `Worker` 0. `Worker` 0 aún no había recibido un error de `recv`, por lo que el subproceso principal se bloqueó, esperando a que `Worker` 0 terminara. Mientras tanto, `Worker` 3 recibió un trabajo y luego todos los subprocesos recibieron un error. Cuando `Worker` 0 terminó, el subproceso principal esperó a que el resto de las instancias de `Worker` terminaran. En ese momento, todas habían salido de sus bucles y se detuvieron.

¡Felicidades! Ahora hemos completado nuestro proyecto; tenemos un servidor web básico que utiliza un grupo de subprocesos para responder de manera asincrónica. Somos capaces de realizar un apagado adecuado del servidor, lo que limpia todos los subprocesos del grupo. Visita *https://www.nostarch.com/Rust2021* para descargar el código completo de este capítulo para referencia.

Podríamos hacer más aquí. Si quieres continuar mejorando este proyecto, aquí hay algunas ideas:

- Agregar más documentación a `ThreadPool` y sus métodos públicos.
- Agregar pruebas de la funcionalidad de la biblioteca.
- Cambiar las llamadas a `unwrap` a un manejo de errores más robusto.
- Usar `ThreadPool` para realizar alguna tarea diferente a atender solicitudes web.
- Encuentra un cráneo de grupo de subprocesos en *https://crates.io* e implementa un servidor web similar usando el cráneo en lugar de eso. Luego compara su API y robustez con el grupo de subprocesos que implementamos.
