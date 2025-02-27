# Introduction

Dans ce laboratoire, nous apprenons les bornes en Rust, qui sont utilisées pour restreindre les durées de vie ou les traits des types génériques. Le caractère `:` est utilisé pour indiquer que toutes les références dans un type doivent avoir une durée de vie supérieure à une certaine durée de vie, tandis que `+` est utilisé pour indiquer qu'un type doit implémenter un trait et que toutes les références dans ce type doivent avoir une durée de vie supérieure à une certaine durée de vie. Un extrait de code exemple montre la syntaxe et l'utilisation des bornes en Rust.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
