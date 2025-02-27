# Introduction

Dans ce laboratoire, nous allons explorer le type `Result` en Rust, qui fournit un moyen de gérer les erreurs potentielles au lieu de la possible absence d'une valeur comme le type `Option`. Le type `Result` peut avoir deux issues - `Ok(T)` pour un résultat réussi avec l'élément `T`, et `Err(E)` pour une erreur avec l'élément `E`. Nous verrons comment utiliser `Result` dans des exemples de code et comment il peut être utilisé comme type de retour de la fonction `main` pour gérer les erreurs et fournir un message d'erreur plus spécifique.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
