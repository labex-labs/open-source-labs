# Introduction

Dans ce laboratoire, nous apprenons que les closures peuvent être utilisées comme paramètres d'entrée et également renvoyées comme paramètres de sortie en utilisant `impl Trait` et en spécifiant les traits valides (`Fn`, `FnMut`, `FnOnce`). Le mot clé `move` est utilisé pour indiquer que toutes les captures se produisent par valeur, évitant les références invalides.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
