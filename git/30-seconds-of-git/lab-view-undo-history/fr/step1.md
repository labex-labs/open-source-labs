# Consulter l'historique des "annulations"

En tant que développeur, vous pouvez avoir besoin d'annuler des modifications apportées à votre codebase. Git propose plusieurs façons d'annuler des modifications, telles que l'utilisation des commandes `git reset` ou `git revert`. Cependant, il peut être difficile de suivre toutes les actions que vous avez entreprises, en particulier si vous avez utilisé des commandes plus avancées comme `git rebase`. C'est là que la commande `git reflog` s'avère pratique.

La commande `git reflog` affiche le journal des références Git, qui est un enregistrement de toutes les actions que vous avez effectuées dans votre référentiel. Cela inclut non seulement les commits, mais également d'autres actions telles que les fusions de branches, les rebases et les remises à zéro. En consultant le journal des références, vous pouvez voir l'historique complet de toutes les modifications que vous avez apportées à votre référentiel, même si elles ne figurent pas dans l'historique des commits.

Pour consulter l'historique des "annulations" dans Git, vous pouvez utiliser la commande `git reflog`. Disons que vous avez apporté quelques modifications à un référentiel et que vous voulez les annuler.

1. Accédez au référentiel à l'aide de la ligne de commande :

```shell
cd git-playground
```

2. Maintenant, supposons que vous réalisez avoir fait une erreur et que vous voulez annuler le dernier commit. Vous pouvez utiliser la commande `git reset` pour ce faire :

```shell
git reset HEAD~1
```

3. Après avoir exécuté cette commande, vous pouvez vous rendre compte que vous avez fait une autre erreur et que vous voulez annuler le remise à zéro. C'est là que la commande `git reflog` s'avère pratique. Vous pouvez l'utiliser pour consulter le journal des références et trouver le hash du commit précédent :

```shell
git reflog
```

Cela affichera une liste de toutes les actions que vous avez effectuées dans le référentiel, y compris le remise à zéro :

```shell
cf80005 (HEAD -> master) HEAD@{0}: reset: moving to HEAD~1
d22f46b (origin/master, origin/feature-branch, origin/HEAD) HEAD@{1}: clone: from https://github.com/labex-labs/git-playground.git
```

4. A partir de cette sortie, vous pouvez voir que le hash du commit précédent est `d22f46b`. Vous pouvez utiliser ce hash pour remettre le référentiel à l'état du commit précédent :

```shell
git reset d22f46b
```

5. Consultez les enregistrements historiques des commits pour vérifier les résultats :

```shell
git log
```
