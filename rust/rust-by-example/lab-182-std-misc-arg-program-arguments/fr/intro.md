# Introduction

Dans ce laboratoire, vous pouvez accéder aux arguments de ligne de commande en Rust en utilisant la fonction `std::env::args`, qui renvoie un itérateur qui produit une `String` pour chaque argument. Le premier argument dans le vecteur renvoyé est le chemin utilisé pour appeler le programme, tandis que le reste des arguments sont les paramètres de ligne de commande. Alternativement, vous pouvez utiliser des crânes comme `clap` pour une gestion plus avancée des arguments de ligne de commande.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
