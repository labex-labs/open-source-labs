# Introduction

Dans ce laboratoire, nous explorons l'utilisation de l'opérateur `?` en Rust, qui permet de déballer facilement les valeurs `Option` sans avoir besoin d'instructions `match` imbriquées. L'opérateur `?` peut être utilisé pour retourner rapidement la valeur sous-jacente si l'`Option` est `Some`, ou terminer la fonction et retourner `None` si l'`Option` est `None`. Cet opérateur peut être chaîné pour rendre le code plus lisible et concise.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
