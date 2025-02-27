# Introduction

Dans ce laboratoire, nous explorons l'utilisation de types de clés alternatifs/ personnalisés dans le `HashMap` de Rust, qui peut inclure des types qui implémentent les traits `Eq` et `Hash` tels que `bool`, `int`, `uint`, `String` et `&str`. De plus, nous pouvons implémenter ces traits pour des types personnalisés en utilisant l'attribut `#[derive(PartialEq, Eq, Hash)]`, leur permettant d'être utilisés comme clés dans un `HashMap`.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
