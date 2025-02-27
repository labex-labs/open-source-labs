# Introduction

Dans ce laboratoire, nous avons une implémentation d'une liste chaînée en utilisant des `enums` en Rust. L'`enum` `List` a deux variantes : `Cons`, qui représente un nœud avec un élément et un pointeur vers le nœud suivant, et `Nil`, qui signifie la fin de la liste chaînée. L'`enum` a des méthodes telles que `new` pour créer une liste vide, `prepend` pour ajouter un élément au début de la liste, `len` pour retourner la longueur de la liste, et `stringify` pour retourner une représentation sous forme de chaîne de caractères de la liste. La fonction `main` fournie démontre l'utilisation de ces méthodes pour créer et manipuler une liste chaînée.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
