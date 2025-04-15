# Git Cherry-Pick

En tant que développeur, vous travaillez sur un projet avec plusieurs branches. Vous avez identifié une modification spécifique qui a été faite dans un commit précédent que vous souhaitez appliquer à votre branche actuelle. Cependant, vous ne voulez pas fusionner toute la branche car elle contient d'autres modifications que vous n'avez pas besoin.

## Tâches

Pour ce défi, utilisons le référentiel de `https://github.com/labex-labs/git-playground`.

1. Accédez au répertoire et configurez l'identité.
2. Créez et basculez sur une branche appelée `one-branch`, créez un fichier appelé `hello.txt`, écrivez "hello,world" dedans, ajoutez-le à la zone de préparation et validez-le avec le message "add hello.txt".
3. Identifiez le hash du commit créé dans l'étape précédente à appliquer à la branche `master`.
4. Basculez sur la branche `master` et appliquez la modification à la branche `master`.
5. Vérifiez que la modification a été appliquée à la branche `master`.

Voici le résultat de l'exécution de `git log` sur la branche `master`:

```shell
ADD hello.txt
```
