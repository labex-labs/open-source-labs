# Introduction

Dans ce laboratoire, nous allons apprendre les liaisons de variables, leur portée et le concept d'ombrage en Rust. Les liaisons de variables sont limitées à un bloc, qui est une collection d'instructions entourées de parenthèses. Deux exemples sont fournis pour illustrer ces concepts. Le premier exemple montre comment une liaison de variable déclarée à l'intérieur d'un bloc est limitée à la portée de ce bloc et n'est pas accessible en dehors de celui-ci. Le second exemple démontre l'ombrage de variables, où une nouvelle liaison avec le même nom est déclarée à l'intérieur d'un bloc, ombrageant ainsi effectivement la liaison externe.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
