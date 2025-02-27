# Introduction

Dans ce laboratoire, vous allez découvrir l'attribut `cfg` et le macro `cfg!` en Rust, qui permettent respectivement des vérifications conditionnelles dans la configuration et l'évaluation. L'attribut `cfg` active la compilation conditionnelle, tandis que le macro `cfg!` évalue à vrai ou faux au moment de l'exécution. Les blocs de code utilisant `cfg!` doivent être valides indépendamment du résultat de l'évaluation, contrairement à `#[cfg]` qui peut supprimer du code.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
