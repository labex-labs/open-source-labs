# Git Cherry-Pick

En tant que développeur, vous travaillez sur un projet avec plusieurs branches. Vous avez identifié une modification spécifique qui a été effectuée dans un commit précédent que vous souhaitez appliquer à votre branche actuelle. Cependant, vous ne voulez pas fusionner toute la branche car elle contient d'autres modifications que vous n'avez pas besoin. Dans ce scénario, vous pouvez utiliser la commande `git cherry-pick` pour appliquer la modification spécifique à votre branche actuelle.

Pour ce laboratoire, utilisons le dépôt de `https://github.com/labex-labs/git-playground`. Suivez les étapes ci-dessous pour terminer le défi :

1. Clonez le dépôt, accédez au répertoire et configurez votre identité :

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Créez et basculez sur une branche appelée `one-branch`, créez un fichier appelé `hello.txt`, écrivez "hello,world" dedans, ajoutez-le à la zone de préparation et validez-le avec le message "add hello.txt" :

```shell
git checkout -b one-branch
echo "hello,world" > hello.txt
git add.
git commit -m "add hello.txt"
```

3. Identifiez le hash du commit créé à l'étape précédente pour l'appliquer à la branche `master` :

```shell
git log
```

4. Basculez sur la branche `master` et appliquez la modification à la branche `master` :

```shell
git checkout master
git cherry-pick 1609c283ec86ee4
```

5. Vérifiez que la modification a été appliquée à la branche `master` :

```shell
git log
```

Voici le résultat de l'exécution de `git log` sur la branche `master` :

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
