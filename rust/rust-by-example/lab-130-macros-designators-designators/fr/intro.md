# Introduction

Dans ce laboratoire, nous sommes introduits au concept de désignateurs dans les macros Rust. Les désignateurs sont utilisés pour préfixer les arguments d'une macro et sont annotés avec un type. Certains exemples de désignateurs incluent `ident` pour les noms de variables / fonctions, `expr` pour les expressions, `block` pour les blocs de code et `pat` pour les motifs. Ces désignateurs sont utilisés dans les règles de macro pour générer du code en fonction des arguments fournis.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
