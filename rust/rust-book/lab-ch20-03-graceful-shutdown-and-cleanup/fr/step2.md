# Implémentation du trait Drop sur ThreadPool

Commenceons par implémenter `Drop` sur notre pool de threads. Lorsque le pool est supprimé, tous nos threads devraient tous rejoindre pour s'assurer qu'ils terminent leur travail. La liste 20-22 montre une première tentative d'implémentation de `Drop`; ce code ne fonctionnera pas encore.

Nom de fichier : `src/lib.rs`

```rust
impl Drop for ThreadPool {
    fn drop(&mut self) {
      1 for worker in &mut self.workers {
          2 println!("Shutting down worker {}", worker.id);

          3 worker.thread.join().unwrap();
        }
    }
}
```

Liste 20-22 : Joindre chaque thread lorsque le pool de threads sort de portée

Tout d'abord, nous parcourons chacun des `workers` du pool de threads \[1\]. Nous utilisons `&mut` pour cela car `self` est une référence mutable, et nous devons également être en mesure de modifier `worker`. Pour chaque `worker`, nous affichons un message indiquant que cette instance particulière de `Worker` est en train de se fermer \[2\], puis nous appelons `join` sur le thread de cette instance de `Worker` \[3\]. Si l'appel à `join` échoue, nous utilisons `unwrap` pour forcer Rust à générer une panique et passer à une fermeture non propre.

Voici l'erreur que nous obtenons lorsque nous compilons ce code :

```bash
error[E0507]: cannot move out of `worker.thread` which is behind a mutable
reference
    --> src/lib.rs:52:13
     |
52   |             worker.thread.join().unwrap();
     |             ^^^^^^^^^^^^^ ------ `worker.thread` moved due to this
method call
     |             |
     |             move occurs because `worker.thread` has type
`JoinHandle<()>`, which does not implement the `Copy` trait
     |
note: this function takes ownership of the receiver `self`, which moves
`worker.thread`
```

L'erreur nous indique que nous ne pouvons pas appeler `join` car nous n'avons qu'un emprunt mutable de chaque `worker` et que `join` prend la propriété de son argument. Pour résoudre ce problème, nous devons déplacer le thread hors de l'instance de `Worker` qui possède `thread` afin que `join` puisse consommer le thread. Nous l'avons fait dans la liste 17-15 : si `Worker` contient une `Option<thread::JoinHandle<()>>` au lieu de cela, nous pouvons appeler la méthode `take` sur l'`Option` pour déplacer la valeur hors de la variante `Some` et laisser une variante `None` à sa place. En d'autres termes, un `Worker` qui est en cours d'exécution aura une variante `Some` dans `thread`, et lorsque nous voulons nettoyer un `Worker`, nous remplaçons `Some` par `None` de sorte que le `Worker` n'ait plus de thread à exécuter.

Donc, nous savons que nous voulons mettre à jour la définition de `Worker` comme ceci :

Nom de fichier : `src/lib.rs`

```rust
struct Worker {
    id: usize,
    thread: Option<thread::JoinHandle<()>>,
}
```

Maintenant, laissons le compilateur trouver les autres endroits qui doivent être modifiés. En vérifiant ce code, nous obtenons deux erreurs :

```bash
error[E0599]: no method named `join` found for enum `Option` in the current
scope
  --> src/lib.rs:52:27
   |
52 |             worker.thread.join().unwrap();
   |                           ^^^^ method not found in
`Option<JoinHandle<()>>`

error[E0308]: mismatched types
  --> src/lib.rs:72:22
   |
72 |         Worker { id, thread }
   |                      ^^^^^^ expected enum `Option`, found struct
`JoinHandle`
   |
   = note: expected enum `Option<JoinHandle<()>>`
            found struct `JoinHandle<_>`
help: try wrapping the expression in `Some`
   |
72 |         Worker { id, thread: Some(thread) }
   |                      +++++++++++++      +
```

Traitons la seconde erreur, qui pointe vers le code à la fin de `Worker::new` ; nous devons envelopper la valeur `thread` dans `Some` lorsque nous créons un nouveau `Worker`. Apportez les modifications suivantes pour corriger cette erreur :

Nom de fichier : `src/lib.rs`

```rust
impl Worker {
    fn new(
        id: usize,
        receiver: Arc<Mutex<mpsc::Receiver<Job>>>,
    ) -> Worker {
        --snip--

        Worker {
            id,
            thread: Some(thread),
        }
    }
}
```

La première erreur se trouve dans notre implémentation de `Drop`. Nous avons mentionné précédemment que nous avions l'intention d'appeler `take` sur la valeur `Option` pour déplacer `thread` hors de `worker`. Les modifications suivantes le feront :

Nom de fichier : `src/lib.rs`

```rust
impl Drop for ThreadPool {
    fn drop(&mut self) {
        for worker in &mut self.workers {
            println!("Shutting down worker {}", worker.id);

          1 if let Some(thread) = worker.thread.take() {
              2 thread.join().unwrap();
            }
        }
    }
}
```

Comme discuté au chapitre 17, la méthode `take` sur `Option` extrait la variante `Some` et laisse `None` à sa place. Nous utilisons `if let` pour déstructurer la `Some` et obtenir le thread \[1\] ; puis nous appelons `join` sur le thread \[2\]. Si le thread d'une instance de `Worker` est déjà `None`, nous savons que le `Worker` a déjà eu son thread nettoyé, donc rien ne se passe dans ce cas.
