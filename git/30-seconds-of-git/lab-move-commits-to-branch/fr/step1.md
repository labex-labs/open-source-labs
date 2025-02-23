# Décaler des commits vers une nouvelle branche

Pour ce laboratoire, utilisons le référentiel de `https://github.com/labex-labs/git-playground`. Vous avez travaillé sur un projet dans la branche `master`. Vous réalisez que certaines des modifications que vous avez apportées auraient dû être effectuées sur une branche distincte. Vous voulez déplacer ces modifications vers une nouvelle branche appelée `feature`.

1. Clonez le référentiel, accédez au répertoire et configurez l'identité :

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "votre-nom-d'utilisateur"
git config --global user.email "votre-email"
```

2. Basculez sur la branche `master` :

```shell
git checkout master
```

3. Créez un fichier appelé `hello.txt`, ajoutez "hello, world" à celui-ci, ajoutez-le à la zone de préparation et soumettez-le avec le message "Ajouté hello.txt" :

```shell
echo "hello,world" >> hello.txt
git add.
git commit -m "Ajouté hello.txt"
```

4. Créez une nouvelle branche appelée `feature` sans basculer sur elle. Lorsque vous créez une nouvelle branche à partir de la branche `master`, l'état de la nouvelle branche est le même que celui de la branche `master`, c'est-à-dire que les fichiers dans la nouvelle branche sont les mêmes que ceux dans la branche `master`, avec le même contenu et l'historique de versions :

```shell
git branch feature
```

5. Annulez le dernier commit sur `master` :

```shell
git reset HEAD~1 --hard
```

6. Vérifiez l'historique des commits sur la branche `master` et l'historique des commits sur la branche `feature` pour vérifier les résultats :

```shell
git log
git checkout feature
git log
```

Voici le résultat de l'exécution de `git log` :

```shell
commit 7969ab5d6606e2a40c9fd826c732206b835976e9 (HEAD -> feature)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 20:19:22 2023 +0800

    Ajouté hello.txt
```
