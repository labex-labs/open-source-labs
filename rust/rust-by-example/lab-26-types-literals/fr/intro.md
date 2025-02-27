# Introduction

Dans ce laboratoire, nous apprenons les littéraux en Rust et comment spécifier leur type en ajoutant un suffixe. Les littéraux suffixés ont leur type connu lors de l'initialisation, tandis que les types des littéraux non suffixés dépendent de la manière dont ils sont utilisés. La fonction `size_of_val` est utilisée pour déterminer la taille d'une variable en octets, et elle est appelée avec son chemin complet, `std::mem::size_of_val`. La fonction `size_of_val` est définie dans le module `mem`, qui est lui-même défini dans la boîte à outils `std`.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
