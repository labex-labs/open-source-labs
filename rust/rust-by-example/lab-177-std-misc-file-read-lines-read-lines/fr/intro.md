# Introduction

Dans ce laboratoire, on nous donne une implémentation naive et une implémentation plus efficace pour lire les lignes d'un fichier en Rust. L'approche naive utilise `read_to_string` pour lire le fichier dans une seule chaîne de caractères puis la divise en lignes, tandis que l'approche plus efficace utilise un `BufReader` pour lire le fichier ligne par ligne sans charger tout le contenu en mémoire.

> **Note:** Si le laboratoire ne spécifie pas un nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
