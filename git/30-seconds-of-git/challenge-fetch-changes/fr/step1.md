# Récupérer les dernières modifications à partir d'un dépôt distant

Supposons que vous travailliez sur un projet avec une équipe de développeurs et que le projet soit stocké dans un dépôt distant. Vous voulez obtenir les dernières modifications du dépôt distant sans les appliquer à votre dépôt local.

## Tâches

Pour démontrer comment récupérer les dernières modifications d'un dépôt distant, nous utiliserons le dépôt Git `git-playground` de votre compte GitHub, qui provient d'un fork de `https://github.com/labex-labs/git-playground.git`.

1. Clonez le dépôt, accédez au répertoire.
2. Trouvez le dépôt `git-playground` dans votre compte sur le site web GitHub, créez et basculez sur une branche appelée `fetch-branch`, créez un fichier appelé `hello.txt`, ajoutez "hello, world" et validez avec le message "Créer hello.txt".
3. Affichez les branches dans les dépôts distants.
4. Récupérez les dernières modifications du dépôt distant.
5. Affichez à nouveau les branches dans les dépôts distants et vérifiez que les dernières modifications ont été récupérées.

Voici le résultat de l'exécution de `git log origin/fetch-branch` :

```shell
commit f3125b4c99e0ef2ce58bc0b1287c966c9e68c577 (origin/fetch-branch)
Author: xiaoshengyunan <131872312+xiaoshengyunan@users.noreply.github.com>
Date:   Thu Jul 20 20:17:23 2023 +0800

    Create hello.txt
```
