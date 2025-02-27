# Utilisation de supertraits

Parfois, vous pouvez écrire une définition de trait qui dépend d'un autre trait : pour qu'un type implémente le premier trait, vous voulez exiger que ce type implémente également le second trait. Vous le feriez pour que la définition de votre trait puisse utiliser les éléments associés du second trait. Le trait dont dépend la définition de votre trait est appelé un _supertrait_ de votre trait.

Par exemple, disons que nous voulons créer un trait `OutlinePrint` avec une méthode `outline_print` qui imprimera une valeur donnée formatée de manière à être encadrée d'étoiles. C'est-à-dire que, étant donné une structure `Point` qui implémente le trait `Display` de la bibliothèque standard pour obtenir `(x, y)`, lorsque nous appelons `outline_print` sur une instance de `Point` qui a `1` pour `x` et `3` pour `y`, elle devrait imprimer ce qui suit :

    **********
    *        *
    * (1, 3) *
    *        *
    **********

Dans l'implémentation de la méthode `outline_print`, nous voulons utiliser la fonctionnalité du trait `Display`. Par conséquent, nous devons spécifier que le trait `OutlinePrint` ne fonctionnera que pour les types qui implémentent également `Display` et fournissent la fonctionnalité dont `OutlinePrint` a besoin. Nous pouvons le faire dans la définition du trait en spécifiant `OutlinePrint: Display`. Cette technique est similaire à l'ajout d'une contrainte de trait au trait. La Liste 19-22 montre une implémentation du trait `OutlinePrint`.

Nom de fichier : `src/main.rs`

```rust
use std::fmt;

trait OutlinePrint: fmt::Display {
    fn outline_print(&self) {
        let output = self.to_string();
        let len = output.len();
        println!("{}", "*".repeat(len + 4));
        println!("*{}*", " ".repeat(len + 2));
        println!("* {} *", output);
        println!("*{}*", " ".repeat(len + 2));
        println!("{}", "*".repeat(len + 4));
    }
}
```

Liste 19-22 : Implémentation du trait `OutlinePrint` qui nécessite la fonctionnalité de `Display`

Comme nous avons spécifié que `OutlinePrint` nécessite le trait `Display`, nous pouvons utiliser la fonction `to_string` qui est automatiquement implémentée pour tout type qui implémente `Display`. Si nous essayions d'utiliser `to_string` sans ajouter deux-points et en spécifiant le trait `Display` après le nom du trait, nous obtiendrions une erreur indiquant qu'aucune méthode nommée `to_string` n'a été trouvée pour le type `&Self` dans la portée actuelle.

Voyons ce qui se passe lorsque nous essayons d'implémenter `OutlinePrint` sur un type qui n'implémente pas `Display`, tel que la structure `Point` :

Nom de fichier : `src/main.rs`

```rust
struct Point {
    x: i32,
    y: i32,
}

impl OutlinePrint for Point {}
```

Nous obtenons une erreur indiquant que `Display` est requis mais non implémenté :

```bash
error[E0277]: `Point` doesn't implement `std::fmt::Display`
  --> src/main.rs:20:6
   |
20 | impl OutlinePrint for Point {}
   |      ^^^^^^^^^^^^ `Point` cannot be formatted with the default formatter
   |
   = help: the trait `std::fmt::Display` is not implemented for `Point`
   = note: in format strings you may be able to use `{:?}` (or {:#?} for
pretty-print) instead
note: required by a bound in `OutlinePrint`
  --> src/main.rs:3:21
   |
3  | trait OutlinePrint: fmt::Display {
   |                     ^^^^^^^^^^^^ required by this bound in `OutlinePrint`
```

Pour corriger ceci, nous implémentons `Display` sur `Point` et satisfaisons la contrainte que `OutlinePrint` exige, comme ceci :

Nom de fichier : `src/main.rs`

```rust
use std::fmt;

impl fmt::Display for Point {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "({}, {})", self.x, self.y)
    }
}
```

Ensuite, l'implémentation du trait `OutlinePrint` sur `Point` compilera avec succès, et nous pouvons appeler `outline_print` sur une instance de `Point` pour l'afficher dans un contour d'étoiles.
