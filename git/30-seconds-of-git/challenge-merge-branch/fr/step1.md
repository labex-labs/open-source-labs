# Fusionner une branche

Votre tâche consiste à fusionner une branche dans la branche actuelle à l'aide de Git. Vous devrez basculer sur la branche cible puis fusionner la branche source dans celle-ci. Cela peut être utile lorsque vous voulez combiner les modifications provenant d'une branche `feature-branch-A` dans la branche `master` de votre projet.

## Tâches

Pour ce défi, utilisons le référentiel de `https://github.com/labex-labs/git-playground`.

1. Accédez au répertoire et configurez l'identité.
2. Créez une branche `feature-branch-A`. Basculez sur elle.
3. Ajoutez "hello,world" au fichier `file2.txt`, ajoutez-le à l'aire de préparation et validez-le avec le message "fix file2.txt".
4. Basculez sur la branche `master`.
5. Fusionnez la branche `feature-branch-A` dans la branche `master`.
6. Résolvez tout conflit qui peut survenir pendant le processus de fusion.

Voici le résultat de l'exécution de `git log`:

```shell
commit e2b80358ae6e4c3b8439cf111a4672a188739290 (HEAD -> master, feature-branch-A)
Author: xiaoshengyunan <xiaoshengyunan@users.noreply.github.com>
Date:   Fri Jul 21 18:51:00 2023 +0800

    fix file2.txt
```
