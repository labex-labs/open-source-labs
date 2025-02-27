# Iterating Over the Values in a Vector

Pour accéder à chaque élément d'un vecteur tour à tour, nous devrions parcourir tous les éléments plutôt que d'utiliser des indices pour accéder à un élément à la fois. La Liste 8-7 montre comment utiliser une boucle `for` pour obtenir des références immuables à chaque élément dans un vecteur de valeurs de type `i32` et les afficher.

```rust
let v = vec![100, 32, 57];
for i in &v {
    println!("{i}");
}
```

Liste 8-7: Affichage de chaque élément d'un vecteur en itérant sur les éléments à l'aide d'une boucle `for`

Nous pouvons également itérer sur des références mutables à chaque élément dans un vecteur mutable afin de modifier tous les éléments. La boucle `for` dans la Liste 8-8 ajoutera `50` à chaque élément.

```rust
let mut v = vec![100, 32, 57];
for i in &mut v {
    *i += 50;
}
```

Liste 8-8: Itération sur des références mutables aux éléments d'un vecteur

Pour modifier la valeur à laquelle la référence mutable fait référence, nous devons utiliser l'opérateur de déréférence `*` pour accéder à la valeur dans `i` avant d'être en mesure d'utiliser l'opérateur `+=`. Nous en parlerons plus longuement dans "Following the Pointer to the Value".

L'itération sur un vecteur, que ce soit de manière immuable ou mutable, est sécurisée grâce aux règles du vérificateur d'emprunt. Si nous avions essayé d'insérer ou de supprimer des éléments dans les corps de boucle `for` des Listes 8-7 et 8-8, nous aurions eu une erreur du compilateur similaire à celle que nous avons eu avec le code de la Liste 8-6. La référence au vecteur que la boucle `for` détient empêche la modification simultanée de l'ensemble du vecteur.
