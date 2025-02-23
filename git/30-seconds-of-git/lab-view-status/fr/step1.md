# Afficher l'état actuel

En tant que développeur, il est important de connaître l'état actuel de votre référentiel Git. Cela inclut des informations sur les fichiers qui ont été modifiés, les fichiers qui sont préparés pour le commit et les fichiers qui ne sont pas suivis. La commande `git status` fournit ces informations dans un format facile à lire.

Votre tâche consiste à utiliser la commande `git status` pour afficher l'état actuel du référentiel Git situé à `https://github.com/labex-labs/git-playground`. Vous devriez prêter attention à la sortie de la commande et essayer de comprendre ce qu'elle signifie.

Pour terminer ce laboratoire, vous devrez cloner le référentiel Git situé à `https://github.com/labex-labs/git-playground`.

1. Une fois que vous avez cloné le référentiel, accédez au répertoire racine du référentiel :

```shell
cd git-playground
```

2. Affichez l'état actuel du référentiel Git :

```shell
git status
```

Cela affichera l'état actuel de l'arbre de travail. Vous devriez voir des informations sur la branche sur laquelle vous vous trouvez actuellement, si votre branche est à jour avec le référentiel distant et tout fichier non suivi ou modifié.

La sortie ressemble à ceci :

```shell
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
```
