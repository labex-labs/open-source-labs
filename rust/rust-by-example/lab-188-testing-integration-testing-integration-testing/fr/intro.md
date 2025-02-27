# Introduction

Dans ce laboratoire, les tests d'intégration sont abordés, qui consistent à tester plusieurs parties d'une bibliothèque ensemble en utilisant son interface publique. Les tests d'intégration peuvent être placés dans le répertoire `tests` à côté du répertoire `src` dans une boîte à outils Rust, et sont exécutés en utilisant la commande `cargo test`. De plus, le code commun peut être partagé entre les tests d'intégration en créant un module avec des fonctions publiques et en l'import ant dans les tests.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
