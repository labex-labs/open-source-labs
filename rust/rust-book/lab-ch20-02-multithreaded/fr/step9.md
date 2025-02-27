# Sending Code from the ThreadPool to a Thread

Nous avons laissé un commentaire dans la boucle `for` du Listing 20-14 concernant la création de threads. Ici, nous allons voir comment nous créons réellement des threads. La bibliothèque standard fournit `thread::spawn` comme moyen de créer des threads, et `thread::spawn` attend de recevoir du code que le thread devrait exécuter dès qu'il est créé. Cependant, dans notre cas, nous voulons créer les threads et les faire _attendre_ du code que nous enverrons plus tard. L'implémentation des threads de la bibliothèque standard ne comprend pas de moyen de le faire ; nous devons l'implémenter manuellement.

Nous allons implémenter ce comportement en introduisant une nouvelle structure de données entre le `ThreadPool` et les threads qui gérera ce nouveau comportement. Nous appellerons cette structure de données _Worker_, qui est un terme courant dans les implémentations de pooling. Le `Worker` prend le code qui doit être exécuté et exécute le code dans son thread.

Imaginez des personnes travaillant dans la cuisine d'un restaurant : les employés attendent jusqu'à ce que des commandes arrivent des clients, puis ils sont responsables de prendre ces commandes et de les exécuter.

Au lieu de stocker un vecteur d'instances de `JoinHandle<()>` dans le thread pool, nous allons stocker des instances de la structure `Worker`. Chaque `Worker` stockera une seule instance de `JoinHandle<()>`. Ensuite, nous implémenterons une méthode sur `Worker` qui prendra une closure de code à exécuter et la transmettra au thread déjà en cours d'exécution pour exécution. Nous donnerons également à chaque `Worker` un `id` pour que nous puissions distinguer entre les différentes instances de `Worker` dans le pool lors de la journalisation ou du débogage.

Voici le nouveau processus qui se produira lorsque nous créerons un `ThreadPool`. Nous implémenterons le code qui envoie la closure au thread après avoir configuré `Worker` de cette manière :

1.  Définir une structure `Worker` qui contient un `id` et un `JoinHandle<()>`.
2.  Modifier `ThreadPool` pour stocker un vecteur d'instances de `Worker`.
3.  Définir une fonction `Worker::new` qui prend un numéro d'`id` et renvoie une instance de `Worker` qui contient l'`id` et un thread lancé avec une closure vide.
4.  Dans `ThreadPool::new`, utiliser le compteur de boucle `for` pour générer un `id`, créer un nouveau `Worker` avec cet `id` et stocker le `Worker` dans le vecteur.

Si vous êtes prêt à relever un défi, essayez d'implémenter ces modifications vous-même avant de regarder le code du Listing 20-15.

Prêt? Voici le Listing 20-15 avec une manière de faire les modifications précédentes.

Nom de fichier : `src/lib.rs`

```rust
use std::thread;

pub struct ThreadPool {
  1 workers: Vec<Worker>,
}

impl ThreadPool {
    --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

        let mut workers = Vec::with_capacity(size);

      2 for id in 0..size {
          3 workers.push(Worker::new(id));
        }

        ThreadPool { workers }
    }
    --snip--
}

4 struct Worker {
    id: usize,
    thread: thread::JoinHandle<()>,
}

impl Worker {
  5 fn new(id: usize) -> Worker {
      6 let thread = thread::spawn(|| {});

        Worker { 7 id, 8 thread }
    }
}
```

Listing 20-15: Modifying `ThreadPool` to hold `Worker` instances instead of holding threads directly

Nous avons changé le nom du champ sur `ThreadPool` de `threads` en `workers` car il stocke désormais des instances de `Worker` au lieu d'instances de `JoinHandle<()>` \[1\]. Nous utilisons le compteur dans la boucle `for` \[2\] comme argument pour `Worker::new`, et nous stockons chaque nouveau `Worker` dans le vecteur nommé `workers` \[3\].

Le code externe (comme notre serveur dans `src/main.rs`) n'a pas besoin de connaître les détails d'implémentation concernant l'utilisation d'une structure `Worker` dans `ThreadPool`, donc nous rendons la structure `Worker` \[4\] et sa fonction `new` \[5\] privées. La fonction `Worker::new` utilise l'`id` que nous lui donnons \[7\] et stocke une instance de `JoinHandle<()>` \[8\] qui est créée en lançant un nouveau thread avec une closure vide \[6\].

> Note: Si le système d'exploitation ne peut pas créer un thread car il n'y a pas assez de ressources système, `thread::spawn` provoquera une panique. Cela fera planter tout notre serveur, même si la création de certains threads peut réussir. Pour simplifier, ce comportement est acceptable, mais dans une implémentation de thread pool en production, vous voudriez probablement utiliser `std::thread::Builder` et sa méthode `spawn` qui renvoie `Result` à la place.

Ce code compilera et stockera le nombre d'instances de `Worker` que nous avons spécifié comme argument pour `ThreadPool::new`. Mais nous _n'avons toujours pas_ traité la closure que nous recevons dans `execute`. Voyons comment faire cela ensuite.
