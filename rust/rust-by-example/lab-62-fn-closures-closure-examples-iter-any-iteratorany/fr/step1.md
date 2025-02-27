# Iterator::any

`Iterator::any` est une fonction qui, lorsqu'elle est passée un itérateur, renverra `true` si un élément quelconque satisfait le prédicat. Sinon, elle renverra `false`. Sa signature :

```rust
pub trait Iterator {
    // Le type sur lequel on itère.
    type Item;

    // `any` prend `&mut self`, ce qui signifie que l'appelant peut être emprunté
    // et modifié, mais pas consommé.
    fn any<F>(&mut self, f: F) -> bool where
        // `FnMut` signifie que toute variable capturée peut au plus être
        // modifiée, pas consommée. `Self::Item` indique qu'elle prend
        // les arguments de la closure par valeur.
        F: FnMut(Self::Item) -> bool;
}
```

```rust
fn main() {
    let vec1 = vec![1, 2, 3];
    let vec2 = vec![4, 5, 6];

    // `iter()` pour les vecteurs renvoie `&i32`. Déstructurez pour obtenir `i32`.
    println!("2 dans vec1 : {}", vec1.iter()    .any(|&x| x == 2));
    // `into_iter()` pour les vecteurs renvoie `i32`. Aucune déstructuration n'est nécessaire.
    println!("2 dans vec2 : {}", vec2.into_iter().any(|x| x == 2));

    // `iter()` ne prend que l'emprunt de `vec1` et de ses éléments, donc ils peuvent être utilisés à nouveau
    println!("Longueur de vec1 : {}", vec1.len());
    println!("Premier élément de vec1 est : {}", vec1[0]);
    // `into_iter()` déplace `vec2` et ses éléments, donc ils ne peuvent plus être utilisés
    // println!("Premier élément de vec2 est : {}", vec2[0]);
    // println!("Longueur de vec2 : {}", vec2.len());
    // TODO : décommentez les deux lignes ci-dessus et observez les erreurs du compilateur.

    let array1 = [1, 2, 3];
    let array2 = [4, 5, 6];

    // `iter()` pour les tableaux renvoie `&i32`.
    println!("2 dans array1 : {}", array1.iter()    .any(|&x| x == 2));
    // `into_iter()` pour les tableaux renvoie `i32`.
    println!("2 dans array2 : {}", array2.into_iter().any(|x| x == 2));
}
```
