# Commenter les éléments inclus

Le commentaire de documentation `//!` ajoute de la documentation à l'élément qui _contient_ les commentaires plutôt qu'aux éléments _suivant_ les commentaires. Nous utilisons généralement ces commentaires de documentation dans le fichier racine de la boîte à outils (crate) (`src/lib.rs` par convention) ou à l'intérieur d'un module pour documenter la boîte à outils ou le module dans son ensemble.

Par exemple, pour ajouter de la documentation qui décrit le but de la boîte à outils (crate) `my_crate` qui contient la fonction `add_one`, nous ajoutons des commentaires de documentation commençant par `//!` au début du fichier `src/lib.rs`, comme montré dans la liste 14-2.

Nom du fichier : `src/lib.rs`

```rust
//! # Ma boîte à outils (My Crate)
//!
//! `my_crate` est une collection d'utilitaires pour faciliter
//! la réalisation de certains calculs.

/// Ajoute un à un nombre donné.
--snip--
```

Liste 14-2 : Documentation pour la boîte à outils (crate) `my_crate` dans son ensemble

Remarquez qu'il n'y a pas de code après la dernière ligne commençant par `//!`. Parce que nous avons commencé les commentaires par `//!` au lieu de `///`, nous documentons l'élément qui contient ce commentaire plutôt qu'un élément qui suit ce commentaire. Dans ce cas, cet élément est le fichier `src/lib.rs`, qui est la racine de la boîte à outils. Ces commentaires décrivent l'ensemble de la boîte à outils.

Lorsque nous exécutons `cargo doc --open`, ces commentaires seront affichés sur la page d'accueil de la documentation de `my_crate` au-dessus de la liste des éléments publics de la boîte à outils, comme montré dans la figure 14-2.

Figure 14-2 : Documentation rendue pour `my_crate`, y compris le commentaire décrivant l'ensemble de la boîte à outils

Les commentaires de documentation à l'intérieur des éléments sont utiles pour décrire les boîtes à outils et les modules en particulier. Utilisez-les pour expliquer le but général du conteneur afin d'aider vos utilisateurs à comprendre l'organisation de la boîte à outils.
