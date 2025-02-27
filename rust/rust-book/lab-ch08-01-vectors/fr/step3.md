# Updating a Vector

Pour créer un vecteur puis y ajouter des éléments, nous pouvons utiliser la méthode `push`, comme montré dans la Liste 8-3.

```rust
let mut v = Vec::new();

v.push(5);
v.push(6);
v.push(7);
v.push(8);
```

Liste 8-3: Utilisation de la méthode `push` pour ajouter des valeurs à un vecteur

Comme pour toute variable, si nous voulons être en mesure de changer sa valeur, nous devons la rendre mutable à l'aide du mot clé `mut`, comme discuté au Chapitre 3. Les nombres que nous plaçons à l'intérieur sont tous de type `i32`, et Rust le déduit à partir des données, de sorte que nous n'avons pas besoin de l'annotation `Vec<i32>`.
