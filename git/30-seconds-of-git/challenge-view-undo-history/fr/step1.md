# Consulter l'historique des annulations

En tant que développeur, vous pouvez avoir besoin d'annuler des modifications apportées à votre base de code. Git propose plusieurs façons d'annuler des modifications, telles que l'utilisation des commandes `git reset` ou `git revert`. Cependant, il peut être difficile de suivre toutes les actions que vous avez entreprises, en particulier si vous avez utilisé des commandes plus avancées comme `git rebase`.

## Tâches

Disons que vous avez apporté quelques modifications à un référentiel et que vous voulez les annuler.

1. Accédez au référentiel.
2. Maintenant, vous réalisez que vous avez commis une erreur et que vous voulez annuler le dernier commit.
3. Vous pouvez vous rendre compte que vous avez commis une autre erreur et que vous voulez annuler le reset. Consultez le journal de référence et trouvez le hash du commit précédent.
4. Vous constatez que le hash du commit précédent est `d22f46b` et utilisez ce hash pour remettre le référentiel à l'état du commit précédent.
5. Consultez les enregistrements historiques de commits pour vérifier les résultats.

Voici le résultat de l'étape 3. Cela affichera une liste de toutes les actions que vous avez entreprises dans le référentiel, y compris le reset :

```shell
cf80005 (HEAD -> master) HEAD@{0}: reset: moving to HEAD~1
d22f46b (origin/master, origin/feature-branch, origin/HEAD) HEAD@{1}: clone: from https://github.com/labex-labs/git-playground.git
```
