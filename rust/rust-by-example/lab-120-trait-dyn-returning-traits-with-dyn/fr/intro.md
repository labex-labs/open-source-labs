# Introduction

Dans ce laboratoire, nous apprenons comment contourner la limitation de retourner directement des traits en Rust en utilisant le type `Box<dyn Animal>`, qui permet à des fonctions de retourner une référence à un objet alloué sur le tas qui implémente le trait `Animal`.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
