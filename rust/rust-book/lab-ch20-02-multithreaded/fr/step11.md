# Implementing the execute Method

Implémentons enfin la méthode `execute` sur `ThreadPool`. Nous changerons également `Job` d'une struct en un alias de type pour un objet de trait qui contient le type de closure que `execute` reçoit. Comme discuté dans "Creating Type Synonyms with Type Aliases", les aliases de type nous permettent de simplifier des types longs pour faciliter leur utilisation. Considérez le Listing 20-19.

Nom de fichier : `src/lib.rs`

```rust
--snip--

type Job = Box<dyn FnOnce() + Send + 'static>;

impl ThreadPool {
    --snip--

    pub fn execute<F>(&self, f: F)
    where
        F: FnOnce() + Send + 'static,
    {
      1 let job = Box::new(f);

      2 self.sender.send(job).unwrap();
    }
}

--snip--
```

Listing 20-19: Creating a `Job` type alias for a `Box` that holds each closure and then sending the job down the channel

Après avoir créé une nouvelle instance de `Job` à l'aide de la closure que nous obtenons dans `execute` \[1\], nous envoyons cette tâche par l'extrémité d'envoi du canal \[2\]. Nous appelons `unwrap` sur `send` pour le cas où l'envoi échoue. Cela peut arriver si, par exemple, nous arrêtons tous nos threads d'exécution, ce qui signifie que l'extrémité de réception a cessé de recevoir de nouveaux messages. En ce moment, nous ne pouvons pas arrêter nos threads d'exécution : nos threads continuent d'exécuter tant que le pool existe. La raison pour laquelle nous utilisons `unwrap` est que nous savons que le cas d'échec ne se produira pas, mais le compilateur ne le sait pas.

Mais nous ne sommes pas tout à fait terminés! Dans le `Worker`, la closure que nous passons à `thread::spawn` ne fait encore que _référencer_ l'extrémité de réception du canal. Au lieu de cela, nous devons que la closure boucle à l'infini, demandant à l'extrémité de réception du canal une tâche et exécutant la tâche lorsqu'elle en reçoit une. Apportons le changement montré dans le Listing 20-20 à `Worker::new`.

Nom de fichier : `src/lib.rs`

```rust
--snip--

impl Worker {
    fn new(
        id: usize,
        receiver: Arc<Mutex<mpsc::Receiver<Job>>>,
    ) -> Worker {
        let thread = thread::spawn(move || loop {
            let job = receiver
              1.lock()
              2.unwrap()
              3.recv()
              4.unwrap();

            println!("Worker {id} got a job; executing.");

            job();
        });

        Worker { id, thread }
    }
}
```

Listing 20-20: Receiving and executing the jobs in the `Worker` instance's thread

Ici, nous appelons d'abord `lock` sur le `receiver` pour acquérir le verrou \[1\], puis nous appelons `unwrap` pour générer une panique en cas d'erreur \[2\]. L'acquisition d'un verrou peut échouer si le verrou est dans un état _empoisonné_, ce qui peut arriver si un autre thread a généré une panique tout en maintenant le verrou au lieu de le libérer. Dans cette situation, appeler `unwrap` pour que ce thread génère une panique est la bonne action à prendre. N'hésitez pas à changer cet `unwrap` en un `expect` avec un message d'erreur qui a du sens pour vous.

Si nous obtenons le verrou sur le verrou, nous appelons `recv` pour recevoir une `Job` du canal \[3\]. Un dernier `unwrap` passe également outre toute erreur ici \[4\], qui peut survenir si le thread possédant l'expéditeur s'est arrêté, de manière similaire à la façon dont la méthode `send` renvoie `Err` si le récepteur s'arrête.

L'appel à `recv` bloque, donc si il n'y a pas de tâche pour le moment, le thread actuel attendra jusqu'à ce qu'une tâche devienne disponible. Le `Mutex<T>` garantit qu'un seul thread `Worker` à la fois essaie de demander une tâche.

Notre thread pool est maintenant en état de fonctionnement! Donnez-lui un `cargo run` et effectuez quelques requêtes :

```bash

```

Succès! Nous avons maintenant un thread pool qui exécute les connexions de manière asynchrone. Il n'y a jamais plus de quatre threads créés, donc notre système ne risque pas d'être surchargé si le serveur reçoit beaucoup de requêtes. Si nous effectuons une requête à _/sleep_, le serveur sera capable de traiter d'autres requêtes en faisant exécuter celles-ci par un autre thread.

> Note: Si vous ouvrez _/sleep_ dans plusieurs fenêtres de navigateur simultanément, elles peuvent charger une par une avec un intervalle de cinq secondes. Certains navigateurs web exécutent plusieurs instances de la même requête séquentiellement pour des raisons de mise en cache. Cette limitation n'est pas causée par notre serveur web.

Après avoir appris sur la boucle `while let` au Chapitre 18, vous vous demandez peut-être pourquoi nous n'avons pas écrit le code du thread `Worker` comme montré dans le Listing 20-21.

Nom de fichier : `src/lib.rs`

```rust
--snip--

impl Worker {
    fn new(
        id: usize,
        receiver: Arc<Mutex<mpsc::Receiver<Job>>>,
    ) -> Worker {
        let thread = thread::spawn(move || {
            while let Ok(job) = receiver.lock().unwrap().recv() {
                println!("Worker {id} got a job; executing.");

                job();
            }
        });

        Worker { id, thread }
    }
}
```

Listing 20-21: An alternative implementation of `Worker::new` using `while let`

Ce code compile et s'exécute mais ne produit pas le comportement de threading souhaité : une requête lente fera toujours attendre les autres requêtes à être traitées. La raison est un peu subtile : la struct `Mutex` n'a pas de méthode publique `unlock` car la propriété du verrou est basée sur la durée de vie du `MutexGuard<T>` dans le `LockResult<MutexGuard<T>>` que la méthode `lock` renvoie. Au moment de la compilation, le vérificateur d'emprunt peut donc appliquer la règle selon laquelle une ressource protégée par un `Mutex` ne peut pas être accédée à moins que nous ne tenions le verrou. Cependant, cette implémentation peut également entraîner le verrou étant maintenu plus longtemps que prévu si nous ne sommes pas attentifs à la durée de vie du `MutexGuard<T>`.

Le code du Listing 20-20 qui utilise `let job = receiver.lock().unwrap().recv().unwrap();` fonctionne car avec `let`, toutes les valeurs temporaires utilisées dans l'expression du côté droit de l'égalité sont immédiatement supprimées lorsque l'instruction `let` se termine. Cependant, `while let` (et `if let` et `match`) ne supprime pas les valeurs temporaires jusqu'à la fin du bloc associé. Dans le Listing 20-21, le verrou reste maintenu pendant la durée de l'appel à `job()`, ce qui signifie que d'autres instances de `Worker` ne peuvent pas recevoir de tâches.
