# Récupérer les dernières modifications à partir d'un dépôt distant

Supposons que vous travailliez sur un projet avec une équipe de développeurs et que le projet soit stocké dans un dépôt distant. Vous voulez obtenir les dernières modifications du dépôt distant sans les appliquer à votre dépôt local. C'est là que la commande `git fetch` s'avère pratique.

La commande `git fetch` télécharge les dernières modifications du dépôt distant vers votre dépôt local, mais elle ne les applique pas à votre répertoire de travail. Cela signifie que vous pouvez examiner les modifications avant de les fusionner dans votre dépôt local.

Pour démontrer comment récupérer les dernières modifications d'un dépôt distant, nous utiliserons le référentiel Git `git-playground` de votre compte GitHub, qui provient d'un fork de `https://github.com/labex-labs/git-playground.git`. Suivez les étapes ci-dessous :

1. Clonez le référentiel, accédez au répertoire :

```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
```

2. Trouvez le référentiel `git-playground` dans votre compte sur le site web GitHub, créez et basculez sur une branche appelée `fetch-branch`, créez un fichier appelé `hello.txt`, ajoutez "hello, world" et validez avec le message "Create hello.txt".
3. Affichez les branches dans les dépôts distants :

```shell
git branch -r
```

4. Récupérez les dernières modifications du dépôt distant :

```shell
git fetch
```

5. Affichez à nouveau les branches dans les dépôts distants et vérifiez que les dernières modifications ont été récupérées :

```shell
git branch -r
git log origin/fetch-branch
```

Cela vous montrera les derniers commits sur la branche `origin/fetch-branch`.Voici le résultat de l'exécution de `git log origin/fetch-branch` :

```shell
commit f3125b4c99e0ef2ce58bc0b1287c966c9e68c577 (origin/fetch-branch)
Author: xiaoshengyunan <131872312+xiaoshengyunan@users.noreply.github.com>
Date:   Thu Jul 20 20:17:23 2023 +0800

    Create hello.txt
```
