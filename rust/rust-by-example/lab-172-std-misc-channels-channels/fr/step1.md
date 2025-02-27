# Canaux

Rust fournit des `canaux` asynchrones pour la communication entre les threads. Les canaux permettent un flux unidirectionnel d'informations entre deux points de terminaison : le `Sender` et le `Receiver`.

```rust
use std::sync::mpsc::{Sender, Receiver};
use std::sync::mpsc;
use std::thread;

static NTHREADS: i32 = 3;

fn main() {
    // Les canaux ont deux points de terminaison : le `Sender<T>` et le `Receiver<T>`,
    // où `T` est le type du message à transférer
    // (l'annotation de type est superflue)
    let (tx, rx): (Sender<i32>, Receiver<i32>) = mpsc::channel();
    let mut children = Vec::new();

    for id in 0..NTHREADS {
        // Le point de terminaison de l'émetteur peut être copié
        let thread_tx = tx.clone();

        // Chaque thread enverra son identifiant via le canal
        let child = thread::spawn(move || {
            // Le thread prend la propriété de `thread_tx`
            // Chaque thread met une message dans la file d'attente du canal
            thread_tx.send(id).unwrap();

            // L'envoi est une opération non bloquante, le thread continuera
            // immédiatement après avoir envoyé son message
            println!("thread {} fini", id);
        });

        children.push(child);
    }

    // Ici, tous les messages sont collectés
    let mut ids = Vec::with_capacity(NTHREADS as usize);
    for _ in 0..NTHREADS {
        // La méthode `recv` sélectionne un message dans le canal
        // `recv` bloquera le thread actuel s'il n'y a pas de messages disponibles
        ids.push(rx.recv());
    }

    // Attendez que les threads terminent tout travail restant
    for child in children {
        child.join().expect("oups! le thread enfant a rencontré une panique");
    }

    // Affichez l'ordre dans lequel les messages ont été envoyés
    println!("{:?}", ids);
}
```
