# Introduction

Dans ce laboratoire, nous apprenons les déplacements partiels dans la décomposition d'une seule variable, où les liaisons de modèle `by-move` et `by-reference` peuvent être utilisées simultanément. Cela entraîne un déplacement partiel de la variable, permettant à certaines parties d'être déplacées tandis que d'autres peuvent toujours être référencées. Si une variable parent est partiellement déplacée, elle ne peut plus être utilisée dans son ensemble ensuite, mais les parties qui ne sont que référencées et non déplacées peuvent toujours être utilisées.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
