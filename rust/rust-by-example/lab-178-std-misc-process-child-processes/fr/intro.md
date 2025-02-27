# Introduction

Dans ce laboratoire, nous apprenons à utiliser les processus enfants en Rust en utilisant la structure `process::Output` pour représenter la sortie d'un processus enfant terminé et la structure `process::Command` pour construire des processus. Le code d'exemple montre comment exécuter la commande `rustc --version` et gérer la sortie en vérifiant si le processus a réussi ou échoué.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
