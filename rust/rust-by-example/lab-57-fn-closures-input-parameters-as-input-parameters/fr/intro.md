# Introduction

Dans ce laboratoire, nous apprenons qu'en écrivant des fonctions en Rust qui prennent une closure en tant que paramètre d'entrée, le type complet de la closure doit être annoté à l'aide d'un des `traits` : `Fn`, `FnMut` ou `FnOnce`, qui déterminent comment la closure utilise la valeur capturée, soit par référence, référence mutable ou valeur. Le compilateur capture les variables de la manière la moins restrictive possible en fonction du trait choisi pour la closure.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
