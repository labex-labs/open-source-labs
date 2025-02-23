# Optimize the Local Repository

Au fil du temps, votre référentiel Git peut se brouiller avec des anciennes versions de fichiers et d'autres données inutiles. Cela peut ralentir Git et rendre plus difficile de travailler avec votre référentiel. Pour optimiser votre référentiel local, vous devez supprimer ces données inutiles.

Lorsque vous exécutez la commande, Git supprimera tous les objets détachés (objets qui ne sont pas référencés par aucune branche ou étiquette) et empaquetera les objets restants dans un nouveau groupe de fichiers de type pack. Cela peut réduire considérablement la taille de votre référentiel et améliorer les performances de Git.

## Tasks

Par exemple, disons que vous avez un référentiel Git nommé `git-playground` situé dans votre répertoire personnel et que vous voulez optimiser ce référentiel.

Voici le résultat de l'optimisation du référentiel `git-playground` en supprimant tous les objets détachés et en empaquetant les objets restants dans un nouveau groupe de fichiers de type pack :

![Optimized Git repository result](../assets/challenge-optimize-repository-step1-1.png)
