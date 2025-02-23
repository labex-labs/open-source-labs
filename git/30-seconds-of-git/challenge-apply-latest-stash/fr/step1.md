# Appliquer le dernier dépôt temporaire

Vous travaillez sur un projet dans votre référentiel Git et avez effectué certaines modifications qui ne sont pas encore prêtes à être validées. Cependant, vous devez passer à une autre branche ou à un autre commit pour travailler sur une autre fonctionnalité. Vous ne voulez pas perdre vos modifications, donc vous décidez de les stocker temporairement. Plus tard, lorsque vous êtes prêt à reprendre le travail sur vos modifications, vous devez appliquer le dernier dépôt temporaire à votre répertoire de travail.

## Tâches

Pour appliquer le dernier dépôt temporaire à votre référentiel Git, suivez ces étapes :

1. Liste de vos dépôts temporaires. Vous devriez voir un dépôt temporaire dans la liste.
2. Appliquez le dernier dépôt temporaire à votre répertoire de travail.
3. Vérifiez le fichier `README.md` pour voir que vos modifications ont été appliquées.

Voici le résultat de l'exécution de la commande `cat README.md` :

![README file changes applied](../assets/challenge-apply-latest-stash-step1-1.png)

Cette commande réapplique les modifications de la dernière sauvegarde au répertoire de travail actuel et ajoute la nouvelle ligne "Ceci est une nouvelle ligne" au fichier `README.md`.
