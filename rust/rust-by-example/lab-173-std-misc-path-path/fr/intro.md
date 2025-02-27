# Introduction

Dans ce laboratoire, nous allons explorer la structure `Path` en Rust, qui représente les chemins de fichiers dans le système de fichiers sous-jacent. Elle existe en deux variantes : `posix::Path` pour les systèmes UNIX et `windows::Path` pour Windows. Le `Path` peut être créé à partir d'un `OsStr` et fournit diverses méthodes pour récupérer des informations sur le fichier ou le répertoire auquel le chemin pointe. Il est important de noter qu'un `Path` est immuable, et sa version propriétaire est appelée `PathBuf`, qui peut être modifiée in situ. La relation entre `Path` et `PathBuf` est similaire à celle entre `str` et `String`.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
