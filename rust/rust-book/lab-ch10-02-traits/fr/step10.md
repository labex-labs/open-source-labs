# Utiliser des Contraintes de Trait pour Implémenter des Méthodes Conditionnellement

En utilisant une contrainte de trait avec un bloc `impl` qui utilise des paramètres de type générique, nous pouvons implémenter des méthodes conditionnellement pour les types qui implémentent les traits spécifiés. Par exemple, le type `Pair<T>` dans la liste 10-15 implémente toujours la fonction `new` pour retourner une nouvelle instance de `Pair<T>` (rappelez-vous de "Définition de Méthodes" que `Self` est un alias de type pour le type du bloc `impl`, qui dans ce cas est `Pair<T>`). Mais dans le prochain bloc `impl`, `Pair<T>` implémente seulement la méthode `cmp_display` si son type interne `T` implémente le trait `PartialOrd` qui permet la comparaison _et_ le trait `Display` qui permet l'affichage.

Nom de fichier : `src/lib.rs`

```rust
use std::fmt::Display;

struct Pair<T> {
    x: T,
    y: T,
}

impl<T> Pair<T> {
    fn new(x: T, y: T) -> Self {
        Self { x, y }
    }
}

impl<T: Display + PartialOrd> Pair<T> {
    fn cmp_display(&self) {
        if self.x >= self.y {
            println!("The largest member is x = {}", self.x);
        } else {
            println!("The largest member is y = {}", self.y);
        }
    }
}
```

Liste 10-15 : Implémentation conditionnelle de méthodes sur un type générique en fonction des contraintes de trait

Nous pouvons également implémenter un trait conditionnellement pour tout type qui implémente un autre trait. Les implémentations d'un trait sur tout type qui satisfait les contraintes de trait sont appelées _implémentations génériques_ et sont largement utilisées dans la bibliothèque standard de Rust. Par exemple, la bibliothèque standard implémente le trait `ToString` sur tout type qui implémente le trait `Display`. Le bloc `impl` dans la bibliothèque standard ressemble à ce code :

```rust
impl<T: Display> ToString for T {
    --snip--
}
```

En raison de cette implémentation générique dans la bibliothèque standard, nous pouvons appeler la méthode `to_string` définie par le trait `ToString` sur tout type qui implémente le trait `Display`. Par exemple, nous pouvons convertir des entiers en leurs valeurs `String` correspondantes comme ceci car les entiers implémentent `Display` :

```rust
let s = 3.to_string();
```

Les implémentations génériques apparaissent dans la documentation du trait dans la section "Implementeurs".

Les traits et les contraintes de trait nous permettent d'écrire du code qui utilise des paramètres de type générique pour réduire la duplication, mais également de spécifier au compilateur que nous voulons que le type générique ait un comportement particulier. Le compilateur peut ensuite utiliser les informations sur les contraintes de trait pour vérifier que tous les types concret utilisés avec notre code fournissent le bon comportement. Dans les langages à typage dynamique, nous obtiendrions une erreur à l'exécution si nous appelions une méthode sur un type qui n'a pas défini la méthode. Mais Rust déplace ces erreurs au moment de la compilation, de sorte que nous sommes contraints de corriger les problèmes avant même que notre code ne puisse s'exécuter. De plus, nous n'avons pas besoin d'écrire du code qui vérifie le comportement à l'exécution car nous avons déjà vérifié au moment de la compilation. Cela améliore les performances sans avoir à renoncer à la flexibilité des types génériques.
