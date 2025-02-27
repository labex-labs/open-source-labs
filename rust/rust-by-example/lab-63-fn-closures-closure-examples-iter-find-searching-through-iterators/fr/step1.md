# Recherche dans les itérateurs

`Iterator::find` est une fonction qui itère sur un itérateur et recherche la première valeur qui satisfait une certaine condition. Si aucune des valeurs ne satisfait la condition, elle renvoie `None`. Sa signature :

```rust
pub trait Iterator {
    // Le type sur lequel on itère.
    type Item;

    // `find` prend `&mut self`, ce qui signifie que l'appelant peut être emprunté
    // et modifié, mais pas consommé.
    fn find<P>(&mut self, predicate: P) -> Option<Self::Item> where
        // `FnMut` signifie que toute variable capturée peut au plus être
        // modifiée, pas consommée. `&Self::Item` indique qu'elle prend
        // les arguments de la clôture par référence.
        P: FnMut(&Self::Item) -> bool;
}
```

```rust
fn main() {
    let vec1 = vec![1, 2, 3];
    let vec2 = vec![4, 5, 6];

    // `iter()` pour les vecteurs produit `&i32`.
    let mut iter = vec1.iter();
    // `into_iter()` pour les vecteurs produit `i32`.
    let mut into_iter = vec2.into_iter();

    // `iter()` pour les vecteurs produit `&i32`, et nous voulons référencer l'un de ses
    // éléments, donc nous devons déstructurer `&&i32` en `i32`
    println!("Trouver 2 dans vec1: {:?}", iter    .find(|&&x| x == 2));
    // `into_iter()` pour les vecteurs produit `i32`, et nous voulons référencer l'un de
    // ses éléments, donc nous devons déstructurer `&i32` en `i32`
    println!("Trouver 2 dans vec2: {:?}", into_iter.find(| &x| x == 2));

    let array1 = [1, 2, 3];
    let array2 = [4, 5, 6];

    // `iter()` pour les tableaux produit `&&i32`
    println!("Trouver 2 dans array1: {:?}", array1.iter()    .find(|&&x| x == 2));
    // `into_iter()` pour les tableaux produit `&i32`
    println!("Trouver 2 dans array2: {:?}", array2.into_iter().find(|&x| x == 2));
}
```

`Iterator::find` vous donne une référence à l'élément. Mais si vous voulez l'_index_ de l'élément, utilisez `Iterator::position`.

```rust
fn main() {
    let vec = vec![1, 9, 3, 3, 13, 2];

    // `iter()` pour les vecteurs produit `&i32` et `position()` ne prend pas de référence, donc
    // nous devons déstructurer `&i32` en `i32`
    let index_of_first_even_number = vec.iter().position(|&x| x % 2 == 0);
    assert_eq!(index_of_first_even_number, Some(5));

    // `into_iter()` pour les vecteurs produit `i32` et `position()` ne prend pas de référence, donc
    // nous n'avons pas besoin de déstructurer
    let index_of_first_negative_number = vec.into_iter().position(|x| x < 0);
    assert_eq!(index_of_first_negative_number, None);
}
```
