# Optimize the Local Repository

Au fil du temps, votre référentiel Git peut se brouiller avec des anciennes versions de fichiers et d'autres données inutiles. Cela peut ralentir Git et rendre plus difficile de travailler avec votre référentiel. Pour optimiser votre référentiel local, vous devez supprimer ces données inutiles. Cela peut être fait en utilisant la commande `git gc`.

La commande `git gc` signifie "Git garbage collector" (ramasse-miettes Git en français). Elle est utilisée pour nettoyer les données inutiles dans votre référentiel. Lorsque vous exécutez `git gc`, Git supprimera tous les objets détachés (objets qui ne sont pas référencés par aucune branche ou étiquette) et empaquetera les objets restants dans un nouveau groupe de fichiers de paquet. Cela peut réduire considérablement la taille de votre référentiel et améliorer les performances de Git.

Pour optimiser le référentiel local, vous pouvez utiliser la commande `git gc` avec les options `--prune=now` et `--aggressive`. Par exemple, disons que vous avez un référentiel Git nommé `git-playground` situé dans votre répertoire personnel. Pour optimiser ce référentiel, vous exécuteriez la commande suivante :

```shell
cd git-playground
git gc --prune=now --aggressive
```

Voici le résultat de l'optimisation du référentiel `git-playground` en supprimant tous les objets détachés et en empaquetant les objets restants dans un nouveau groupe de fichiers de paquet :

![Git repository optimization result](../assets/challenge-optimize-repository-step1-1.png)
