# Supprimer des fichiers de la zone de préparation

Vous travaillez sur un projet dans le référentiel `git-playground`. Vous avez apporté quelques modifications aux fichiers et les avez ajoutés à la zone de préparation à l'aide de la commande `git add`. Cependant, vous constatez que vous avez accidentellement ajouté un fichier que vous ne voulez pas valider. Vous devez supprimer ce fichier de la zone de préparation.

1. Voir l'état du répertoire de travail actuel :

```shell
git status
```

2. Supprimer le fichier `newfile.txt` de la zone de préparation à l'aide de la commande `git restore --staged` :

```shell
git restore --staged newfile.txt
```

3. Vérifier que le fichier a été supprimé de la zone de préparation à l'aide de la commande `git status` :

```shell
git status
```

Voici le résultat final :

```shell
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
(use "git push" to publish your local commits)

Changes to be committed:
(use "git restore --staged <file>..." to unstage)
modified: README.md

Untracked files:
(use "git add <file>..." to include in what will be committed)
newfile.txt
```
