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

ADD hello.txt
```
