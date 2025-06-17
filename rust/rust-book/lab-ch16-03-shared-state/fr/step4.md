# Partage d'un Mutex`<T>` entre plusieurs threads

Maintenant, essayons de partager une valeur entre plusieurs threads en utilisant `Mutex<T>`. Nous allons démarrer 10 threads et leur demander chacun d'incrémenter d'un 1 une valeur de compteur, de sorte que le compteur passe de 0 à 10. L'exemple de la liste 16-13 entraînera une erreur de compilation, et nous utiliserons cette erreur pour en apprendre plus sur l'utilisation de `Mutex<T>` et sur la manière dont Rust nous aide à l'utiliser correctement.

Nom de fichier : `src/main.rs`

```rust
use std::sync::Mutex;
use std::thread;

fn main() {
  1 let counter = Mutex::new(0);
    let mut handles = vec![];

  2 for _ in 0..10 {
      3 let handle = thread::spawn(move || {
          4 let mut num = counter.lock().unwrap();

          5 *num += 1;
        });
      6 handles.push(handle);
    }

    for handle in handles {
      7 handle.join().unwrap();
    }

  8 println!("Result: {}", *counter.lock().unwrap());
}
```

Liste 16-13 : Dix threads, chacun incrémentant un compteur protégé par un `Mutex<T>`

Nous créons une variable `counter` pour stocker un `i32` à l'intérieur d'un `Mutex<T>` \[1\], comme nous l'avons fait dans la liste 16-12. Ensuite, nous créons 10 threads en itérant sur une plage de nombres \[2\]. Nous utilisons `thread::spawn` et donnons à tous les threads la même fermeture : une fermeture qui déplace le compteur dans le thread \[3\], acquiert un verrou sur le `Mutex<T>` en appelant la méthode `lock` \[4\], puis ajoute 1 à la valeur dans le mutex \[5\]. Lorsqu'un thread a fini d'exécuter sa fermeture, `num` sortira de portée et libérera le verrou pour que le verrou puisse être acquis par un autre thread.

Dans le thread principal, nous collectons tous les pointeurs d'attente de `join` \[6\]. Ensuite, comme nous l'avons fait dans la liste 16-2, nous appelons `join` sur chaque pointeur pour nous assurer que tous les threads se terminent \[7\]. À ce moment-là, le thread principal acquerra le verrou et affichera le résultat de ce programme \[8\].

Nous avons laissé entendre que cet exemple ne compilerait pas. Maintenant, voyons pourquoi!

```bash
error[E0382]: use of moved value: `counter`
  --> src/main.rs:9:36
   |
5  |     let counter = Mutex::new(0);
   |         ------- move occurs because `counter` has type `Mutex<i32>`, which
does not implement the `Copy` trait
...
9  |         let handle = thread::spawn(move || {
   |                                    ^^^^^^^ value moved into closure here,
in previous iteration of loop
10 |             let mut num = counter.lock().unwrap();
   |                           ------- use occurs due to use in closure
```

Le message d'erreur indique que la valeur `counter` a été déplacée dans l'itération précédente de la boucle. Rust nous dit que nous ne pouvons pas déplacer la propriété du verrou `counter` dans plusieurs threads. Corrigeons l'erreur de compilation avec la méthode de propriété multiple que nous avons discutée au chapitre 15.
