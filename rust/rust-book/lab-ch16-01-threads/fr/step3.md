# Attendre que tous les threads se terminent en utilisant des join handles

Le code de la Liste 16-1 arrête non seulement le thread lancé prématurément la plupart du temps en raison de la fin du thread principal, mais également, puisque l'ordre d'exécution des threads n'est pas garanti, nous ne pouvons pas non plus garantir que le thread lancé va même s'exécuter du tout!

Nous pouvons résoudre le problème du non-exécution ou de la terminaison prématurée du thread lancé en enregistrant la valeur de retour de `thread::spawn` dans une variable. Le type de retour de `thread::spawn` est `JoinHandle<T>`. Un `JoinHandle<T>` est une valeur propriétaire qui, lorsqu'on appelle la méthode `join` dessus, attendra que son thread se termine. La Liste 16-2 montre comment utiliser le `JoinHandle<T>` du thread que nous avons créé dans la Liste 16-1 et appeler `join` pour vous assurer que le thread lancé se termine avant que `main` ne sorte.

Nom de fichier : `src/main.rs`

```rust
use std::thread;
use std::time::Duration;

fn main() {
    let handle = thread::spawn(|| {
        for i in 1..10 {
            println!("hi number {i} from the spawned thread!");
            thread::sleep(Duration::from_millis(1));
        }
    });

    for i in 1..5 {
        println!("hi number {i} from the main thread!");
        thread::sleep(Duration::from_millis(1));
    }

    handle.join().unwrap();
}
```

Liste 16-2 : Enregistrer un `JoinHandle<T>` de `thread::spawn` pour garantir que le thread est exécuté jusqu'à la fin

Appeler `join` sur le handle bloque le thread actuellement en cours d'exécution jusqu'à ce que le thread représenté par le handle se termine. _Bloquer_ un thread signifie que ce thread est empêché de travailler ou de sortir. Comme nous avons placé l'appel à `join` après la boucle `for` du thread principal, exécuter la Liste 16-2 devrait produire une sortie similaire à celle-ci :

    hi number 1 from the main thread!
    hi number 2 from the main thread!
    hi number 1 from the spawned thread!
    hi number 3 from the main thread!
    hi number 2 from the spawned thread!
    hi number 4 from the main thread!
    hi number 3 from the spawned thread!
    hi number 4 from the spawned thread!
    hi number 5 from the spawned thread!
    hi number 6 from the spawned thread!
    hi number 7 from the spawned thread!
    hi number 8 from the spawned thread!
    hi number 9 from the spawned thread!

Les deux threads continuent de s'alterner, mais le thread principal attend en raison de l'appel à `handle.join()` et ne se termine pas avant que le thread lancé ne soit terminé.

Mais voyons ce qui se passe lorsque nous plaçons `handle.join()` avant la boucle `for` dans `main`, comme ceci :

Nom de fichier : `src/main.rs`

```rust
use std::thread;
use std::time::Duration;

fn main() {
    let handle = thread::spawn(|| {
        for i in 1..10 {
            println!("hi number {i} from the spawned thread!");
            thread::sleep(Duration::from_millis(1));
        }
    });

    handle.join().unwrap();

    for i in 1..5 {
        println!("hi number {i} from the main thread!");
        thread::sleep(Duration::from_millis(1));
    }
}
```

Le thread principal attendra que le thread lancé se termine puis exécutera sa boucle `for`, de sorte que la sortie ne sera plus intercalée, comme le montre ici :

    hi number 1 from the spawned thread!
    hi number 2 from the spawned thread!
    hi number 3 from the spawned thread!
    hi number 4 from the spawned thread!
    hi number 5 from the spawned thread!
    hi number 6 from the spawned thread!
    hi number 7 from the spawned thread!
    hi number 8 from the spawned thread!
    hi number 9 from the spawned thread!
    hi number 1 from the main thread!
    hi number 2 from the main thread!
    hi number 3 from the main thread!
    hi number 4 from the main thread!

De petits détails, comme le lieu où `join` est appelé, peuvent affecter si vos threads s'exécutent en même temps ou non.
