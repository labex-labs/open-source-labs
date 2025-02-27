# Introduction

Dans ce laboratoire, nous explorons l'idiome `newtype`, qui offre des garanties au moment de la compilation en nous permettant de créer un nouveau type distinct de son type sous-jacent. Un exemple est présenté où une structure `Years` est utilisée pour représenter l'âge en années, et une structure `Days` est utilisée pour représenter l'âge en jours. En utilisant l'idiome `newtype`, nous pouvons nous assurer que le bon type de valeur est fourni à un programme, comme dans la fonction de vérification d'âge `old_enough`, qui nécessite une valeur de type `Years`. De plus, nous apprenons à obtenir la valeur d'un `newtype` comme son type sous-jacent en utilisant la syntaxe de tuple ou de décomposition.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
