# Introduction

Dans ce laboratoire, la principale manière de documenter un projet Rust consiste à annoter le code source avec des commentaires de documentation, qui sont écrits selon la spécification CommonMark Markdown et prennent en charge les blocs de code à l'intérieur. Rust s'occupe de la correction et ces blocs de code sont compilés et utilisés comme tests de documentation. Ces tests sont exécutés automatiquement lors de l'utilisation de la commande `cargo test`. La motivation derrière les tests de documentation est de servir d'exemples qui mettent en œuvre la fonctionnalité et permettent d'utiliser les exemples de la documentation comme extraits de code complets.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
