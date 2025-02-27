# Exposing Paths with the pub Keyword

Revoyons l'erreur de la Liste 7-4 qui nous a dit que le module `hosting` est privé. Nous voulons que la fonction `eat_at_restaurant` dans le module parent ait accès à la fonction `add_to_waitlist` dans le module enfant, donc nous marquons le module `hosting` avec le mot clé `pub`, comme montré dans la Liste 7-5.

Nom de fichier : `src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        fn add_to_waitlist() {}
    }
}

--snip--
```

Liste 7-5 : Décaration du module `hosting` comme `pub` pour l'utiliser à partir de `eat_at_restaurant`

Malheureusement, le code de la Liste 7-5 entraîne toujours des erreurs de compilation, comme montré dans la Liste 7-6.

```bash
$ cargo build
   Compiling restaurant v0.1.0 (file:///projects/restaurant)
error[E0603]: function `add_to_waitlist` is private
 --> src/lib.rs:9:37
  |
9 |     crate::front_of_house::hosting::add_to_waitlist();
  |                                     ^^^^^^^^^^^^^^^ private function
  |
note: the function `add_to_waitlist` is defined here
 --> src/lib.rs:3:9
  |
3 |         fn add_to_waitlist() {}
  |         ^^^^^^^^^^^^^^^^^^^^

error[E0603]: function `add_to_waitlist` is private
  --> src/lib.rs:12:30
   |
12 |     front_of_house::hosting::add_to_waitlist();
   |                              ^^^^^^^^^^^^^^^ private function
   |
note: the function `add_to_waitlist` is defined here
  --> src/lib.rs:3:9
   |
3  |         fn add_to_waitlist() {}
   |         ^^^^^^^^^^^^^^^^^^^^
```

Liste 7-6 : Erreurs du compilateur lors de la construction du code de la Liste 7-5

Qu'est-ce qui s'est passé? Ajouter le mot clé `pub` devant `mod hosting` rend le module public. Avec ce changement, si nous pouvons accéder à `front_of_house`, nous pouvons accéder à `hosting`. Mais les _contenus_ de `hosting` restent privés ; rendre le module public ne rend pas ses contenus publics. Le mot clé `pub` sur un module permet seulement au code dans ses modules ancêtres de se référer à lui, pas d'accéder à son code interne. Comme les modules sont des conteneurs, il n'y a pas grand-chose que nous puissions faire en ne rendant que le module public ; nous devons aller plus loin et choisir de rendre public un ou plusieurs des éléments à l'intérieur du module également.

Les erreurs de la Liste 7-6 disent que la fonction `add_to_waitlist` est privée. Les règles de confidentialité s'appliquent aux structs, enums, fonctions, méthodes ainsi qu'aux modules.

Rendons également la fonction `add_to_waitlist` publique en ajoutant le mot clé `pub` avant sa définition, comme dans la Liste 7-7.

Nom de fichier : `src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

--snip--
```

Liste 7-7 : Ajout du mot clé `pub` à `mod hosting` et `fn add_to_waitlist` nous permet d'appeler la fonction à partir de `eat_at_restaurant`.

Maintenant, le code compilera! Pour voir pourquoi ajouter le mot clé `pub` nous permet d'utiliser ces chemins dans `add_to_waitlist` par rapport aux règles de confidentialité, regardons les chemins absolus et relatifs.

Dans le chemin absolu, nous commençons par `crate`, la racine de l'arborescence de modules de notre crate. Le module `front_of_house` est défini dans la racine du crate. Bien que `front_of_house` ne soit pas public, puisque la fonction `eat_at_restaurant` est définie dans le même module que `front_of_house` (c'est-à-dire que `eat_at_restaurant` et `front_of_house` sont des frères), nous pouvons nous référer à `front_of_house` à partir de `eat_at_restaurant`. Ensuite vient le module `hosting` marqué avec `pub`. Nous pouvons accéder au module parent de `hosting`, donc nous pouvons accéder à `hosting`. Enfin, la fonction `add_to_waitlist` est marquée avec `pub` et nous pouvons accéder à son module parent, donc cet appel de fonction fonctionne!

Dans le chemin relatif, la logique est la même que pour le chemin absolu, sauf pour la première étape : au lieu de commencer à partir de la racine du crate, le chemin commence par `front_of_house`. Le module `front_of_house` est défini dans le même module que `eat_at_restaurant`, donc le chemin relatif commençant par le module dans lequel `eat_at_restaurant` est définie fonctionne. Ensuite, puisque `hosting` et `add_to_waitlist` sont marqués avec `pub`, le reste du chemin fonctionne, et cet appel de fonction est valide!

Si vous prévoyez de partager votre crate de bibliothèque afin que d'autres projets puissent utiliser votre code, votre API publique est votre contrat avec les utilisateurs de votre crate qui détermine la manière dont ils peuvent interagir avec votre code. Il y a de nombreuses considérations autour de la gestion des modifications de votre API publique pour faciliter la dépendance des gens à votre crate. Ces considérations sont en dehors des limites de ce livre ; si vous êtes intéressé par ce sujet, consultez les Rust API Guidelines à *https://rust-lang.github.io/api-guidelines*.

> **Best Practices for Packages with a Binary and a Library**
>
> Nous avons mentionné qu'un package peut contenir à la fois une racine de crate binaire `src/main.rs` ainsi qu'une racine de crate de bibliothèque `src/lib.rs`, et que les deux crates auront le nom du package par défaut. En général, les packages avec ce modèle de conteneur à la fois une bibliothèque et une crate binaire auront assez de code dans la crate binaire pour démarrer un exécutable qui appelle du code avec la crate de bibliothèque. Cela permet à d'autres projets de profiter de la plupart des fonctionnalités que le package offre car le code de la crate de bibliothèque peut être partagé.
>
> L'arborescence de modules devrait être définie dans `src/lib.rs`. Ensuite, tout élément public peut être utilisé dans la crate binaire en commençant les chemins par le nom du package. La crate binaire devient un utilisateur de la crate de bibliothèque tout comme une crate complètement externe utiliserait la crate de bibliothèque : elle ne peut utiliser que l'API publique. Cela vous aide à concevoir une bonne API ; non seulement êtes-vous l'auteur, vous êtes également un client!
>
> Dans le Chapitre 12, nous démontrerons cette pratique d'organisation avec un programme de ligne de commande qui contiendra à la fois une crate binaire et une crate de bibliothèque.
