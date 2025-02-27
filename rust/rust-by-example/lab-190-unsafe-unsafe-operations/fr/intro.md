# Introduction

Dans ce laboratoire, nous allons explorer les opérations non sécurisées en Rust, qui sont utilisées pour contourner les protections du compilateur et sont généralement utilisées pour déréférencer des pointeurs bruts, appeler des fonctions non sécurisées, accéder ou modifier des variables statiques mutables et implémenter des traits non sécurisés. Ces opérations devraient être minimisées dans une base de code pour assurer la sécurité.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
