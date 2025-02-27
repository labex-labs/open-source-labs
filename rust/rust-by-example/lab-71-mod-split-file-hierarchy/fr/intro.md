# Introduction

Dans ce laboratoire, la hiérarchie de fichiers des modules dans l'exemple de code peut être représentée comme suit : Il existe un répertoire nommé "my" qui contient deux fichiers, "inaccessible.rs" et "nested.rs". De plus, il existe un fichier nommé "my.rs" et un fichier nommé "split.rs". Le fichier "split.rs" inclut le module "my" qui est défini dans le fichier "my.rs", et le fichier "my.rs" inclut les modules "inaccessible" et "nested" qui sont définis respectivement dans les fichiers "inaccessible.rs" et "nested.rs".

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
