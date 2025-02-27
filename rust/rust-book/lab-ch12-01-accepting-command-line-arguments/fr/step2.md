# Reading the Argument Values

Pour permettre à `minigrep` de lire les valeurs des arguments de ligne de commande que nous lui passons, nous aurons besoin de la fonction `std::env::args` fournie dans la bibliothèque standard de Rust. Cette fonction renvoie un itérateur des arguments de ligne de commande passés à `minigrep`. Nous aborderons les itérateurs en détail au chapitre 13. Pour l'instant, vous n'avez besoin de connaître que deux détails sur les itérateurs : les itérateurs produisent une série de valeurs, et nous pouvons appeler la méthode `collect` sur un itérateur pour le transformer en une collection, telle qu'un vecteur, qui contient tous les éléments produits par l'itérateur.

Le code de la liste 12-1 permet à votre programme `minigrep` de lire tous les arguments de ligne de commande passés à celui-ci, puis de collecter les valeurs dans un vecteur.

Nom de fichier : `src/main.rs`

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    dbg!(args);
}
```

Liste 12-1 : Collecter les arguments de ligne de commande dans un vecteur et les imprimer

Tout d'abord, nous importons le module `std::env` dans la portée avec une instruction `use` pour pouvoir utiliser sa fonction `args`. Remarquez que la fonction `std::env::args` est imbriquée dans deux niveaux de modules. Comme nous l'avons discuté au chapitre 7, dans les cas où la fonction souhaitée est imbriquée dans plus d'un module, nous avons choisi d'importer le module parent dans la portée plutôt que la fonction. En faisant ainsi, nous pouvons facilement utiliser d'autres fonctions de `std::env`. Cela est également moins ambigu que d'ajouter `use std::env::args` puis d'appeler la fonction avec seulement `args`, car `args` pourrait facilement être confondu avec une fonction définie dans le module actuel.

> **La fonction args et l'Unicode invalide**
>
> Notez que `std::env::args` provoquera une panique si un argument contient un Unicode invalide. Si votre programme doit accepter des arguments contenant un Unicode invalide, utilisez `std::env::args_os` à la place. Cette fonction renvoie un itérateur qui produit des valeurs `OsString` au lieu de `String` valeurs. Nous avons choisi d'utiliser `std::env::args` ici pour la simplicité car les valeurs `OsString` diffèrent selon la plateforme et sont plus complexes à manipuler que les valeurs `String`.

Sur la première ligne de `main`, nous appelons `env::args`, et nous utilisons immédiatement `collect` pour transformer l'itérateur en un vecteur contenant toutes les valeurs produites par l'itérateur. Nous pouvons utiliser la fonction `collect` pour créer de nombreux types de collections, donc nous annotons explicitement le type de `args` pour spécifier que nous voulons un vecteur de chaînes de caractères. Bien que vous ayez très rarement besoin d'annoter les types en Rust, `collect` est une fonction pour laquelle vous devez souvent annoter le type car Rust n'est pas capable d'inférer le type de collection que vous voulez.

Enfin, nous imprimons le vecteur à l'aide de la macro de débogage. Essayons d'exécuter le code d'abord sans arguments puis avec deux arguments :

```bash
$ cargo run
--snip--
[src/main.rs:5] args = [
"target/debug/minigrep",
]
$ cargo run -- needle haystack
--snip--
[src/main.rs:5] args = [
"target/debug/minigrep",
"needle",
"haystack",
]
```

Remarquez que la première valeur dans le vecteur est `"target/debug/minigrep"`, qui est le nom de notre binaire. Cela correspond au comportement de la liste d'arguments en C, permettant aux programmes d'utiliser le nom sous lequel ils ont été invoqués dans leur exécution. Il est souvent pratique d'avoir accès au nom du programme au cas où vous voudriez l'imprimer dans des messages ou changer le comportement du programme en fonction de l'alias de ligne de commande utilisé pour invoquer le programme. Mais dans le cadre de ce chapitre, nous allons l'ignorer et ne conserver que les deux arguments dont nous avons besoin.
