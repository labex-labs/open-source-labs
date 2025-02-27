# Creating Space to Store the Threads

Maintenant que nous avons un moyen de savoir que nous avons un nombre valide de threads à stocker dans le pool, nous pouvons créer ces threads et les stocker dans la structure `ThreadPool` avant de renvoyer la structure. Mais comment "stockons-nous" un thread? Regardons à nouveau la signature de `thread::spawn` :

```rust
pub fn spawn<F, T>(f: F) -> JoinHandle<T>
    where
        F: FnOnce() -> T,
        F: Send + 'static,
        T: Send + 'static,
```

La fonction `spawn` renvoie un `JoinHandle<T>`, où `T` est le type que la closure renvoie. Essayons d'utiliser `JoinHandle` également et voyons ce qui se passe. Dans notre cas, les closures que nous passons au thread pool géreront la connexion et ne renverront rien, donc `T` sera le type unité `()`.

Le code du Listing 20-14 compilera mais ne créera pas encore de threads. Nous avons changé la définition de `ThreadPool` pour stocker un vecteur d'instances de `thread::JoinHandle<()>`, initialisé le vecteur avec une capacité de `size`, configuré une boucle `for` qui exécutera du code pour créer les threads et renvoyé une instance de `ThreadPool` les contenant.

Nom de fichier : `src/lib.rs`

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
            // créer quelques threads et les stocker dans le vecteur
        }

        ThreadPool { threads }
    }
    --snip--
}
```

Listing 20-14 : Création d'un vecteur pour `ThreadPool` pour stocker les threads

Nous avons porté `std::thread` dans la portée dans le crate bibliothèque \[1\] car nous utilisons `thread::JoinHandle` comme type des éléments dans le vecteur de `ThreadPool` \[2\].

Une fois une taille valide reçue, notre `ThreadPool` crée un nouveau vecteur qui peut stocker `size` éléments \[3\]. La fonction `with_capacity` effectue la même tâche que `Vec::new` mais avec une différence importante : elle réserve de l'espace dans le vecteur à l'avance. Comme nous savons que nous devons stocker `size` éléments dans le vecteur, effectuer cette allocation d'avance est légèrement plus efficace que d'utiliser `Vec::new`, qui redimensionne lui-même lorsqu'éléments sont insérés.

Lorsque vous exécutez `cargo check` à nouveau, cela devrait réussir.
