# Hilos

Rust proporciona un mecanismo para crear hilos nativos del sistema operativo a través de la función `spawn`, cuyo argumento es una clausura móvil.

```rust
use std::thread;

const NTHREADS: u32 = 10;

// Este es el hilo `main`
fn main() {
    // Crea un vector para almacenar los hilos hijos que se crean.
    let mut children = vec![];

    for i in 0..NTHREADS {
        // Inicia otro hilo
        children.push(thread::spawn(move || {
            println!("este es el hilo número {}", i);
        }));
    }

    for child in children {
        // Espera a que el hilo termine. Devuelve un resultado.
        let _ = child.join();
    }
}
```

Estos hilos serán programados por el sistema operativo.
