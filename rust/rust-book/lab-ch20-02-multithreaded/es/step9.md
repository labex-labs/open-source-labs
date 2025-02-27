# Enviando código desde ThreadPool a un subproceso

Dejamos un comentario en el bucle `for` de la Lista 20-14 sobre la creación de subprocesos. Aquí, veremos cómo realmente creamos subprocesos. La biblioteca estándar proporciona `thread::spawn` como una forma de crear subprocesos, y `thread::spawn` espera recibir algún código que el subproceso debe ejecutar tan pronto como se crea el subproceso. Sin embargo, en nuestro caso, queremos crear los subprocesos y que _espere_ por el código que enviaremos más tarde. La implementación de subprocesos de la biblioteca estándar no incluye ninguna forma de hacer eso; tenemos que implementarlo manualmente.

Implementaremos este comportamiento introduciendo una nueva estructura de datos entre `ThreadPool` y los subprocesos que gestionará este nuevo comportamiento. Llamaremos a esta estructura de datos _Worker_, que es un término común en las implementaciones de pooling. El `Worker` recoge el código que necesita ser ejecutado y lo ejecuta en su subproceso.

Imagina a las personas que trabajan en la cocina de un restaurante: los trabajadores esperan hasta que lleguen los pedidos de los clientes, y luego son responsables de tomar esos pedidos y atendérselos.

En lugar de almacenar un vector de instancias de `JoinHandle<()>` en el grupo de subprocesos, almacenaremos instancias de la estructura `Worker`. Cada `Worker` almacenará una sola instancia de `JoinHandle<()>`. Luego implementaremos un método en `Worker` que tomará una clausura de código a ejecutar y la enviará al subproceso ya en ejecución para su ejecución. También le daremos a cada `Worker` un `id` para que podamos distinguir entre las diferentes instancias de `Worker` en el grupo cuando registramos o depuramos.

Aquí está el nuevo proceso que sucederá cuando creemos un `ThreadPool`. Implementaremos el código que envía la clausura al subproceso después de tener `Worker` configurado de esta manera:

1.  Definir una estructura `Worker` que contiene un `id` y un `JoinHandle<()>`.
2.  Cambiar `ThreadPool` para contener un vector de instancias de `Worker`.
3.  Definir una función `Worker::new` que toma un número de `id` y devuelve una instancia de `Worker` que contiene el `id` y un subproceso creado con una clausura vacía.
4.  En `ThreadPool::new`, usar el contador del bucle `for` para generar un `id`, crear un nuevo `Worker` con ese `id` y almacenar el `Worker` en el vector.

Si estás dispuesto a un desafío, intenta implementar estos cambios por tu cuenta antes de ver el código de la Lista 20-15.

¿Listo? Aquí está la Lista 20-15 con una forma de hacer las modificaciones anteriores.

Nombre de archivo: `src/lib.rs`

```rust
use std::thread;

pub struct ThreadPool {
  1 workers: Vec<Worker>,
}

impl ThreadPool {
    --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

        let mut workers = Vec::with_capacity(size);

      2 for id in 0..size {
          3 workers.push(Worker::new(id));
        }

        ThreadPool { workers }
    }
    --snip--
}

4 struct Worker {
    id: usize,
    thread: thread::JoinHandle<()>,
}

impl Worker {
  5 fn new(id: usize) -> Worker {
      6 let thread = thread::spawn(|| {});

        Worker { 7 id, 8 thread }
    }
}
```

Lista 20-15: Modificando `ThreadPool` para contener instancias de `Worker` en lugar de contener subprocesos directamente

Hemos cambiado el nombre del campo en `ThreadPool` de `threads` a `workers` porque ahora contiene instancias de `Worker` en lugar de instancias de `JoinHandle<()>` \[1\]. Usamos el contador en el bucle `for` \[2\] como argumento para `Worker::new`, y almacenamos cada nuevo `Worker` en el vector llamado `workers` \[3\].

El código externo (como nuestro servidor en `src/main.rs`) no necesita conocer los detalles de implementación sobre el uso de una estructura `Worker` dentro de `ThreadPool`, así que hacemos que la estructura `Worker` \[4\] y su función `new` \[5\] sean privadas. La función `Worker::new` usa el `id` que le damos \[7\] y almacena una instancia de `JoinHandle<()>` \[8\] que se crea al generar un nuevo subproceso usando una clausura vacía \[6\].

> Nota: Si el sistema operativo no puede crear un subproceso porque no hay suficientes recursos del sistema, `thread::spawn` causará un error. Eso hará que todo nuestro servidor se detenga con un error, aunque la creación de algunos subprocesos puede tener éxito. Por simplicidad, este comportamiento es aceptable, pero en una implementación de grupo de subprocesos en producción, probablemente querrías usar `std::thread::Builder` y su método `spawn` que devuelve `Result` en lugar.

Este código se compilará y almacenará el número de instancias de `Worker` que especificamos como argumento para `ThreadPool::new`. Pero _todavía_ no estamos procesando la clausura que obtenemos en `execute`. Veamos cómo hacerlo a continuación.
