# Threads

Rust fornece um mecanismo para criar threads nativas do sistema operacional por meio da função `spawn`, cujo argumento é um fecho (closure) móvel.

```rust
use std::thread;

const NTHREADS: u32 = 10;

// Esta é a thread principal
fn main() {
    // Crie um vetor para armazenar as threads filhas criadas.
    let mut children = vec![];

    for i in 0..NTHREADS {
        // Inicie outra thread
        children.push(thread::spawn(move || {
            println!("esta é a thread número {}", i);
        }));
    }

    for child in children {
        // Aguarde a conclusão da thread. Retorna um resultado.
        let _ = child.join();
    }
}
```

Essas threads serão agendadas pelo sistema operacional.
