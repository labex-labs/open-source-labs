# Restaurer un fichier supprimé

Vous travaillez sur un projet utilisant Git et vous avez accidentellement supprimé un fichier nommé `file2.txt` dont vous avez besoin. Heureusement, vous connaissez le commit où le fichier a été supprimé. Votre tâche est de restaurer le fichier supprimé à l'aide de Git.

Pour terminer ce laboratoire, vous utiliserez le référentiel Git `git-playground` de `https://github.com/labex-labs/git-playground.git`. Suivez les étapes ci-dessous :

1. Accédez au répertoire du référentiel en utilisant la commande `cd git-playground`.
2. Exécutez la commande `git log --oneline` pour afficher l'historique des commits.
3. Identifiez un commit où un fichier a été supprimé avec le message "Added file2.txt".
4. Exécutez la commande `git checkout <commit> -- <file>` pour restaurer le fichier `<file>` spécifié supprimé dans le commit `<commit>` spécifié. Remplacez `<commit>` par le hash du commit et `<file>` par le nom du fichier supprimé.

Par exemple, si le fichier `file2.txt` a été supprimé dans le commit `d22f46b`, vous exécuteriez la commande suivante :

```shell
git checkout d22f46b -- file2.txt
```

Cela restaurera le fichier `file2.txt` dans votre référentiel local.

Voici le résultat de l'exécution de la commande `ll` :

```shell
total 12K
-rw-r--r-- 1 labex labex 15 Jun 18 18:05 file1.txt
-rw-r--r-- 1 labex labex 15 Jun 18 18:13 file2.txt
-rw-r--r-- 1 labex labex 32 Jun 18 18:05 README.md
```
