# Consulter un résumé bref des commits

En tant que développeur, vous travaillez sur un projet avec plusieurs contributeurs. Vous devez consulter un résumé de tous les commits effectués sur le projet pour comprendre les modifications apportées et identifier tout problème potentiel. Cependant, vous ne voulez pas passer beaucoup de temps à trier tous les messages de commit pour trouver les informations dont vous avez besoin.

Pour consulter un résumé bref de tous les commits effectués dans un référentiel Git, vous pouvez utiliser la commande `git log --oneline`. Par exemple, supposons que vous travailliez sur un projet hébergé sur GitHub appelé `git-playground`.

1. Vous pouvez cloner le référentiel sur votre machine locale en utilisant la commande suivante :

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Une fois que vous avez cloné le référentiel, accédez au répertoire du projet et exécutez la commande suivante pour consulter un résumé bref de tous les commits :

```shell
cd git-playground
git log --oneline
```

Cela affichera une liste de tous les commits effectués dans le référentiel, ainsi qu'un résumé bref de chaque message de commit. Par exemple :

```shell
d22f46b (HEAD -> master, origin/master, origin/feature-branch, origin/HEAD) Ajouté file2.txt
cf80005 Ajouté file1.txt
b00b937 Commit initial
```
