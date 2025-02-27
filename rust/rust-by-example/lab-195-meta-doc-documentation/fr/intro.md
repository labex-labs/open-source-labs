# Introduction

Dans ce laboratoire, vous pouvez utiliser `cargo doc` pour générer la documentation dans `target/doc`. Vous pouvez également utiliser `cargo test` pour exécuter tous les tests, y compris les tests de documentation, et `cargo test --doc` pour n'exécuter que les tests de documentation. Les commentaires de documentation, dénotés par `///`, sont compilés en documentation par `rustdoc` et prennent en charge Markdown. Ces commentaires sont utiles pour documenter le code dans de grands projets. Les attributs de documentation, tels que `inline`, `no_inline` et `hidden`, sont fréquemment utilisés avec `rustdoc`. Rustdoc est largement utilisé par la communauté pour générer de la documentation, y compris les docs de la bibliothèque standard.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
