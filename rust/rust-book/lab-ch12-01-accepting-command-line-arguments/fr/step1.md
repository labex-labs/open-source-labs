# Accepting Command Line Arguments

Créons un nouveau projet avec, comme toujours, `cargo new`. Nous appellerons notre projet `minigrep` pour le distinguer de l'outil `grep` que vous pouvez déjà avoir sur votre système.

```bash
$ cargo new minigrep
     Created binary (application) `minigrep` project
$ cd minigrep
```

La première tâche est de faire en sorte que `minigrep` accepte ses deux arguments de ligne de commande : le chemin du fichier et une chaîne de caractères à rechercher. C'est-à-dire que nous voulons être en mesure d'exécuter notre programme avec `cargo run`, deux tirets pour indiquer que les arguments suivants sont pour notre programme et non pour `cargo`, une chaîne de caractères à rechercher et un chemin vers un fichier dans lequel effectuer la recherche, comme ceci :

```bash
cargo run -- searchstring example-filename.txt
```

En ce moment, le programme généré par `cargo new` ne peut pas traiter les arguments que nous lui donnons. Certaines bibliothèques existantes sur *https://crates.io* peuvent aider à écrire un programme qui accepte des arguments de ligne de commande, mais comme vous apprenez juste ce concept, implémentons cette fonctionnalité nous-mêmes.
