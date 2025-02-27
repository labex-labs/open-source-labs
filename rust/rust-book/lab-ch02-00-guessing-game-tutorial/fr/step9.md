# Générer un nombre secret

Ensuite, nous devons générer un nombre secret que l'utilisateur tentera de deviner. Le nombre secret devrait être différent à chaque fois pour que le jeu soit amusant à rejouer. Nous utiliserons un nombre aléatoire entre 1 et 100 pour que le jeu ne soit pas trop difficile. Rust n'inclut pas encore de fonctionnalité de génération de nombres aléatoires dans sa bibliothèque standard. Cependant, l'équipe Rust fournit un paquet `rand` sur *https://crates.io/crates/rand* avec cette fonctionnalité.
