# Trouver les commits qui ont modifié une chaîne de caractères spécifique

En tant que développeur, vous pouvez avoir besoin de trouver tous les commits qui ont modifié une chaîne de caractères spécifique dans votre base de code. Par exemple, vous pouvez vouloir trouver tous les commits qui ont ajouté ou supprimé un nom de fonction ou une variable spécifique. Cela peut être utile lors du débogage de problèmes ou de la recherche de la source d'un bogue.

Supposons que vous travailliez sur un projet hébergé sur GitHub appelé `git-playground`. Vous voulez trouver tous les commits qui ont modifié la chaîne de caractères "Git Playground" dans le fichier `README.md`. Voici comment vous pouvez le faire :

1. Accédez au répertoire du référentiel :

```shell
cd git-playground
```

2. Utilisez la commande `git log -S` pour trouver tous les commits qui ont modifié la chaîne de caractères "Git Playground" dans le fichier `README.md` et utilisez les flèches pour naviguer dans la liste des commits. Appuyez sur <kbd>Q</kbd> pour quitter le journal :

```shell
git log -S"Git Playground" README.md
```

Git affichera une liste de tous les commits qui ont modifié la chaîne de caractères "Git Playground" dans le fichier `README.md` :

```shell
commit b00b9374a7c549d1af111aa777fdcc868d8a2a01
Author: Hang <huhuhang@gmail.com>
Date:   Wed Apr 26 14:16:00 2023 +0800

    Initial commit
```
