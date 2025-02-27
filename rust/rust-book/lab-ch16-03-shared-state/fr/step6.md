# Compte-rendu de référence atomique avec Arc`<T>`{=html}

Heureusement, `Arc<T>` _est_ un type similaire à `Rc<T>` qui est sécurisé à utiliser dans des situations concurrentes. Le _a_ signifie _atomique_, ce qui signifie qu'il s'agit d'un type _compté en référence de manière atomique_. Les atomes sont un autre type de primitif de concurrence que nous ne détaillerons pas ici : consultez la documentation de la bibliothèque standard pour `std::sync::atomic` pour plus de détails. À ce stade, vous n'avez qu'à savoir que les atomes fonctionnent comme les types primitifs mais sont sécurisés à partager entre les threads.

Vous vous demandez peut-être pourquoi tous les types primitifs ne sont pas atomiques et pourquoi les types de la bibliothèque standard ne sont pas implémentés pour utiliser `Arc<T>` par défaut. La raison est que la sécurité des threads entraîne une pénalité de performance que vous ne voulez payer que si vous avez vraiment besoin. Si vous effectuez seulement des opérations sur des valeurs dans un seul thread, votre code peut exécuter plus rapidement s'il n'a pas à appliquer les garanties que les atomes offrent.

Revenons à notre exemple : `Arc<T>` et `Rc<T>` ont la même API, donc nous corrigons notre programme en changeant la ligne `use`, l'appel à `new` et l'appel à `clone`. Le code de la liste 16-15 compilera enfin et s'exécutera.

Nom de fichier : `src/main.rs`

```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    let counter = Arc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..10 {
        let counter = Arc::clone(&counter);
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

Liste 16-15 : Utilisation d'un `Arc<T>` pour emballer le `Mutex<T>` afin de pouvoir partager la propriété entre plusieurs threads

Ce code affichera ceci :

```rust
Result: 10
```

Nous y sommes arrivés! Nous avons compté de 0 à 10, ce qui peut ne pas sembler très impressionnant, mais cela nous a vraiment appris beaucoup sur `Mutex<T>` et la sécurité des threads. Vous pouvez également utiliser la structure de ce programme pour effectuer des opérations plus complexes que simplement incrémenter un compteur. En utilisant cette stratégie, vous pouvez diviser un calcul en parties indépendantes, répartir ces parties entre les threads, puis utiliser un `Mutex<T>` pour que chaque thread mette à jour le résultat final avec sa partie.

Notez que si vous effectuez des opérations numériques simples, il existe des types plus simples que les types `Mutex<T>` fournis par le module `std::sync::atomic` de la bibliothèque standard. Ces types offrent un accès sécurisé, concurrent et atomique aux types primitifs. Nous avons choisi d'utiliser `Mutex<T>` avec un type primitif pour cet exemple afin de pouvoir nous concentrer sur la manière dont `Mutex<T>` fonctionne.
