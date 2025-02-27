# Creando espacio para almacenar los subprocesos

Ahora que tenemos una forma de saber que tenemos un número válido de subprocesos para almacenar en el grupo, podemos crear esos subprocesos y almacenarlos en la estructura `ThreadPool` antes de devolver la estructura. Pero, ¿cómo "almacenamos" un subproceso? Echemos otro vistazo a la firma de `thread::spawn`:

```rust
pub fn spawn<F, T>(f: F) -> JoinHandle<T>
    where
        F: FnOnce() -> T,
        F: Send + 'static,
        T: Send + 'static,
```

La función `spawn` devuelve un `JoinHandle<T>`, donde `T` es el tipo que devuelve la clausura. Intentemos usar `JoinHandle` también y ver qué pasa. En nuestro caso, las clausuras que estamos pasando al grupo de subprocesos manejarán la conexión y no devolverán nada, por lo que `T` será el tipo unitario `()`.

El código de la Lista 20-14 se compilará pero aún no creará ningún subproceso. Hemos cambiado la definición de `ThreadPool` para que contenga un vector de instancias de `thread::JoinHandle<()>`, inicializado el vector con una capacidad de `size`, configurado un bucle `for` que ejecutará algún código para crear los subprocesos y devuelto una instancia de `ThreadPool` que los contiene.

Nombre de archivo: `src/lib.rs`

```rust
1 use std::thread;

pub struct ThreadPool {
  2 threads: Vec<thread::JoinHandle<()>>,
}

impl ThreadPool {
    --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

      3 let mut threads = Vec::with_capacity(size);

        for _ in 0..size {
            // create some threads and store them in the vector
        }

        ThreadPool { threads }
    }
    --snip--
}
```

Lista 20-14: Creando un vector para `ThreadPool` para almacenar los subprocesos

Hemos traído `std::thread` al ámbito en el crate de biblioteca \[1\] porque estamos usando `thread::JoinHandle` como el tipo de los elementos en el vector en `ThreadPool` \[2\].

Una vez que se recibe un tamaño válido, nuestro `ThreadPool` crea un nuevo vector que puede contener `size` elementos \[3\]. La función `with_capacity` realiza la misma tarea que `Vec::new` pero con una importante diferencia: reserva espacio previamente en el vector. Debido a que sabemos que necesitamos almacenar `size` elementos en el vector, hacer esta asignación por adelantado es ligeramente más eficiente que usar `Vec::new`, que se redimensiona a sí misma a medida que se insertan elementos.

Cuando vuelva a ejecutar `cargo check`, debería tener éxito.
