# Sending Requests to Threads via Channels

Le prochain problème que nous allons résoudre est que les closures données à `thread::spawn` ne font absolument rien. Actuellement, nous obtenons la closure que nous voulons exécuter dans la méthode `execute`. Mais nous devons donner à `thread::spawn` une closure à exécuter lorsque nous créons chaque `Worker` lors de la création du `ThreadPool`.

Nous voulons que les structs `Worker` que nous venons de créer récupèrent le code à exécuter dans une file d'attente contenue dans le `ThreadPool` et envoient ce code à son thread pour exécution.

Les canaux dont nous avons parlé au Chapitre 16 - une manière simple de communiquer entre deux threads - seraient parfait pour ce cas d'utilisation. Nous utiliserons un canal pour fonctionner comme une file d'attente de tâches, et `execute` enverra une tâche du `ThreadPool` aux instances de `Worker`, qui enverront la tâche à son thread. Voici le plan :

1.  Le `ThreadPool` créera un canal et gardera le sender.
2.  Chaque `Worker` gardera le receiver.
3.  Nous créerons une nouvelle struct `Job` qui contiendra les closures que nous voulons envoyer par le canal.
4.  La méthode `execute` enverra la tâche qu'elle veut exécuter via le sender.
5.  Dans son thread, le `Worker` bouclera sur son receiver et exécutera les closures de toutes les tâches qu'il reçoit.

Commencons par créer un canal dans `ThreadPool::new` et en garder le sender dans l'instance de `ThreadPool`, comme montré dans le Listing 20-16. La struct `Job` ne contient rien pour le moment mais sera le type d'élément que nous envoyons par le canal.

Nom de fichier : `src/lib.rs`

```rust
use std::{sync::mpsc, thread};

pub struct ThreadPool {
    workers: Vec<Worker>,
    sender: mpsc::Sender<Job>,
}

struct Job;

impl ThreadPool {
    --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

      1 let (sender, receiver) = mpsc::channel();

        let mut workers = Vec::with_capacity(size);

        for id in 0..size {
            workers.push(Worker::new(id));
        }

        ThreadPool { workers, 2 sender }
    }
    --snip--
}
```

Listing 20-16: Modifying `ThreadPool` to store the sender of a channel that transmits `Job` instances

Dans `ThreadPool::new`, nous créons notre nouveau canal \[1\] et le pool garde le sender \[2\]. Cela compilera avec succès.

Essayons de passer un receiver du canal à chaque `Worker` lorsque le thread pool crée le canal. Nous savons que nous voulons utiliser le receiver dans le thread que les instances de `Worker` lancent, donc nous ferons référence au paramètre `receiver` dans la closure. Le code du Listing 20-17 ne compilera pas encore tout à fait.

Nom de fichier : `src/lib.rs`

```rust
impl ThreadPool {
    --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

        let (sender, receiver) = mpsc::channel();

        let mut workers = Vec::with_capacity(size);

        for id in 0..size {
          1 workers.push(Worker::new(id, receiver));
        }

        ThreadPool { workers, sender }
    }
    --snip--
}

--snip--

impl Worker {
    fn new(id: usize, receiver: mpsc::Receiver<Job>) -> Worker {
        let thread = thread::spawn(|| {
          2 receiver;
        });

        Worker { id, thread }
    }
}
```

Listing 20-17: Passing the receiver to each `Worker`

Nous avons apporté quelques modifications petites et simples : nous passons le receiver à `Worker::new` \[1\], puis nous l'utilisons à l'intérieur de la closure \[2\].

Lorsque nous essayons de vérifier ce code, nous obtenons cette erreur :

```bash
$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
error[E0382]: use of moved value: `receiver`
  --> src/lib.rs:26:42
   |
21 |         let (sender, receiver) = mpsc::channel();
   |                      -------- move occurs because `receiver` has type
`std::sync::mpsc::Receiver<Job>`, which does not implement the `Copy` trait
...
26 |             workers.push(Worker::new(id, receiver));
   |                                          ^^^^^^^^ value moved here, in
previous iteration of loop
```

Le code essaie de passer `receiver` à plusieurs instances de `Worker`. Cela ne fonctionnera pas, comme vous le rappellerez du Chapitre 16 : l'implémentation de canal que Rust fournit est multiple _producteur_, unique _consommateur_. Cela signifie que nous ne pouvons pas simplement cloner l'extrémité consommateur du canal pour corriger ce code. Nous ne voulons également pas envoyer un message plusieurs fois à plusieurs consommateurs ; nous voulons une liste de messages avec plusieurs instances de `Worker` de sorte que chaque message soit traité une fois.

De plus, prendre une tâche dans la file d'attente du canal implique de modifier le `receiver`, donc les threads ont besoin d'un moyen sûr de partager et de modifier `receiver` ; sinon, nous risquons d'avoir des conditions de course (comme décrit au Chapitre 16).

Rappelez-vous les pointeurs intelligents sécurisés pour les threads discutés au Chapitre 16 : pour partager la propriété entre plusieurs threads et permettre aux threads de modifier la valeur, nous devons utiliser `Arc<Mutex<T>>`. Le type `Arc` permettra à plusieurs instances de `Worker` d'avoir la propriété du receiver, et `Mutex` assurera qu'un seul `Worker` obtienne une tâche du receiver à la fois. Le Listing 20-18 montre les modifications que nous devons apporter.

Nom de fichier : `src/lib.rs`

```rust
use std::{
    sync::{mpsc, Arc, Mutex},
    thread,
};
--snip--

impl ThreadPool {
    --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

        let (sender, receiver) = mpsc::channel();

      1 let receiver = Arc::new(Mutex::new(receiver));

        let mut workers = Vec::with_capacity(size);

        for id in 0..size {
            workers.push(
                Worker::new(id, Arc::clone(& 2 receiver))
            );
        }

        ThreadPool { workers, sender }
    }

    --snip--
}

--snip--

impl Worker {
    fn new(
        id: usize,
        receiver: Arc<Mutex<mpsc::Receiver<Job>>>,
    ) -> Worker {
        --snip--
    }
}
```

Listing 20-18: Sharing the receiver among the `Worker` instances using `Arc` and `Mutex`

Dans `ThreadPool::new`, nous mettons le receiver dans un `Arc` et un `Mutex` \[1\]. Pour chaque nouveau `Worker`, nous clonons l'`Arc` pour augmenter le compte de référence de sorte que les instances de `Worker` puissent partager la propriété du receiver \[2\].

Avec ces modifications, le code compile! Nous y arrivons!
