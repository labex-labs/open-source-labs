# Introduction

Dans ce laboratoire, nous explorons les concepts des traits `From` et `Into` en Rust, qui sont utilisés pour convertir entre différents types. Ces traits sont intrinsèquement liés, avec `Into` étant le réciproque de `From`. Le trait `From` permet à un type de définir comment se créer à partir d'un autre type, permettant une conversion facile entre types. Le trait `Into` appelle automatiquement l'implémentation de `From` si nécessaire. Les deux traits peuvent être implémentés pour des types personnalisés, offrant une flexibilité dans les conversions de type.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
