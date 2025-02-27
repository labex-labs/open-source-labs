# Bringing Paths into Scope with the use Keyword

Devoir écrire les chemins pour appeler des fonctions peut paraître pratique et répétitif. Dans la Liste 7-7, que nous ayons choisi le chemin absolu ou relatif vers la fonction `add_to_waitlist`, chaque fois que nous avons voulu appeler `add_to_waitlist`, nous avons dû également spécifier `front_of_house` et `hosting`. Heureusement, il existe un moyen de simplifier ce processus : nous pouvons créer un raccourci pour un chemin une fois avec le mot-clé `use`, puis utiliser le nom plus court partout ailleurs dans la portée.

Dans la Liste 7-11, nous ramenons le module `crate::front_of_house::hosting` dans la portée de la fonction `eat_at_restaurant` afin que nous n'ayons qu'à spécifier `hosting::add_to_waitlist` pour appeler la fonction `add_to_waitlist` dans `eat_at_restaurant`.

Nom de fichier : `src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

use crate::front_of_house::hosting;

pub fn eat_at_restaurant() {
    hosting::add_to_waitlist();
}
```

Liste 7-11 : Amener un module dans la portée avec `use`

Ajouter `use` et un chemin dans une portée est similaire à créer un lien symbolique dans le système de fichiers. En ajoutant `use crate::front_of_house::hosting` dans la racine du crate, `hosting` est désormais un nom valide dans cette portée, tout comme si le module `hosting` avait été défini dans la racine du crate. Les chemins ramenés dans la portée avec `use` vérifient également la confidentialité, comme tous les autres chemins.

Notez que `use` ne crée le raccourci que pour la portée particulière dans laquelle `use` apparaît. La Liste 7-12 déplace la fonction `eat_at_restaurant` dans un nouveau module enfant nommé `customer`, qui est alors une portée différente de l'énoncé `use`, de sorte que le corps de la fonction ne compilera pas.

Nom de fichier : `src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

use crate::front_of_house::hosting;

mod customer {
    pub fn eat_at_restaurant() {
        hosting::add_to_waitlist();
    }
}
```

Liste 7-12 : Un énoncé `use` n'est valable que dans la portée où il se trouve.

L'erreur du compilateur montre que le raccourci n'est plus valable dans le module `customer` :

```bash
error[E0433]: failed to resolve: use of undeclared crate or module `hosting`
  --> src/lib.rs:11:9
   |
11 |         hosting::add_to_waitlist();
   |         ^^^^^^^ use of undeclared crate or module `hosting`

warning: unused import: `crate::front_of_house::hosting`
 --> src/lib.rs:7:5
  |
7 | use crate::front_of_house::hosting;
  |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  |
  = note: `#[warn(unused_imports)]` on by default
```

Remarquez qu'il y a également un avertissement indiquant que `use` n'est plus utilisé dans sa portée! Pour résoudre ce problème, déplacez également `use` dans le module `customer`, ou faites référence au raccourci dans le module parent avec `super::hosting` dans le module enfant `customer`.
