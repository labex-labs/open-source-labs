# The Iterator Trait and the next Method

Tous les itérateurs implémentent un trait nommé `Iterator` qui est défini dans la bibliothèque standard. La définition du trait ressemble à ceci :

```rust
pub trait Iterator {
    type Item;

    fn next(&mut self) -> Option<Self::Item>;

    // méthodes avec des implémentations par défaut omises
}
```

Remarquez que cette définition utilise une nouvelle syntaxe : `type Item` et `Self::Item`, qui définissent un _type associé_ avec ce trait. Nous parlerons des types associés en profondeur au Chapitre 19. Pour l'instant, tout ce que vous avez besoin de savoir est que ce code indique que l'implémentation du trait `Iterator` nécessite également la définition d'un type `Item`, et ce type `Item` est utilisé dans le type de retour de la méthode `next`. En d'autres termes, le type `Item` sera le type renvoyé par l'itérateur.

Le trait `Iterator` ne demande aux implémentateurs de définir qu'une seule méthode : la méthode `next`, qui renvoie un élément de l'itérateur à la fois, emballé dans `Some`, et, lorsque l'itération est terminée, renvoie `None`.

Nous pouvons appeler la méthode `next` directement sur les itérateurs ; la Liste 13-12 montre quelles valeurs sont renvoyées par des appels répétés à `next` sur l'itérateur créé à partir du vecteur.

Nom du fichier : `src/lib.rs`

```rust
#[test]
fn iterator_demonstration() {
    let v1 = vec![1, 2, 3];

    let mut v1_iter = v1.iter();

    assert_eq!(v1_iter.next(), Some(&1));
    assert_eq!(v1_iter.next(), Some(&2));
    assert_eq!(v1_iter.next(), Some(&3));
    assert_eq!(v1_iter.next(), None);
}
```

Liste 13-12: Appel de la méthode `next` sur un itérateur

Notez que nous avons dû rendre `v1_iter` mutable : appeler la méthode `next` sur un itérateur change l'état interne que l'itérateur utilise pour suivre où il se trouve dans la séquence. En d'autres termes, ce code _consomme_, ou utilise, l'itérateur. Chaque appel à `next` consomme un élément de l'itérateur. Nous n'avons pas dû rendre `v1_iter` mutable lorsque nous avons utilisé une boucle `for` car la boucle a pris la propriété de `v1_iter` et l'a rendu mutable en coulisse.

Notez également que les valeurs que nous obtenons des appels à `next` sont des références immuables aux valeurs dans le vecteur. La méthode `iter` produit un itérateur sur des références immuables. Si nous voulons créer un itérateur qui prend la propriété de `v1` et renvoie des valeurs propriétaires, nous pouvons appeler `into_iter` au lieu de `iter`. De même, si nous voulons itérer sur des références mutables, nous pouvons appeler `iter_mut` au lieu de `iter`.
