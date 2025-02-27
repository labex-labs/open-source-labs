# Introduction

Dans ce laboratoire, nous explorons le concept de paramètres de type fantôme, qui sont des paramètres de type vérifiés statiquement au moment de la compilation et n'ont aucun comportement ou valeur exécutée au moment de l'exécution. Nous démontrons leur utilisation en Rust en combinant `std::marker::PhantomData` avec le concept de paramètres de type fantôme pour créer des tuples et des structs qui contiennent différents types de données.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
