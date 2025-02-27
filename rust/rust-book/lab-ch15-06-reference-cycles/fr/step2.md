# Création d'un cycle de référence

Regardons comment un cycle de référence peut se produire et comment le prévenir, en commençant par la définition de l'énumération `List` et d'une méthode `tail` dans la liste 15-25.

Nom de fichier : `src/main.rs`

```rust
use crate::List::{Cons, Nil};
use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug)]
enum List {
  1 Cons(i32, RefCell<Rc<List>>),
    Nil,
}

impl List {
  2 fn tail(&self) -> Option<&RefCell<Rc<List>>> {
        match self {
            Cons(_, item) => Some(item),
            Nil => None,
        }
    }
}
```

Liste 15-25 : Une définition de liste cons qui contient un `RefCell<T>` pour pouvoir modifier ce que le variant `Cons` pointe

Nous utilisons une autre variante de la définition de `List` de la liste 15-5. Le deuxième élément du variant `Cons` est désormais `RefCell<Rc<List>>` \[1\], ce qui signifie que, au lieu d'avoir la possibilité de modifier la valeur `i32` comme nous l'avons fait dans la liste 15-24, nous voulons modifier la valeur de `List` vers laquelle un variant `Cons` pointe. Nous ajoutons également une méthode `tail` \[2\] pour faciliter l'accès au deuxième élément si nous avons un variant `Cons`.

Dans la liste 15-26, nous ajoutons une fonction `main` qui utilise les définitions de la liste 15-25. Ce code crée une liste dans `a` et une liste dans `b` qui pointe vers la liste dans `a`. Ensuite, il modifie la liste dans `a` pour qu'elle pointe vers `b`, créant ainsi un cycle de référence. Il y a des instructions `println!` tout au long pour montrer quels sont les comptages de références à différents points de ce processus.

Nom de fichier : `src/main.rs`

```rust
fn main() {
  1 let a = Rc::new(Cons(5, RefCell::new(Rc::new(Nil))));

    println!("a initial rc count = {}", Rc::strong_count(&a));
    println!("a next item = {:?}", a.tail());

  2 let b = Rc::new(Cons(10, RefCell::new(Rc::clone(&a))));

    println!(
        "a rc count after b creation = {}",
        Rc::strong_count(&a)
    );
    println!("b initial rc count = {}", Rc::strong_count(&b));
    println!("b next item = {:?}", b.tail());

  3 if let Some(link) = a.tail() {
      4 *link.borrow_mut() = Rc::clone(&b);
    }

    println!(
        "b rc count after changing a = {}",
        Rc::strong_count(&b)
    );
    println!(
        "a rc count after changing a = {}",
        Rc::strong_count(&a)
    );

    // Désactivez la ligne suivante pour voir qu'il y a un cycle ;
    // cela entraînera un débordement de pile
    // println!("a next item = {:?}", a.tail());
}
```

Liste 15-26 : Création d'un cycle de référence entre deux valeurs `List` qui se pointent mutuellement

Nous créons une instance `Rc<List>` contenant une valeur `List` dans la variable `a` avec une liste initiale de `5, Nil` \[1\]. Ensuite, nous créons une instance `Rc<List>` contenant une autre valeur `List` dans la variable `b` qui contient la valeur `10` et pointe vers la liste dans `a` \[2\].

Nous modifions `a` pour qu'elle pointe vers `b` au lieu de `Nil`, créant ainsi un cycle. Nous le faisons en utilisant la méthode `tail` pour obtenir une référence au `RefCell<Rc<List>>` dans `a`, que nous mettons dans la variable `link` \[3\]. Ensuite, nous utilisons la méthode `borrow_mut` sur le `RefCell<Rc<List>>` pour changer la valeur à l'intérieur d'un `Rc<List>` qui contient une valeur `Nil` en l'`Rc<List>` dans `b` \[4\].

Lorsque nous exécutons ce code, en laissant la dernière instruction `println!` commentée pour le moment, nous obtiendrons cette sortie :

    a initial rc count = 1
    a next item = Some(RefCell { value: Nil })
    a rc count after b creation = 2
    b initial rc count = 1
    b next item = Some(RefCell { value: Cons(5, RefCell { value: Nil }) })
    b rc count after changing a = 2
    a rc count after changing a = 2

Le comptage de références des instances `Rc<List>` dans `a` et `b` est de 2 après avoir modifié la liste dans `a` pour qu'elle pointe vers `b`. À la fin de `main`, Rust supprime la variable `b`, ce qui diminue le comptage de références de l'instance `Rc<List>` de `b` de 2 à 1. La mémoire que `Rc<List>` a sur le tas ne sera pas supprimée à ce moment-là car son comptage de références est 1, pas 0. Ensuite, Rust supprime `a`, ce qui diminue également le comptage de références de l'instance `Rc<List>` de `a` de 2 à 1. La mémoire de cette instance ne peut pas non plus être supprimée, car l'autre instance `Rc<List>` la référence toujours. La mémoire allouée à la liste restera incollectée pour toujours. Pour visualiser ce cycle de référence, nous avons créé un diagramme dans la figure 15-4.

Figure 15-4 : Un cycle de référence entre les listes `a` et `b` qui se pointent mutuellement

Si vous activez la dernière instruction `println!` et exécutez le programme, Rust tentera d'afficher ce cycle avec `a` qui pointe vers `b` qui pointe vers `a` et ainsi de suite jusqu'à ce qu'il y ait un débordement de pile.

Comparé à un programme du monde réel, les conséquences de la création d'un cycle de référence dans cet exemple ne sont pas très graves : juste après avoir créé le cycle de référence, le programme se termine. Cependant, si un programme plus complexe allouait beaucoup de mémoire dans un cycle et la conservait longtemps, le programme utiliserait plus de mémoire qu'il n'en avait besoin et pourrait saturer le système, entraînant ainsi une insuffisance de mémoire disponible.

La création de cycles de référence n'est pas facile, mais ce n'est pas impossible non plus. Si vous avez des valeurs `RefCell<T>` qui contiennent des valeurs `Rc<T>` ou des combinaisons imbriquées similaires de types avec mutabilité interne et comptage de références, vous devez vous assurer de ne pas créer de cycles ; vous ne pouvez pas compter sur Rust pour les détecter. La création d'un cycle de référence serait une erreur logique dans votre programme que vous devriez minimiser en utilisant des tests automatisés, des révisions de code et d'autres pratiques de développement logiciel.

Une autre solution pour éviter les cycles de référence est de reorganiser vos structures de données de manière à ce que certaines références expriment la propriété et que certaines références n'en expriment pas. En conséquence, vous pouvez avoir des cycles composés de certaines relations de propriété et de certaines relations non de propriété, et seule la relation de propriété affecte la possibilité de supprimer une valeur. Dans la liste 15-25, nous voulons toujours que les variants `Cons` possèdent leur liste, donc il n'est pas possible de reorganiser la structure de données. Regardons un exemple utilisant des graphes composés de nœuds parents et de nœuds enfants pour voir dans quels cas les relations non de propriété sont un moyen approprié de prévenir les cycles de référence.
