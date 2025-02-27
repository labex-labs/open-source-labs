# Introduction

Dans ce laboratoire, nous avons un extrait de code en Rust qui montre comment créer des threads natifs du système d'exploitation à l'aide de la fonction `spawn` et d'une closure mobile. Le code crée un vecteur pour stocker les threads créés, itère sur une plage de nombres pour créer plusieurs threads et imprime un message identifiant chaque numéro de thread. Enfin, le thread principal attend que chaque thread créé se termine à l'aide de la fonction `join`.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
