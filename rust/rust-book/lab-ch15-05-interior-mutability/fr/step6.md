# Autoriser plusieurs propriétaires de données mutables avec Rc`<T>`{=html} et RefCell`<T>`{=html}

Une manière courante d'utiliser `RefCell<T>` est en combinaison avec `Rc<T>`. Rappelez-vous que `Rc<T>` vous permet d'avoir plusieurs propriétaires pour certaines données, mais il ne vous donne qu'un accès immuable à ces données. Si vous avez un `Rc<T>` qui contient un `RefCell<T>`, vous pouvez obtenir une valeur qui peut avoir plusieurs propriétaires _et_ que vous pouvez modifier!

Par exemple, rappelez-vous l'exemple de liste cons dans la liste 15-18 où nous avons utilisé `Rc<T>` pour permettre à plusieurs listes de partager la propriété d'une autre liste. Étant donné que `Rc<T>` ne contient que des valeurs immuables, nous ne pouvons pas modifier aucune des valeurs de la liste une fois qu'elles ont été créées. Ajoutons `RefCell<T>` pour sa capacité à modifier les valeurs dans les listes. La liste 15-24 montre que, en utilisant un `RefCell<T>` dans la définition de `Cons`, nous pouvons modifier la valeur stockée dans toutes les listes.

Nom de fichier : `src/main.rs`

```rust
#[derive(Debug)]
enum List {
    Cons(Rc<RefCell<i32>>, Rc<List>),
    Nil,
}

use crate::List::{Cons, Nil};
use std::cell::RefCell;
use std::rc::Rc;

fn main() {
  1 let value = Rc::new(RefCell::new(5));

  2 let a = Rc::new(Cons(Rc::clone(&value), Rc::new(Nil)));

    let b = Cons(Rc::new(RefCell::new(3)), Rc::clone(&a));
    let c = Cons(Rc::new(RefCell::new(4)), Rc::clone(&a));

  3 *value.borrow_mut() += 10;

    println!("a after = {:?}", a);
    println!("b after = {:?}", b);
    println!("c after = {:?}", c);
}
```

Liste 15-24 : Utilisation de `Rc<RefCell<i32>>` pour créer une `List` que nous pouvons modifier

Nous créons une valeur qui est une instance de `Rc<RefCell<i32>>` et la stockons dans une variable nommée `value` \[1\] pour pouvoir y accéder directement plus tard. Ensuite, nous créons une `List` dans `a` avec une variante `Cons` qui contient `value` \[2\]. Nous devons cloner `value` pour que `a` et `value` aient tous les deux la propriété de la valeur interne `5` plutôt que de transférer la propriété de `value` à `a` ou d'avoir `a` emprunter `value`.

Nous enveloppons la liste `a` dans un `Rc<T>` pour que lorsque nous créons les listes `b` et `c`, elles puissent toutes deux faire référence à `a`, comme nous l'avons fait dans la liste 15-18.

Après avoir créé les listes dans `a`, `b` et `c`, nous voulons ajouter 10 à la valeur dans `value` \[3\]. Nous le faisons en appelant `borrow_mut` sur `value`, qui utilise la fonctionnalité d'indirection automatique dont nous avons parlé dans "Où est l'opérateur -\>?" pour indirectionner le `Rc<T>` vers la valeur interne `RefCell<T>`. La méthode `borrow_mut` renvoie un pointeur intelligent `RefMut<T>`, et nous utilisons l'opérateur d'indirection dessus et changeons la valeur interne.

Lorsque nous imprimons `a`, `b` et `c`, nous pouvons voir qu'elles ont toutes la valeur modifiée de `15` plutôt que de `5` :

    a after = Cons(RefCell { value: 15 }, Nil)
    b after = Cons(RefCell { value: 3 }, Cons(RefCell { value: 15 }, Nil))
    c after = Cons(RefCell { value: 4 }, Cons(RefCell { value: 15 }, Nil))

Cette technique est assez pratique! En utilisant `RefCell<T>`, nous avons une valeur `List` qui est extérieurement immuable. Mais nous pouvons utiliser les méthodes sur `RefCell<T>` qui donnent accès à sa mutabilité interne pour modifier nos données lorsque nécessaire. Les vérifications à l'exécution des règles d'emprunt nous protègent contre les courses de données, et il est parfois intéressant de sacrifier un peu de vitesse pour cette flexibilité dans nos structures de données. Notez que `RefCell<T>` ne fonctionne pas pour le code multithreadé! `Mutex<T>` est la version thread-safe de `RefCell<T>`, et nous en parlerons au chapitre 16.
