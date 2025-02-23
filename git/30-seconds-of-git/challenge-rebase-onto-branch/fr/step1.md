# Rebase sur une autre branche

En tant que développeur, vous travaillez sur un projet avec plusieurs branches. Vous avez apporté des modifications à votre branche et souhaitez incorporer ces modifications dans une autre branche. Cependant, vous ne voulez pas fusionner les branches car vous voulez maintenir une historique propre et linéaire.

## Tâches

Pour ce défi, utilisons le référentiel de `https://github.com/labex-labs/git-playground`.

1. Accédez au répertoire et configurez l'identité.
2. Créez et basculez sur une branche appelée `one-branch`.
3. Ajoutez "hello,world" au fichier `README.md`, ajoutez-le à la zone de préparation et validez-le avec le message "Added some changes to README.md".
4. Basculez sur la branche `master`.
5. Assurez-vous que votre branche locale `master` est à jour avec le référentiel distant.
6. Rebasez la branche `one-branch` sur la branche `master`.
7. Résolvez tout conflit qui se produit pendant le processus de rebase.

Voici le résultat de l'exécution de `git log`:

```shell
commit eccff423dd6bf5335f76f2f364fa3b95130ff805 (HEAD -> master, one-branch)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Sat Jul 22 23:10:04 2023 +0800

    Added some changes to README.md
```
