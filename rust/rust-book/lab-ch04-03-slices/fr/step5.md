# Autres tranches

Les tranches de chaîne, comme vous pouvez l'imaginer, sont spécifiques aux chaînes. Mais il existe également un type de tranche plus général. Considérez ce tableau :

```rust
let a = [1, 2, 3, 4, 5];
```

De même que nous pouvons vouloir faire référence à une partie d'une chaîne, nous pouvons vouloir faire référence à une partie d'un tableau. Nous le ferions comme ceci :

```rust
let a = [1, 2, 3, 4, 5];

let slice = &a[1..3];

assert_eq!(slice, &[2, 3]);
```

Cette tranche a le type `&[i32]`. Elle fonctionne de la même manière que les tranches de chaîne, en stockant une référence au premier élément et une longueur. Vous utiliserez ce type de tranche pour toutes sortes d'autres collections. Nous aborderons ces collections en détail lorsque nous parlerons des vecteurs au Chapitre 8.
