# Introduction

Dans ce laboratoire, le code montre comment utiliser le type `Box` pour conserver les erreurs originales en les enveloppant, permettant un traitement dynamique des erreurs, et le trait `From` de la bibliothèque `Std` aide à convertir tout type qui implémente le trait `Error` en l'objet trait `Box<Error>`. Il inclut un exemple de conversion et de traitement d'erreurs en utilisant `Box` avec un type d'erreur personnalisé.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
