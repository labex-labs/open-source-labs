# Introduction

Dans ce laboratoire, nous avons un exemple d'analyse d'arguments en utilisant la correspondance de motifs en Rust. Le programme prend des arguments de ligne de commande et effectue différentes opérations en fonction du nombre et du type d'arguments passés. Si aucun argument n'est passé, il affiche un message. Si un seul argument est passé et qu'il peut être analysé comme l'entier 42, il affiche "This is the answer!". Si une commande et un argument entier sont passés, il effectue une opération d'augmentation ou de diminution sur l'entier. Si un nombre quelconque d'autres arguments est passé, il affiche un message d'aide expliquant la bonne utilisation du programme.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
