# Introduction

Dans ce laboratoire, nous explorons le concept de types associés en Rust, qui permet d'améliorer la lisibilité du code en définissant des types internes localement dans un trait en tant que types de sortie. Cela est réalisé en utilisant le mot clé `type` à l'intérieur de la définition du trait. Avec les types associés, les fonctions qui utilisent le trait n'ont plus besoin d'exprimer explicitement les types `A` et `B`, rendant le code plus concis et flexible. Nous réécrivons un exemple d'une section précédente en utilisant des types associés pour illustrer leur utilisation en pratique.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
