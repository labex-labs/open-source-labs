# Introduction

Dans ce laboratoire, on démontre l'utilisation de `let`-`else` en Rust, où un motif réfutable peut correspondre et lier des variables dans la portée environnante, ou sinon diverger lorsque le motif ne correspond pas en utilisant des instructions telles que `break`, `return` ou `panic!`. Cette construction permet d'avoir un code concis et lisible lorsqu'il s'agit de traiter des scénarios de correspondance de motifs et de gestion d'erreurs, éliminant la nécessité de répéter des blocs de code ou d'utiliser des instructions `let` externes.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
