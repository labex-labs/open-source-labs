# Décaler des commits vers une nouvelle branche

Pour ce défi, utilisons le référentiel de `https://github.com/labex-labs/git-playground`. Vous avez travaillé sur un projet dans la branche `master`. Vous réalisez que certaines des modifications que vous avez apportées auraient dû être effectuées sur une branche distincte. Vous voulez déplacer ces modifications vers une nouvelle branche appelée `feature`.

## Tâches

1. Accédez au répertoire du référentiel et configurez votre identité GitHub.
2. Basculez sur la branche `master`.
3. Créez un fichier appelé `hello.txt`, ajoutez "hello, world" à celui-ci, ajoutez-le à l'aire de préparation et soumettez-le avec le message "Added hello.txt".
4. Créez une nouvelle branche appelée `feature` sans basculer vers elle.
5. Annulez le dernier commit sur `master`.
6. Vérifiez l'historique des commits sur la branche `master` et l'historique des commits sur la branche `feature` pour vérifier les résultats.

Voici le résultat de l'exécution de `git log`:

```shell
commit 7969ab5d6606e2a40c9fd826c732206b835976e9 (HEAD -> feature)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 20:19:22 2023 +0800

    Added hello.txt
```
