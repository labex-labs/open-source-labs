# Implementando el método execute

Finalmente, implementemos el método `execute` en `ThreadPool`. También cambiaremos `Job` de una estructura a un alias de tipo para un objeto de trato que contiene el tipo de clausura que recibe `execute`. Como se discutió en "Creating Type Synonyms with Type Aliases", los alias de tipo nos permiten hacer que los tipos largos sean más cortos para mayor facilidad de uso. Echa un vistazo a la Lista 20-19.

Nombre de archivo: `src/lib.rs`

```rust
--snip--

type Job = Box<dyn FnOnce() + Send + 'static>;

impl ThreadPool {
    --snip--

    pub fn execute<F>(&self, f: F)
    where
        F: FnOnce() + Send + 'static,
    {
      1 let job = Box::new(f);

      2 self.sender.send(job).unwrap();
    }
}

--snip--
```

Lista 20-19: Creando un alias de tipo `Job` para un `Box` que contiene cada clausura y luego enviando el trabajo por el canal

Después de crear una nueva instancia de `Job` usando la clausura que obtenemos en `execute` \[1\], enviamos ese trabajo por el extremo de envío del canal \[2\]. Estamos llamando a `unwrap` en `send` para el caso en el que el envío falle. Esto podría suceder, por ejemplo, si detenemos la ejecución de todos nuestros subprocesos, lo que significa que el extremo de recepción ha dejado de recibir nuevos mensajes. En este momento, no podemos detener la ejecución de nuestros subprocesos: nuestros subprocesos continúan ejecutándose mientras el grupo existe. La razón por la que usamos `unwrap` es que sabemos que el caso de error no sucederá, pero el compilador no lo sabe.

Pero todavía no hemos terminado ¡Todavía! En el `Worker`, la clausura que se le pasa a `thread::spawn` todavía solo _referencia_ el extremo de recepción del canal. En cambio, necesitamos que la clausura se repita para siempre, pidiendo al extremo de recepción del canal un trabajo y ejecutando el trabajo cuando lo recibe. Hagamos el cambio mostrado en la Lista 20-20 en `Worker::new`.

Nombre de archivo: `src/lib.rs`

```rust
--snip--

impl Worker {
    fn new(
        id: usize,
        receiver: Arc<Mutex<mpsc::Receiver<Job>>>,
    ) -> Worker {
        let thread = thread::spawn(move || loop {
            let job = receiver
              1.lock()
              2.unwrap()
              3.recv()
              4.unwrap();

            println!("Worker {id} got a job; executing.");

            job();
        });

        Worker { id, thread }
    }
}
```

Lista 20-20: Recibiendo y ejecutando los trabajos en el subproceso de la instancia de `Worker`

Aquí, primero llamamos a `lock` en el `receptor` para adquirir el mutex \[1\], y luego llamamos a `unwrap` para generar un error en cualquier error \[2\]. Adquirir un bloqueo puede fallar si el mutex está en un estado _envenenado_, lo que puede suceder si algún otro subproceso generó un error mientras mantenía el bloqueo en lugar de liberarlo. En esta situación, llamar a `unwrap` para que este subproceso genere un error es la acción correcta a tomar. Siéntase libre de cambiar este `unwrap` por un `expect` con un mensaje de error que tenga sentido para usted.

Si obtenemos el bloqueo del mutex, llamamos a `recv` para recibir un `Job` del canal \[3\]. Un último `unwrap` también se salta cualquier error aquí \[4\], que podría ocurrir si el subproceso que mantiene el emisor se ha detenido, de manera similar a cómo el método `send` devuelve `Err` si el receptor se detiene.

La llamada a `recv` se bloquea, por lo que si todavía no hay un trabajo, el subproceso actual esperará hasta que un trabajo esté disponible. El `Mutex<T>` asegura que solo un subproceso `Worker` a la vez intenta solicitar un trabajo.

Nuestro grupo de subprocesos ahora está en un estado de funcionamiento ¡Dale un `cargo run` y haz algunas solicitudes!

```bash
[object Object]
```

¡Éxito! Ahora tenemos un grupo de subprocesos que ejecuta conexiones de forma asincrónica. Nunca se crean más de cuatro subprocesos, por lo que nuestro sistema no se sobrecargará si el servidor recibe muchas solicitudes. Si hacemos una solicitud a _/sleep_, el servidor podrá atender otras solicitudes haciéndolas ejecutar otro subproceso.

> Nota: Si abres _/sleep_ en múltiples ventanas del navegador simultáneamente, es posible que se carguen una a una con intervalos de cinco segundos. Algunos navegadores web ejecutan múltiples instancias de la misma solicitud secuencialmente por razones de caché. Esta limitación no es causada por nuestro servidor web.

Después de aprender sobre el bucle `while let` en el Capítulo 18, es posible que te preguntes por qué no escribimos el código del subproceso `Worker` como se muestra en la Lista 20-21.

Nombre de archivo: `src/lib.rs`

```rust
--snip--

impl Worker {
    fn new(
        id: usize,
        receiver: Arc<Mutex<mpsc::Receiver<Job>>>,
    ) -> Worker {
        let thread = thread::spawn(move || {
            while let Ok(job) = receiver.lock().unwrap().recv() {
                println!("Worker {id} got a job; executing.");

                job();
            }
        });

        Worker { id, thread }
    }
}
```

Lista 20-21: Una implementación alternativa de `Worker::new` usando `while let`

Este código se compila y ejecuta pero no produce el comportamiento de subprocesamiento deseado: una solicitud lenta todavía hará que otras solicitudes esperen a ser procesadas. La razón es algo sutil: la estructura `Mutex` no tiene un método público `unlock` porque la propiedad del bloqueo se basa en la duración de la `MutexGuard<T>` dentro del `LockResult<MutexGuard<T>>` que devuelve el método `lock`. En tiempo de compilación, el verificador de préstamos puede entonces aplicar la regla de que un recurso protegido por un `Mutex` no puede ser accedido a menos que mantengamos el bloqueo. Sin embargo, esta implementación también puede causar que el bloqueo se mantenga más tiempo del esperado si no tenemos en cuenta la duración de la `MutexGuard<T>`.

El código de la Lista 20-20 que usa `let job = receiver.lock().unwrap().recv().unwrap();` funciona porque con `let`, cualquier valor temporal usado en la expresión en el lado derecho del signo igual se descarta inmediatamente cuando la declaración `let` finaliza. Sin embargo, `while let` (y `if let` y `match`) no descarta valores temporales hasta el final del bloque asociado. En la Lista 20-21, el bloqueo permanece durante la duración de la llamada a `job()`, lo que significa que otras instancias de `Worker` no pueden recibir trabajos.
