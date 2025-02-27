# Methods That Consume the Iterator

Le trait `Iterator` a un certain nombre de méthodes différentes avec des implémentations par défaut fournies par la bibliothèque standard ; vous pouvez en découvrir plus sur ces méthodes en consultant la documentation de l'API de la bibliothèque standard pour le trait `Iterator`. Certaines de ces méthodes appellent la méthode `next` dans leur définition, voilà pourquoi vous êtes obligé d'implémenter la méthode `next` lors de l'implémentation du trait `Iterator`.

Les méthodes qui appellent `next` sont appelées _adapters consommateurs_ car les appeler utilise l'itérateur. Un exemple est la méthode `sum`, qui prend la propriété de l'itérateur et itère sur les éléments en appelant répétitivement `next`, consommant ainsi l'itérateur. Pendant l'itération, elle ajoute chaque élément à un total en cours et renvoie le total une fois l'itération terminée. La Liste 13-13 a un test illustrant l'utilisation de la méthode `sum`.

Nom du fichier : `src/lib.rs`

```rust
#[test]
fn iterator_sum() {
    let v1 = vec![1, 2, 3];

    let v1_iter = v1.iter();

    let total: i32 = v1_iter.sum();

    assert_eq!(total, 6);
}
```

Liste 13-13: Appel de la méthode `sum` pour obtenir le total de tous les éléments de l'itérateur

Nous ne sommes pas autorisés à utiliser `v1_iter` après l'appel à `sum` car `sum` prend la propriété de l'itérateur sur lequel nous l'appelons.
