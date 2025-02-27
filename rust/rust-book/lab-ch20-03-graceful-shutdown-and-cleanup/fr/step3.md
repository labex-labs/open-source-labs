# Signaler aux threads de cesser d'écouter les jobs

Avec toutes les modifications que nous avons apportées, notre code se compile sans avertissements. Cependant, le mauvais news est que ce code ne fonctionne pas comme nous le souhaitons encore. La clé est la logique dans les closures exécutées par les threads des instances de `Worker` : pour l'instant, nous appelons `join`, mais cela ne fermera pas les threads, car ils `bouclent` à l'infini à la recherche de jobs. Si nous essayons de supprimer notre `ThreadPool` avec notre implémentation actuelle de `drop`, le thread principal bloquera à l'infini, en attendant que le premier thread termine.

Pour résoudre ce problème, nous devrons apporter une modification à l'implémentation de `drop` de `ThreadPool` puis une modification à la boucle de `Worker`.

Tout d'abord, nous modifierons l'implémentation de `drop` de `ThreadPool` pour supprimer explicitement le `sender` avant d'attendre que les threads se terminent. La liste 20-23 montre les modifications apportées à `ThreadPool` pour supprimer explicitement `sender`. Nous utilisons la même technique `Option` et `take` que celle que nous avons utilisée avec le thread pour pouvoir déplacer `sender` hors de `ThreadPool`.

Nom de fichier : `src/lib.rs`

```rust
pub struct ThreadPool {
    workers: Vec<Worker>,
    sender: Option<mpsc::Sender<Job>>,
}
--snip--
impl ThreadPool {
    pub fn new(size: usize) -> ThreadPool {
        --snip--

        ThreadPool {
            workers,
            sender: Some(sender),
        }
    }

    pub fn execute<F>(&self, f: F)
    where
        F: FnOnce() + Send + 'static,
    {
        let job = Box::new(f);

        self.sender
           .as_ref()
           .unwrap()
           .send(job)
           .unwrap();
    }
}

impl Drop for ThreadPool {
    fn drop(&mut self) {
      1 drop(self.sender.take());

        for worker in &mut self.workers {
            println!("Shutting down worker {}", worker.id);

            if let Some(thread) = worker.thread.take() {
                thread.join().unwrap();
            }
        }
    }
}
```

Liste 20-23 : Suppression explicite de `sender` avant de rejoindre les threads de `Worker`

Supprimer `sender` \[1\] ferme le canal, ce qui indique qu'aucun message ne sera envoyé plus. Lorsque cela se produit, toutes les appels à `recv` que les instances de `Worker` effectuent dans la boucle infinie retourneront une erreur. Dans la liste 20-24, nous changeons la boucle de `Worker` pour sortir de la boucle de manière propre dans ce cas, ce qui signifie que les threads se termineront lorsque l'implémentation de `drop` de `ThreadPool` appellera `join` sur eux.

Nom de fichier : `src/lib.rs`

```rust
impl Worker {
    fn new(
        id: usize,
        receiver: Arc<Mutex<mpsc::Receiver<Job>>>,
    ) -> Worker {
        let thread = thread::spawn(move || loop {
            let message = receiver.lock().unwrap().recv();

            match message {
                Ok(job) => {
                    println!(
                        "Worker {id} got a job; executing."
                    );

                    job();
                }
                Err(_) => {
                    println!(
                        "Worker {id} shutting down."
                    );
                    break;
                }
            }
        });

        Worker {
            id,
            thread: Some(thread),
        }
    }
}
```

Liste 20-24 : Sortir explicitement de la boucle lorsque `recv` renvoie une erreur

Pour voir ce code en action, modifions `main` pour accepter seulement deux requêtes avant de fermer proprement le serveur, comme montré dans la liste 20-25.

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();
    let pool = ThreadPool::new(4);

    for stream in listener.incoming().take(2) {
        let stream = stream.unwrap();

        pool.execute(|| {
            handle_connection(stream);
        });
    }

    println!("Shutting down.");
}
```

Liste 20-25 : Arrêter le serveur après avoir traité deux requêtes en sortant de la boucle

Vous ne voudriez pas qu'un serveur web du monde réel se ferme après avoir traité seulement deux requêtes. Ce code montre simplement que l'arrêt propre et le nettoyage fonctionnent correctement.

La méthode `take` est définie dans le trait `Iterator` et limite l'itération aux deux premiers éléments au plus. Le `ThreadPool` sortira de portée à la fin de `main`, et l'implémentation de `drop` s'exécutera.

Démarrez le serveur avec `cargo run` et effectuez trois requêtes. La troisième requête devrait générer une erreur, et dans votre terminal, vous devriez voir une sortie similaire à celle-ci :

```bash
$ cargo run
   Compiling hello v0.1.0 (file:///projects/hello)
    Finished dev [unoptimized + debuginfo] target(s) in 1.0s
     Running `target/debug/hello`
Worker 0 got a job; executing.
Shutting down.
Shutting down worker 0
Worker 3 got a job; executing.
Worker 1 disconnected; shutting down.
Worker 2 disconnected; shutting down.
Worker 3 disconnected; shutting down.
Worker 0 disconnected; shutting down.
Shutting down worker 1
Shutting down worker 2
Shutting down worker 3
```

Vous pouvez voir un ordre différent d'IDs de `Worker` et de messages affichés. Nous pouvons voir comment ce code fonctionne à partir des messages : les instances de `Worker` 0 et 3 ont reçu les deux premières requêtes. Le serveur a cessé d'accepter des connexions après la deuxième connexion, et l'implémentation de `Drop` sur `ThreadPool` commence à s'exécuter avant même que `Worker` 3 n'ait commencé son job. Supprimer le `sender` déconnecte toutes les instances de `Worker` et leur indique de se fermer. Les instances de `Worker` affichent chacun un message lorsqu'elles se déconnectent, puis le pool de threads appelle `join` pour attendre que chaque thread de `Worker` se termine.

Remarquez un aspect intéressant de cette exécution particulière : le `ThreadPool` a supprimé le `sender`, et avant que tout `Worker` n'ait reçu une erreur, nous avons essayé de rejoindre `Worker` 0. `Worker` 0 n'avait pas encore reçu d'erreur de `recv`, donc le thread principal a bloqué, en attendant que `Worker` 0 se termine. Pendant ce temps, `Worker` 3 a reçu un job puis tous les threads ont reçu une erreur. Lorsque `Worker` 0 a terminé, le thread principal a attendu que le reste des instances de `Worker` se terminent. À ce moment-là, elles étaient toutes sorties de leur boucle et étaient arrêtées.

Félicitations! Nous avons maintenant terminé notre projet ; nous avons un serveur web de base qui utilise un pool de threads pour répondre de manière asynchrone. Nous sommes capables d'effectuer un arrêt propre du serveur, qui nettoie tous les threads du pool. Consultez *https://www.nostarch.com/Rust2021* pour télécharger le code complet de ce chapitre à des fins de référence.

Nous pourrions faire plus ici! Si vous voulez continuer à améliorer ce projet, voici quelques idées :

- Ajoutez plus de documentation à `ThreadPool` et à ses méthodes publiques.
- Ajoutez des tests de la fonctionnalité de la bibliothèque.
- Changez les appels à `unwrap` pour un traitement d'erreur plus robuste.
- Utilisez `ThreadPool` pour effectuer une tâche autre que le traitement de requêtes web.
- Trouvez une boîte à outils de pool de threads sur *https://crates.io* et implémentez un serveur web similaire en utilisant la boîte à outils à la place. Ensuite, comparez son API et sa robustesse avec le pool de threads que nous avons implémenté.
