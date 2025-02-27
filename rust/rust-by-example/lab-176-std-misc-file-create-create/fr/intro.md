# Introduction

Dans ce laboratoire, nous avons une fonction `create` qui ouvre un fichier en mode écriture seule. Elle crée soit un nouveau fichier, soit détruit le contenu ancien si le fichier existe déjà. La fonction utilise la bibliothèque standard de Rust pour gérer les opérations de fichier. L'exemple fourni montre comment utiliser la fonction `create` pour écrire le contenu d'une chaîne statique `LOREM_IPSUM` dans un fichier nommé "lorem_ipsum.txt". La sortie montre une confirmation d'opération d'écriture réussie, et le contenu du fichier est affiché en utilisant la commande `cat`.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
