# Renommer une branche

En tant que développeur, vous devrez peut-être renommer une branche pour diverses raisons, par exemple pour la rendre plus descriptive ou pour suivre une convention de nommage. Renommer une branche peut être une tâche simple, mais elle nécessite une certaine connaissance des commandes Git. Dans ce défi, vous allez apprendre à renommer une branche à l'aide de Git.

Pour ce laboratoire, nous utiliserons le référentiel Git nommé `https://github.com/labex-labs/git-playground`.

Supposons que vous créiez une branche nommée `old-branch` pour travailler sur une nouvelle fonctionnalité. Après avoir terminé la fonctionnalité, vous constatez que le nom de la branche n'est pas assez descriptif. Vous voulez renommer la branche en `new-branch` pour la rendre plus significative. Pour renommer la branche, suivez ces étapes :

1. Ouvrez le terminal et accédez au répertoire du référentiel local.
2. Utilisez la commande `git checkout -b old-branch` pour créer une branche nommée `old-branch` et utilisez la commande `git branch -m <ancien nom> <nouveau nom>` pour renommer la branche. Dans notre exemple, la commande serait `git branch -m old-branch new-branch`.
3. Vérifiez que la branche a été renommée en utilisant la commande `git branch`.

La sortie devrait montrer le nouveau nom de la branche :

```shell
master
* new-branch
```
