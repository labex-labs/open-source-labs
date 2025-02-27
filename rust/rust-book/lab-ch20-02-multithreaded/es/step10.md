# Enviando solicitudes a los subprocesos a través de canales

El siguiente problema que abordaremos es que las clausuras que se le dan a `thread::spawn` no hacen absolutamente nada. Actualmente, obtenemos la clausura que queremos ejecutar en el método `execute`. Pero necesitamos dar a `thread::spawn` una clausura para ejecutar cuando creamos cada `Worker` durante la creación del `ThreadPool`.

Queremos que las estructuras `Worker` que acabamos de crear obtengan el código a ejecutar de una cola que se mantenga en el `ThreadPool` y lo envíen a su subproceso para que se ejecute.

Los canales que aprendimos sobre en el Capítulo 16, una forma simple de comunicarse entre dos subprocesos, sería perfecta para este caso de uso. Usaremos un canal para funcionar como la cola de trabajos, y `execute` enviará un trabajo desde el `ThreadPool` a las instancias de `Worker`, que lo enviarán a su subproceso. Aquí está el plan:

1.  El `ThreadPool` creará un canal y se quedará con el emisor.
2.  Cada `Worker` se quedará con el receptor.
3.  Crearemos una nueva estructura `Job` que contendrá las clausuras que queremos enviar por el canal.
4.  El método `execute` enviará el trabajo que quiere ejecutar a través del emisor.
5.  En su subproceso, el `Worker` recorrerá su receptor y ejecutará las clausuras de cualquier trabajo que reciba.

Comencemos creando un canal en `ThreadPool::new` y manteniendo el emisor en la instancia de `ThreadPool`, como se muestra en la Lista 20-16. La estructura `Job` no contiene nada por ahora pero será el tipo de elemento que estamos enviando por el canal.

Nombre de archivo: `src/lib.rs`

```rust
use std::{sync::mpsc, thread};

pub struct ThreadPool {
    workers: Vec<Worker>,
    sender: mpsc::Sender<Job>,
}

struct Job;

impl ThreadPool {
    --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

      1 let (sender, receiver) = mpsc::channel();

        let mut workers = Vec::with_capacity(size);

        for id in 0..size {
            workers.push(Worker::new(id));
        }

        ThreadPool { workers, 2 sender }
    }
    --snip--
}
```

Lista 20-16: Modificando `ThreadPool` para almacenar el emisor de un canal que transmite instancias de `Job`

En `ThreadPool::new`, creamos nuestro nuevo canal \[1\] y hacemos que el grupo se quede con el emisor \[2\]. Esto se compilará correctamente.

Intentemos pasar un receptor del canal a cada `Worker` cuando el grupo de subprocesos crea el canal. Sabemos que queremos usar el receptor en el subproceso que las instancias de `Worker` generan, así que haremos referencia al parámetro `receptor` en la clausura. El código de la Lista 20-17 todavía no se compilará.

Nombre de archivo: `src/lib.rs`

```rust
impl ThreadPool {
    --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

        let (sender, receiver) = mpsc::channel();

        let mut workers = Vec::with_capacity(size);

        for id in 0..size {
          1 workers.push(Worker::new(id, receiver));
        }

        ThreadPool { workers, sender }
    }
    --snip--
}

--snip--

impl Worker {
    fn new(id: usize, receiver: mpsc::Receiver<Job>) -> Worker {
        let thread = thread::spawn(|| {
          2 receiver;
        });

        Worker { id, thread }
    }
}
```

Lista 20-17: Pasando el receptor a cada `Worker`

Hemos hecho algunos cambios pequeños y directos: pasamos el receptor a `Worker::new` \[1\], y luego lo usamos dentro de la clausura \[2\].

Cuando intentamos comprobar este código, obtenemos este error:

```bash
$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
error[E0382]: use of moved value: `receiver`
  --> src/lib.rs:26:42
   |
21 |         let (sender, receiver) = mpsc::channel();
   |                      -------- move occurs because `receiver` has type
`std::sync::mpsc::Receiver<Job>`, which does not implement the `Copy` trait
...
26 |             workers.push(Worker::new(id, receiver));
   |                                          ^^^^^^^^ value moved here, in
previous iteration of loop
```

El código está intentando pasar `receptor` a múltiples instancias de `Worker`. Esto no funcionará, como recordarás del Capítulo 16: la implementación de canal que Rust proporciona es de múltiples _productores_, un solo _consumidor_. Esto significa que no podemos simplemente clonar el extremo consumidor del canal para corregir este código. Tampoco queremos enviar un mensaje múltiples veces a múltiples consumidores; queremos una lista de mensajes con múltiples instancias de `Worker` de modo que cada mensaje se procese una vez.

Además, tomar un trabajo de la cola del canal implica mutar el `receptor`, por lo que los subprocesos necesitan una forma segura de compartir y modificar `receptor`; de lo contrario, es posible que obtengamos condiciones de carrera (como se cubre en el Capítulo 16).

Recuerde los punteros inteligentes seguros para subprocesos discutidos en el Capítulo 16: para compartir la propiedad entre múltiples subprocesos y permitir que los subprocesos muten el valor, necesitamos usar `Arc<Mutex<T>>`. El tipo `Arc` permitirá que múltiples instancias de `Worker` posean el receptor, y `Mutex` asegurará que solo un `Worker` obtenga un trabajo del receptor a la vez. La Lista 20-18 muestra los cambios que necesitamos hacer.

Nombre de archivo: `src/lib.rs`

```rust
use std::{
    sync::{mpsc, Arc, Mutex},
    thread,
};
--snip--

impl ThreadPool {
    --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

        let (sender, receiver) = mpsc::channel();

      1 let receiver = Arc::new(Mutex::new(receiver));

        let mut workers = Vec::with_capacity(size);

        for id in 0..size {
            workers.push(
                Worker::new(id, Arc::clone(& 2 receiver))
            );
        }

        ThreadPool { workers, sender }
    }

    --snip--
}

--snip--

impl Worker {
    fn new(
        id: usize,
        receiver: Arc<Mutex<mpsc::Receiver<Job>>>,
    ) -> Worker {
        --snip--
    }
}
```

Lista 20-18: Compartiendo el receptor entre las instancias de `Worker` usando `Arc` y `Mutex`

En `ThreadPool::new`, ponemos el receptor en un `Arc` y un `Mutex` \[1\]. Para cada nuevo `Worker`, clonamos el `Arc` para aumentar el recuento de referencias para que las instancias de `Worker` puedan compartir la propiedad del receptor \[2\].

Con estos cambios, ¡el código se compila! Estamos llegando!
