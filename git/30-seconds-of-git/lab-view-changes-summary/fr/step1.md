# Consulter les modifications entre deux commits

En tant que développeur, vous travaillez sur un projet hébergé sur le référentiel `https://github.com/labex-labs/git-playground`. Vous avez effectué plusieurs commits sur le référentiel, et vous voulez consulter un résumé des modifications entre deux commits spécifiques. Cependant, vous n'êtes pas sûr de savoir comment le faire avec Git.

Pour consulter un résumé des modifications entre deux commits, disons que vous voulez voir les modifications entre le commit `HEAD` et le commit avec le message "Initial commit". Voici comment vous pouvez le faire :

1. Ouvrez une fenêtre de terminal et accédez au répertoire où se trouve le référentiel `git-playground` :

```
cd git-playground
```

2. Exécutez la commande suivante :

```
git shortlog 3050fc0de..HEAD
```

Git affichera un résumé des modifications entre les deux commits. Vous pouvez utiliser les flèches pour naviguer dans le résumé et appuyer sur `Q` pour sortir.

Voici un exemple de ce que pourrait être la sortie :

```shell
Hang (2):
      Added file1.txt
      Added file2.txt
```

Dans cet exemple, Git montre qu'il y a eu deux commits entre le commit `3050fc0de` et le commit `HEAD`. Le premier commit a ajouté `file1.txt` et le second commit a ajouté `file2.txt`.
