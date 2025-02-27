# Separation of Concerns for Binary Projects

Le problème organisationnel consistant à attribuer la responsabilité de plusieurs tâches à la fonction `main` est courant dans de nombreux projets binaires. En conséquence, la communauté Rust a élaboré des directives pour diviser les préoccupations distinctes d'un programme binaire lorsque `main` commence à devenir volumineux. Ce processus comporte les étapes suivantes :

- Divisez votre programme en un fichier `main.rs` et un fichier `lib.rs` et déplacez la logique de votre programme vers `lib.rs`.
- Tant que votre logique d'analyse des arguments de ligne de commande est simple, elle peut rester dans `main.rs`.
- Lorsque la logique d'analyse des arguments de ligne de commande commence à devenir complexe, extraire-la de `main.rs` et la déplacer vers `lib.rs`.

Les responsabilités qui restent dans la fonction `main` après ce processus devraient être limitées aux suivantes :

- Appeler la logique d'analyse des arguments de ligne de commande avec les valeurs des arguments
- Configurer tout autre paramètre
- Appeler une fonction `run` dans `lib.rs`
- Gérer l'erreur si `run` renvoie une erreur

Ce modèle consiste à séparer les préoccupations : `main.rs` gère l'exécution du programme et `lib.rs` gère toute la logique de la tâche en cours. Étant donné que vous ne pouvez pas tester directement la fonction `main`, cette structure vous permet de tester toute la logique de votre programme en la déplaçant dans des fonctions de `lib.rs`. Le code qui reste dans `main.rs` sera suffisamment simple pour vérifier sa correction en le lisant. Modifions notre programme en suivant ce processus.
