# Introduction

Dans ce laboratoire, le concept de dépendances de développement est expliqué. Les dépendances de développement sont ajoutées dans la section `[dev-dependencies]` du fichier `Cargo.toml` et sont utilisées pour les tests, les exemples ou les benchmarks. Un exemple de dépendance de développement est `pretty_assertions`, qui étend les macros standard telles que `assert_eq!` et `assert_ne!` pour fournir des différences colorées.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
