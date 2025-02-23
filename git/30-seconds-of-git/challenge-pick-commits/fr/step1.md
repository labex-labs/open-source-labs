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
commit e2f3c6af9570f4eac2580dea93ca8133f1547d53 (HEAD -> master)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Sat Jul 15 14:30:31 2023 +0800

    add hello.txt

commit d22f46ba8c2d4e07d773c5126e9c803933eb5898 (origin/master, origin/HEAD)
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt

commit cf80005e40a3c661eb212fcea5fad06f8283f08f
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file1.txt

commit b00b9374a7c549d1af111aa777fdcc868d8a2a01
Author: Hang <huhuhang@gmail.com>
Date:   Wed Apr 26 14:16:00 2023 +0800

    Initial commit
```
