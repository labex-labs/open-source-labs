# Restaurer un fichier supprimé

Vous travaillez sur un projet utilisant Git et vous avez accidentellement supprimé un fichier nommé `file2.txt` dont vous avez besoin. Heureusement, vous connaissez le commit où le fichier a été supprimé. Votre tâche est de restaurer le fichier supprimé à l'aide de Git.

## Tâches

Pour compléter ce défi, vous utiliserez le référentiel Git `git-playground` de `https://github.com/labex-labs/git-playground.git`.

1. Identifiez un commit où un fichier a été supprimé avec le message "Added file2.txt".
2. Restaurez le fichier supprimé en effectuant un checkout du commit avant la suppression.

Cela restaurera le fichier `file2.txt` dans votre référentiel local.

Voici le résultat de l'exécution de la commande `ll`:

```shell
total 12K
-rw-r--r-- 1 labex labex 15 Jun 18 18:05 file1.txt
-rw-r--r-- 1 labex labex 15 Jun 18 18:13 file2.txt
-rw-r--r-- 1 labex labex 32 Jun 18 18:05 README.md
```
