# Creating a New Vector

Pour créer un nouveau vecteur vide, nous appelons la fonction `Vec::new`, comme montré dans la Liste 8-1.

```rust
let v: Vec<i32> = Vec::new();
```

Liste 8-1: Création d'un nouveau vecteur vide pour stocker des valeurs de type `i32`

Notez que nous avons ajouté une annotation de type ici. Comme nous n'insérons aucune valeur dans ce vecteur, Rust ne sait pas quel type d'éléments nous avons l'intention de stocker. Ceci est un point important. Les vecteurs sont implémentés à l'aide de génériques ; nous aborderons la manière d'utiliser les génériques avec vos propres types au Chapitre 10. Pour l'instant, sachez que le type `Vec<T>` fourni par la bibliothèque standard peut stocker n'importe quel type. Lorsque nous créons un vecteur pour stocker un type spécifique, nous pouvons spécifier le type entre crochets. Dans la Liste 8-1, nous avons dit à Rust que le `Vec<T>` dans `v` stockera des éléments du type `i32`.

Plus souvent, vous créerez un `Vec<T>` avec des valeurs initiales et Rust devinera le type de valeur que vous voulez stocker, de sorte que vous n'aurez rarement besoin de cette annotation de type. Rust fournit commodément le macro `vec!`, qui créera un nouveau vecteur qui stockera les valeurs que vous lui donnez. La Liste 8-2 crée un nouveau `Vec<i32>` qui stocke les valeurs `1`, `2` et `3`. Le type entier est `i32` car c'est le type entier par défaut, comme nous l'avons discuté dans "Data Types".

```rust
let v = vec![1, 2, 3];
```

Liste 8-2: Création d'un nouveau vecteur contenant des valeurs

Comme nous avons donné des valeurs initiales de type `i32`, Rust peut deviner que le type de `v` est `Vec<i32>`, et l'annotation de type n'est pas nécessaire. Ensuite, nous examinerons comment modifier un vecteur.
