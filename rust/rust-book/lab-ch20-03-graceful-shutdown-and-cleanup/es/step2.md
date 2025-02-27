# Implementando el trato Drop en ThreadPool

Comencemos implementando `Drop` en nuestro grupo de subprocesos. Cuando se elimina el grupo, todos nuestros subprocesos deben unirse para asegurarse de terminar su trabajo. La Lista 20-22 muestra un primer intento de implementación de `Drop`; este código aún no funcionará correctamente.

Nombre de archivo: `src/lib.rs`

```rust
impl Drop for ThreadPool {
    fn drop(&mut self) {
      1 for worker in &mut self.workers {
          2 println!("Apagando el trabajador {}", worker.id);

          3 worker.thread.join().unwrap();
        }
    }
}
```

Lista 20-22: Uniendo cada subproceso cuando el grupo de subprocesos sale del ámbito

Primero, recorremos cada uno de los `workers` del grupo de subprocesos \[1\]. Usamos `&mut` para esto porque `self` es una referencia mutable, y también necesitamos poder mutar `worker`. Para cada `worker`, imprimimos un mensaje diciendo que esta instancia particular de `Worker` se está apagando \[2\], y luego llamamos a `join` en el subproceso de esa instancia de `Worker` \[3\]. Si la llamada a `join` falla, usamos `unwrap` para que Rust se detenga abruptamente y entre en un apagado no adecuado.

Aquí está el error que obtenemos cuando compilamos este código:

```bash
error[E0507]: no se puede mover `worker.thread` que está detrás de una
referencia mutable
    --> src/lib.rs:52:13
     |
52   |             worker.thread.join().unwrap();
     |             ^^^^^^^^^^^^^ ------ `worker.thread` movido debido a
este método de llamada
     |             |
     |             el movimiento ocurre porque `worker.thread` tiene el
tipo `JoinHandle<()>`, que no implementa el trato `Copy`
     |
nota: esta función toma posesión del receptor `self`, lo que mueve
`worker.thread`
```

El error nos dice que no podemos llamar a `join` porque solo tenemos un préstamo mutable de cada `worker` y `join` toma posesión de su argumento. Para resolver este problema, necesitamos mover el subproceso fuera de la instancia de `Worker` que posee `thread` para que `join` pueda consumir el subproceso. Hicimos esto en la Lista 17-15: si `Worker` contiene una `Option<thread::JoinHandle<()>>` en lugar de eso, podemos llamar al método `take` en la `Option` para mover el valor fuera de la variante `Some` y dejar una variante `None` en su lugar. En otras palabras, un `Worker` que está en ejecución tendrá una variante `Some` en `thread`, y cuando queramos limpiar un `Worker`, reemplazaremos `Some` con `None` para que el `Worker` no tenga un subproceso para ejecutar.

Entonces, sabemos que queremos actualizar la definición de `Worker` de la siguiente manera:

Nombre de archivo: `src/lib.rs`

```rust
struct Worker {
    id: usize,
    thread: Option<thread::JoinHandle<()>>,
}
```

Ahora, apoyémonos en el compilador para encontrar los otros lugares que necesitan cambiar. Al revisar este código, obtenemos dos errores:

```bash
error[E0599]: no se encontró el método llamado `join` para el enum
`Option` en el ámbito actual
  --> src/lib.rs:52:27
   |
52 |             worker.thread.join().unwrap();
   |                           ^^^^ método no encontrado en
`Option<JoinHandle<()>>`

error[E0308]: tipos no coincidentes
  --> src/lib.rs:72:22
   |
72 |         Worker { id, thread }
   |                      ^^^^^^ se esperaba el enum `Option`, se
encontró la struct `JoinHandle`
   |
   = nota: se esperaba el enum `Option<JoinHandle<()>>`
            se encontró la struct `JoinHandle<_>`
ayuda: intente envolver la expresión en `Some`
   |
72 |         Worker { id, thread: Some(thread) }
   |                      +++++++++++++      +
```

Vamos a abordar el segundo error, que apunta al código al final de `Worker::new`; necesitamos envolver el valor de `thread` en `Some` cuando creamos un nuevo `Worker`. Haga los siguientes cambios para corregir este error:

Nombre de archivo: `src/lib.rs`

```rust
impl Worker {
    fn new(
        id: usize,
        receiver: Arc<Mutex<mpsc::Receiver<Job>>>,
    ) -> Worker {
        --snip--

        Worker {
            id,
            thread: Some(thread),
        }
    }
}
```

El primer error está en nuestra implementación de `Drop`. Mencionamos anteriormente que teníamos la intención de llamar a `take` en el valor de `Option` para mover `thread` fuera de `worker`. Los siguientes cambios lo harán:

Nombre de archivo: `src/lib.rs`

```rust
impl Drop for ThreadPool {
    fn drop(&mut self) {
        for worker in &mut self.workers {
            println!("Apagando el trabajador {}", worker.id);

          1 if let Some(thread) = worker.thread.take() {
              2 thread.join().unwrap();
            }
        }
    }
}
```

Como se discutió en el Capítulo 17, el método `take` en `Option` toma la variante `Some` y deja `None` en su lugar. Estamos usando `if let` para desestructurar la `Some` y obtener el subproceso \[1\]; luego llamamos a `join` en el subproceso \[2\]. Si el subproceso de una instancia de `Worker` ya es `None`, sabemos que el `Worker` ya ha tenido su subproceso limpiado, por lo que en ese caso nada pasa.
