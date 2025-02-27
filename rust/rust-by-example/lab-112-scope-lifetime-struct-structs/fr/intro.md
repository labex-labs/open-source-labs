# Introduction

Dans ce laboratoire, nous avons du code Rust qui démontre l'utilisation des durées de vie dans les structs. Le code inclut une struct appelée `Borrowed` qui contient une référence à un `i32`, et la référence doit exister plus longtemps que la struct elle-même. Il y a également une struct appelée `NamedBorrowed` avec deux références à des `i32`, les deux références doivent exister plus longtemps que la struct. En outre, il y a un enum appelé `Either` qui peut être soit un `i32` soit une référence à un `i32`, et la référence doit exister plus longtemps que l'enum. Enfin, le code crée des instances de ces structs et de cet enum, et imprime leur contenu pour montrer l'utilisation des durées de vie en Rust.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
