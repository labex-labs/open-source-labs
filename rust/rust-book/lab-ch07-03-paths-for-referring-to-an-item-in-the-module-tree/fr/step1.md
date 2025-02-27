# Paths for Referring to an Item in the Module Tree

Pour montrer à Rust où trouver un élément dans l'arborescence des modules, nous utilisons un chemin de la même manière que lorsque nous navigons dans un système de fichiers. Pour appeler une fonction, nous devons connaître son chemin.

Un chemin peut prendre deux formes :

- Un _chemin absolu_ est le chemin complet commençant par une racine de crate ; pour le code provenant d'un crate externe, le chemin absolu commence par le nom du crate, et pour le code du crate actuel, il commence par le littéral `crate`.
- Un _chemin relatif_ commence par le module actuel et utilise `self`, `super` ou un identifiant dans le module actuel.

Les chemins absolus et relatifs sont suivis d'un ou plusieurs identifiants séparés par deux points (`::`).

Revoyons la Liste 7-1. Disons que nous voulons appeler la fonction `add_to_waitlist`. C'est comme demander : quel est le chemin de la fonction `add_to_waitlist`? La Liste 7-3 contient la Liste 7-1 avec certains des modules et fonctions supprimés.

Nous montrerons deux façons d'appeler la fonction `add_to_waitlist` à partir d'une nouvelle fonction, `eat_at_restaurant`, définie dans la racine du crate. Ces chemins sont corrects, mais il reste un autre problème qui empêchera cet exemple de compiler tel quel. Nous expliquerons pourquoi un peu plus tard.

La fonction `eat_at_restaurant` est partie de l'API publique de notre crate de bibliothèque, donc nous la marquons avec le mot clé `pub`. Dans "Exposing Paths with the pub Keyword", nous approfondirons le sujet du `pub`.

Nom de fichier : `src/lib.rs`

```rust
mod front_of_house {
    mod hosting {
        fn add_to_waitlist() {}
    }
}

pub fn eat_at_restaurant() {
    // Chemin absolu
    crate::front_of_house::hosting::add_to_waitlist();

    // Chemin relatif
    front_of_house::hosting::add_to_waitlist();
}
```

Liste 7-3 : Appel de la fonction `add_to_waitlist` en utilisant des chemins absolus et relatifs

La première fois que nous appelons la fonction `add_to_waitlist` dans `eat_at_restaurant`, nous utilisons un chemin absolu. La fonction `add_to_waitlist` est définie dans le même crate que `eat_at_restaurant`, ce qui signifie que nous pouvons utiliser le mot clé `crate` pour commencer un chemin absolu. Nous incluons ensuite chacun des modules successifs jusqu'à ce que nous arrivions à `add_to_waitlist`. Vous pouvez imaginer un système de fichiers avec la même structure : nous spécifierions le chemin `/front_of_house/hosting/add_to_waitlist` pour exécuter le programme `add_to_waitlist` ; utiliser le nom du `crate` pour commencer à partir de la racine du crate est comme utiliser `/` pour commencer à partir de la racine du système de fichiers dans votre shell.

La seconde fois que nous appelons `add_to_waitlist` dans `eat_at_restaurant`, nous utilisons un chemin relatif. Le chemin commence par `front_of_house`, le nom du module défini au même niveau de l'arborescence des modules que `eat_at_restaurant`. Ici, l'équivalent dans le système de fichiers serait d'utiliser le chemin `front_of_house/hosting/add_to_waitlist`. Commencer par un nom de module signifie que le chemin est relatif.

Choisir d'utiliser un chemin relatif ou absolu est une décision que vous prendrez en fonction de votre projet, et cela dépend de si vous êtes plus susceptible de déplacer le code de définition d'un élément séparément ou ensemble avec le code qui utilise l'élément. Par exemple, si nous déplacions le module `front_of_house` et la fonction `eat_at_restaurant` dans un module nommé `customer_experience`, nous devrions mettre à jour le chemin absolu vers `add_to_waitlist`, mais le chemin relatif serait toujours valide. Cependant, si nous déplacions la fonction `eat_at_restaurant` séparément dans un module nommé `dining`, le chemin absolu vers l'appel de `add_to_waitlist` resterait le même, mais le chemin relatif devrait être mis à jour. Notre préférence générale est de spécifier des chemins absolus car il est plus probable que nous voulions déplacer les définitions de code et les appels d'éléments indépendamment l'un de l'autre.

Essayons de compiler la Liste 7-3 et trouvons pourquoi elle ne compile pas encore! Les erreurs que nous obtenons sont montrées dans la Liste 7-4.

```bash
$ cargo build
   Compiling restaurant v0.1.0 (file:///projects/restaurant)
error[E0603]: module `hosting` is private
 --> src/lib.rs:9:28
  |
9 |     crate::front_of_house::hosting::add_to_waitlist();
  |                            ^^^^^^^ private module
  |
note: the module `hosting` is defined here
 --> src/lib.rs:2:5
  |
2 |     mod hosting {
  |     ^^^^^^^^^^^

error[E0603]: module `hosting` is private
  --> src/lib.rs:12:21
   |
12 |     front_of_house::hosting::add_to_waitlist();
   |                     ^^^^^^^ private module
   |
note: the module `hosting` is defined here
  --> src/lib.rs:2:5
   |
2  |     mod hosting {
   |     ^^^^^^^^^^^
```

Liste 7-4 : Erreurs du compilateur lors de la construction du code de la Liste 7-3

Les messages d'erreur disent que le module `hosting` est privé. En d'autres termes, nous avons les chemins corrects pour le module `hosting` et la fonction `add_to_waitlist`, mais Rust ne nous permet pas de les utiliser car il n'a pas accès aux parties privées. En Rust, tous les éléments (fonctions, méthodes, structs, enums, modules et constantes) sont privés par défaut pour les modules parents. Si vous voulez rendre un élément tel qu'une fonction ou un struct privé, vous le mettez dans un module.

Les éléments dans un module parent ne peuvent pas utiliser les éléments privés à l'intérieur des modules enfants, mais les éléments dans les modules enfants peuvent utiliser les éléments dans leurs modules ancêtres. C'est parce que les modules enfants enveloppent et cachent leurs détails d'implémentation, mais les modules enfants peuvent voir le contexte dans lequel ils sont définis. Pour continuer avec notre métaphore, imaginez les règles de confidentialité comme étant comme le bureau arrière d'un restaurant : ce qui se passe là-dedans est privé pour les clients du restaurant, mais les gestionnaires de bureau peuvent voir et faire tout dans le restaurant qu'ils gèrent.

Rust a choisi de faire fonctionner le système de modules de cette manière afin que le fait de cacher les détails d'implémentation interne soit la norme. Ainsi, vous savez quelles parties du code interne vous pouvez modifier sans casser le code externe. Cependant, Rust vous donne l'option d'exposer les parties internes du code des modules enfants aux modules ancêtres externes en utilisant le mot clé `pub` pour rendre un élément public.
