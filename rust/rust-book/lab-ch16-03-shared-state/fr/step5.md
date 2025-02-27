# Propriété multiple avec plusieurs threads

Au chapitre 15, nous avons donné une valeur à plusieurs propriétaires en utilisant le pointeur intelligent `Rc<T>` pour créer une valeur comptée en référence. Faisons de même ici et voyons ce qui se passe. Nous emballerons le `Mutex<T>` dans `Rc<T>` dans la liste 16-14 et clonerons le `Rc<T>` avant de transférer la propriété au thread.

Nom de fichier : `src/main.rs`

```rust
use std::rc::Rc;
use std::sync::Mutex;
use std::thread;

fn main() {
    let counter = Rc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..10 {
        let counter = Rc::clone(&counter);
        let handle = thread::spawn(move || {
            let mut num = counter.lock().unwrap();

            *num += 1;
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("Result: {}", *counter.lock().unwrap());
}
```

Liste 16-14 : Tentative d'utilisation de `Rc<T>` pour autoriser plusieurs threads à posséder le `Mutex<T>`

Encore une fois, nous compilons et obtenons... des erreurs différentes! Le compilateur nous apprend beaucoup de choses.

```bash
error[E0277]: `Rc<Mutex<i32>>` cannot be sent between threads safely 1
   --> src/main.rs:11:22
    |
11  |           let handle = thread::spawn(move || {
    |  ______________________^^^^^^^^^^^^^_-
    | |                      |
    | |                      `Rc<Mutex<i32>>` cannot be sent between threads
safely
12  | |             let mut num = counter.lock().unwrap();
13  | |
14  | |             *num += 1;
15  | |         });
    | |_________- within this `[closure@src/main.rs:11:36: 15:10]`
    |
= help: within `[closure@src/main.rs:11:36: 15:10]`, the trait `Send` is not
implemented for `Rc<Mutex<i32>>` 2
    = note: required because it appears within the type
`[closure@src/main.rs:11:36: 15:10]`
note: required by a bound in `spawn`
```

Wow, ce message d'erreur est très long! Voici la partie importante sur laquelle se concentrer : ``Rc<Mutex<i32>>` cannot be sent between threads safely` [1]. Le compilateur nous dit également pourquoi : `the trait `Send` is not implemented for `Rc<Mutex<i32>>`` \[2\]. Nous parlerons de `Send` dans la section suivante : c'est l'un des traits qui garantit que les types que nous utilisons avec les threads sont destinés à être utilisés dans des situations concurrentes.

Malheureusement, il n'est pas sécurisé de partager `Rc<T>` entre les threads. Lorsque `Rc<T>` gère le compteur de références, il incrémente le compte pour chaque appel à `clone` et décrémente le compte lorsque chaque clone est supprimé. Mais il n'utilise aucun primitif de concurrence pour s'assurer que les modifications du compte ne peuvent pas être interrompues par un autre thread. Cela pourrait entraîner des comptes erronés - des bogues subtils qui pourraient à leur tour entraîner des fuites mémoire ou une valeur qui serait supprimée avant que nous ayons fini avec elle. Ce dont nous avons besoin, c'est un type exactement comme `Rc<T>` mais qui modifie le compteur de références de manière sécurisée pour les threads.
