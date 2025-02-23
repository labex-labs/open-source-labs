# Fusionner une branche et créer un commit de fusion

En tant que développeur, vous devrez peut-être fusionner une branche dans la branche actuelle, en créant un commit de fusion. Cela peut être un peu difficile si vous n'êtes pas familier avec Git. Le problème est de fusionner une branche dans la branche actuelle, en créant un commit de fusion, en utilisant le référentiel Git nommé `https://github.com/labex-labs/git-playground` dans le répertoire.

## Tâches

Pour ce défi, utilisons le référentiel de `https://github.com/labex-labs/git-playground`.

1. Clonez le référentiel, accédez au répertoire et configurez l'identité.
2. Créez et basculez sur une branche appelée `feature-branch`.
3. Ajoutez "Ceci est une nouvelle ligne." au fichier `README.md`, ajoutez-le à la zone de préparation et validez-le, le message de commit est "Ajouter une nouvelle ligne au README.md".
4. Basculez sur la branche `master`.
5. Fusionnez la branche `feature-branch` dans la branche `master`, ce qui créera un commit de fusion avec le message "Fusionner feature-branch".

Voici le résultat de l'exécution de `git log`:

```shell
commit 45b7e0fa8656d0aa751c7ca3cee29422e3d6cf05 (HEAD -> master)
Merge: d22f46b 1f19499
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 19:26:57 2023 +0800

    Merge feature-branch

commit 1f1949955387a154ff1bb5286d3d0a2b993f87e0 (feature-branch)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 19:26:57 2023 +0800

    Add new line to README.md
```
