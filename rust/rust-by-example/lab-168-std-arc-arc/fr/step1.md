# Arc

Lorsque la propriété partagée entre les threads est nécessaire, on peut utiliser `Arc`(Atomiquement Compte de Référence). Cette structure, via l'implémentation de `Clone`, peut créer un pointeur de référence pour l'emplacement d'une valeur dans le tas mémoire tout en augmentant le compteur de référence. Comme elle partage la propriété entre les threads, lorsque le dernier pointeur de référence vers une valeur sort de portée, la variable est supprimée.

```rust
use std::time::Duration;
use std::sync::Arc;
use std::thread;

fn main() {
    // Cette déclaration de variable est où sa valeur est spécifiée.
    let apple = Arc::new("the same apple");

    for _ in 0..10 {
        // Ici, il n'y a pas de spécification de valeur car il s'agit d'un pointeur
        // vers une référence dans le tas mémoire.
        let apple = Arc::clone(&apple);

        thread::spawn(move || {
            // Comme Arc a été utilisé, des threads peuvent être créés en utilisant
            // la valeur allouée à l'emplacement du pointeur de variable Arc.
            println!("{:?}", apple);
        });
    }

    // Assurez-vous que toutes les instances Arc sont imprimées à partir des
    // threads créés.
    thread::sleep(Duration::from_secs(1));
}
```
