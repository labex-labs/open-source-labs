# Threads

Rust fournit un mécanisme pour créer des threads natifs du système d'exploitation via la fonction `spawn`, l'argument de cette fonction est une closure mobile.

```rust
use std::thread;

const NTHREADS: u32 = 10;

// Ceci est le thread `main`
fn main() {
    // Crée un vecteur pour stocker les threads enfants créés.
    let mut children = vec![];

    for i in 0..NTHREADS {
        // Lance un autre thread
        children.push(thread::spawn(move || {
            println!("ceci est le thread numéro {}", i);
        }));
    }

    for child in children {
        // Attend que le thread se termine. Renvoie un résultat.
        let _ = child.join();
    }
}
```

Ces threads seront planifiés par le système d'exploitation.
