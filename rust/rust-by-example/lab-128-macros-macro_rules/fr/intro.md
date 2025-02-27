# Introduction

Dans ce laboratoire, nous allons explorer le puissant système de macros fourni par Rust, qui permet la métaprogrammation en étendant les macros en arbres syntaxiques abstraits. Le macro `macro_rules!` est utilisé pour créer des macros, et elles sont distinguées des fonctions par leur terminaison bang `!`. Les macros sont utiles pour éviter la répétition de code, créer des langages spécifiques au domaine et définir des interfaces variadiques pour les fonctions qui peuvent prendre un nombre variable d'arguments.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
