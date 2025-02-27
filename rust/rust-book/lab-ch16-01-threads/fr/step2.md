# Création d'un nouveau thread avec spawn

Pour créer un nouveau thread, nous appelons la fonction `thread::spawn` et lui passons une closure (nous avons parlé des closures au chapitre 13) contenant le code que nous voulons exécuter dans le nouveau thread. L'exemple de la Liste 16-1 affiche du texte dans le thread principal et d'autres textes dans un nouveau thread.

Nom de fichier : `src/main.rs`

```rust
use std::thread;
use std::time::Duration;

fn main() {
    thread::spawn(|| {
        for i in 1..10 {
            println!("hi number {i} from the spawned thread!");
            thread::sleep(Duration::from_millis(1));
        }
    });

    for i in 1..5 {
        println!("hi number {i} from the main thread!");
        thread::sleep(Duration::from_millis(1));
    }
}
```

Liste 16-1 : Création d'un nouveau thread pour afficher une chose tandis que le thread principal affiche autre chose

Notez que lorsque le thread principal d'un programme Rust se termine, tous les threads lancés sont arrêtés, que ce soit s'ils ont fini d'exécuter ou non. La sortie de ce programme peut être un peu différente à chaque exécution, mais elle ressemblera à ceci :

    hi number 1 from the main thread!
    hi number 1 from the spawned thread!
    hi number 2 from the main thread!
    hi number 2 from the spawned thread!
    hi number 3 from the main thread!
    hi number 3 from the spawned thread!
    hi number 4 from the main thread!
    hi number 4 from the spawned thread!
    hi number 5 from the spawned thread!

Les appels à `thread::sleep` forcent un thread à arrêter son exécution pendant une courte durée, permettant à un autre thread de s'exécuter. Les threads prendront probablement la relève, mais cela n'est pas garanti : cela dépend de la façon dont votre système d'exploitation programme les threads. Dans cette exécution, le thread principal a affiché en premier, même si l'instruction d'affichage du thread lancé apparaît en premier dans le code. Et même si nous avons dit au thread lancé d'afficher jusqu'à ce que `i` soit égal à 9, il n'est arrivé qu'à 5 avant que le thread principal ne se termine.

Si vous exécutez ce code et ne voyez que la sortie du thread principal, ou si vous ne voyez pas d'emboîtement, essayez d'augmenter les nombres dans les plages pour créer plus de possibilités pour le système d'exploitation de basculer entre les threads.
