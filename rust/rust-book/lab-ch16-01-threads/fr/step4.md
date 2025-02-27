# Utiliser des closures move avec des threads

Nous utiliserons souvent le mot-clé `move` avec les closures passées à `thread::spawn` car la closure prendra alors la propriété des valeurs qu'elle utilise de l'environnement, transférant ainsi la propriété de ces valeurs d'un thread à l'autre. Dans "Capturer l'environnement avec les closures", nous avons discuté de `move` dans le contexte des closures. Maintenant, nous nous concentrerons plus sur l'interaction entre `move` et `thread::spawn`.

Remarquez dans la Liste 16-1 que la closure que nous passons à `thread::spawn` ne prend aucun argument : nous n'utilisons aucune donnée du thread principal dans le code du thread lancé. Pour utiliser des données du thread principal dans le thread lancé, la closure du thread lancé doit capturer les valeurs dont elle a besoin. La Liste 16-3 montre une tentative de créer un vecteur dans le thread principal et de l'utiliser dans le thread lancé. Cependant, cela ne fonctionnera pas encore, comme vous le verrez tout de suite.

Nom de fichier : `src/main.rs`

```rust
use std::thread;

fn main() {
    let v = vec![1, 2, 3];

    let handle = thread::spawn(|| {
        println!("Here's a vector: {:?}", v);
    });

    handle.join().unwrap();
}
```

Liste 16-3 : Tentative d'utiliser un vecteur créé par le thread principal dans un autre thread

La closure utilise `v`, donc elle capturera `v` et le fera faire partie de l'environnement de la closure. Comme `thread::spawn` exécute cette closure dans un nouveau thread, nous devrions être en mesure d'accéder à `v` à l'intérieur de ce nouveau thread. Mais lorsque nous compilons cet exemple, nous obtenons l'erreur suivante :

```bash
error[E0373]: closure may outlive the current function, but it borrows `v`,
which is owned by the current function
 --> src/main.rs:6:32
  |
6 |     let handle = thread::spawn(|| {
  |                                ^^ may outlive borrowed value `v`
7 |         println!("Here's a vector: {:?}", v);
  |                                           - `v` is borrowed here
  |
note: function requires argument type to outlive `'static`
 --> src/main.rs:6:18
  |
6 |       let handle = thread::spawn(|| {
  |  __________________^
7 | |         println!("Here's a vector: {:?}", v);
8 | |     });
  | |______^
help: to force the closure to take ownership of `v` (and any other referenced
variables), use the `move` keyword
  |
6 |     let handle = thread::spawn(move || {
  |                                ++++
```

Rust _déduit_ comment capturer `v`, et puisque `println!` a besoin seulement d'une référence à `v`, la closure essaie de prêter `v`. Cependant, il y a un problème : Rust ne peut pas savoir combien de temps le thread lancé va exécuter, donc il ne sait pas si la référence à `v` sera toujours valide.

La Liste 16-4 fournit un scénario où il est plus probable d'avoir une référence à `v` qui ne sera pas valide.

Nom de fichier : `src/main.rs`

```rust
use std::thread;

fn main() {
    let v = vec![1, 2, 3];

    let handle = thread::spawn(|| {
        println!("Here's a vector: {:?}", v);
    });

    drop(v); // oh no!

    handle.join().unwrap();
}
```

Liste 16-4 : Un thread avec une closure qui tente de capturer une référence à `v` d'un thread principal qui supprime `v`

Si Rust nous autorisait à exécuter ce code, il y aurait une possibilité que le thread lancé soit immédiatement mis en arrière-plan sans s'exécuter du tout. Le thread lancé a une référence à `v` à l'intérieur, mais le thread principal supprime immédiatement `v`, en utilisant la fonction `drop` dont nous avons parlé au chapitre 15. Ensuite, lorsque le thread lancé commence à s'exécuter, `v` n'est plus valide, donc une référence à elle n'est pas non plus valide. Oh non!

Pour corriger l'erreur du compilateur dans la Liste 16-3, nous pouvons suivre l'avis du message d'erreur :

    help: to force the closure to take ownership of `v` (and any other referenced
    variables), use the `move` keyword
      |
    6 |     let handle = thread::spawn(move || {
      |                                ++++

En ajoutant le mot-clé `move` avant la closure, nous forçons la closure à prendre la propriété des valeurs qu'elle utilise plutôt que de laisser Rust déduire qu'elle devrait prêter les valeurs. La modification de la Liste 16-3 montrée dans la Liste 16-5 compilera et s'exécutera comme nous le souhaitons.

Nom de fichier : `src/main.rs`

```rust
use std::thread;

fn main() {
    let v = vec![1, 2, 3];

    let handle = thread::spawn(move || {
        println!("Here's a vector: {:?}", v);
    });

    handle.join().unwrap();
}
```

Liste 16-5 : Utilisation du mot-clé `move` pour forcer une closure à prendre la propriété des valeurs qu'elle utilise

Nous serions tentés d'essayer la même chose pour corriger le code de la Liste 16-4 où le thread principal appelait `drop` en utilisant une closure `move`. Cependant, ce remède ne fonctionnera pas car ce que la Liste 16-4 essaye de faire est interdit pour une raison différente. Si nous ajoutions `move` à la closure, nous déplacerions `v` dans l'environnement de la closure, et nous ne pourrions plus appeler `drop` dessus dans le thread principal. Nous obtiendrions cette erreur du compilateur à la place :

```bash
error[E0382]: use of moved value: `v`
  --> src/main.rs:10:10
   |
4  |     let v = vec![1, 2, 3];
   |         - move occurs because `v` has type `Vec<i32>`, which does not
implement the `Copy` trait
5  |
6  |     let handle = thread::spawn(move || {
   |                                ------- value moved into closure here
7  |         println!("Here's a vector: {:?}", v);
   |                                           - variable moved due to use in
closure
...
10 |     drop(v); // oh no!
   |          ^ value used here after move
```

Les règles d'appartenance de Rust nous ont sauvé encore! Nous avons eu une erreur avec le code de la Liste 16-3 parce que Rust était prudent et prêtait seulement `v` au thread, ce qui signifiait que le thread principal pourrait théoriquement invalider la référence du thread lancé. En disant à Rust de déplacer la propriété de `v` au thread lancé, nous garantissons à Rust que le thread principal ne va plus utiliser `v`. Si nous modifions la Liste 16-4 de la même manière, nous violons alors les règles d'appartenance lorsque nous essayons d'utiliser `v` dans le thread principal. Le mot-clé `move` remplace la valeur par défaut prudente de Rust qui consiste à prêter ; il ne nous permet pas de violer les règles d'appartenance.

Maintenant que nous avons couvert ce qu'est un thread et les méthodes fournies par l'API de thread, regardons quelques situations dans lesquelles nous pouvons utiliser des threads.
