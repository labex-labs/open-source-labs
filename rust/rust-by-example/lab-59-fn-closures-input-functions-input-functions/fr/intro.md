# Introduction

Dans ce laboratoire, vous allez apprendre comment les fonctions peuvent prendre des closures comme paramètres, permettant à toute fonction qui satisfait la contrainte de trait de la closure d'être utilisée comme argument. Les traits `Fn`, `FnMut` et `FnOnce` déterminent la manière dont une closure capture les variables du scope entourant.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
