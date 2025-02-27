# Creación de un número finito de subprocesos

Queremos que nuestro grupo de subprocesos funcione de manera similar y familiar, de modo que cambiar de subprocesos a un grupo de subprocesos no requiera grandes cambios en el código que utiliza nuestra API. La Lista 20-12 muestra la interfaz hipotética para una estructura `ThreadPool` que queremos usar en lugar de `thread::spawn`.

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();
  1 let pool = ThreadPool::new(4);

    for stream in listener.incoming() {
        let stream = stream.unwrap();

      2 pool.execute(|| {
            handle_connection(stream);
        });
    }
}
```

Lista 20-12: Nuestra interfaz ideal de `ThreadPool`

Usamos `ThreadPool::new` para crear un nuevo grupo de subprocesos con un número configurable de subprocesos, en este caso cuatro \[1\]. Luego, en el bucle `for`, `pool.execute` tiene una interfaz similar a `thread::spawn` en el sentido de que toma una clausura que el grupo debe ejecutar para cada flujo \[2\]. Necesitamos implementar `pool.execute` de modo que tome la clausura y la deje ejecutar por un subproceso en el grupo. Este código aún no se compilará, pero lo intentaremos para que el compilador nos pueda guiar en cómo corregirlo.
