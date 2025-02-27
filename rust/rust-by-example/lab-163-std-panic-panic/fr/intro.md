# Introduction

Dans ce laboratoire, nous étudions la macro `panic!` en Rust, qui peut être utilisée pour générer une panique et commencer à dérouler sa pile, entraînant la sortie du programme en rapportant le message de panique. Le runtime prend soin de libérer toutes les ressources appartenant au fil en appelant le destructeur de ses objets. Nous examinons également un exemple d'utilisation de la macro `panic!` pour gérer la division par zéro et vérifions qu'elle ne résulte pas de fuites mémoire en utilisant Valgrind.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
