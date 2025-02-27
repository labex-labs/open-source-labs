# Introduction

Dans ce laboratoire, l'approche alternative consistant à encapsuler les erreurs dans un type d'erreur personnalisé est démontrée. L'exemple de code montre comment définir un alias de type `Result` qui utilise l'énumération `DoubleError` comme variant d'erreur, qui encapsule l'`ParseIntError` de la bibliothèque standard. En implémentant les traits `fmt::Display`, `error::Error` et `From`, le type d'erreur personnalisé peut fournir des informations supplémentaires et gérer les erreurs sous-jacentes.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
