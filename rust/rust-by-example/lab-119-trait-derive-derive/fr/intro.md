# Introduction

Dans ce laboratoire, nous allons découvrir l'attribut `#[derive]` en Rust, qui permet au compilateur de fournir des implémentations de base pour certains traits tels que `Eq`, `PartialEq`, `Ord`, `PartialOrd`, `Clone`, `Copy`, `Hash`, `Default` et `Debug`. Ces traits peuvent également être implémentés manuellement si un comportement plus complexe est nécessaire. Le laboratoire fournit un code exemple montrant l'utilisation de ces traits sur différents structs tuple tels que `Centimeters`, `Inches` et `Seconds`.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
