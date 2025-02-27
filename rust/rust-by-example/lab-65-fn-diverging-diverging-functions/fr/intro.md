# Introduction

Dans ce laboratoire, nous allons étudier les fonctions divergentes qui sont marquées avec `!` en Rust. Les fonctions divergentes ne retournent jamais et leur type de retour est un type vide. Cela est différent du type `()` qui n'a qu'une seule valeur possible. Les fonctions divergentes peuvent être utiles lorsqu'il est nécessaire de convertir en tout autre type, par exemple dans les branches `match`. Elles sont également le type de retour des fonctions qui bouclent à l'infini ou qui terminent le processus.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
