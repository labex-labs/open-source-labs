# Afficher les branches fusionnées

Votre tâche consiste à imprimer la liste de toutes les branches locales fusionnées dans le référentiel Git nommé `https://github.com/labex-labs/git-playground`. Vous devrez utiliser la commande `git branch -a --merged` pour afficher la liste des branches fusionnées. Une fois que vous avez la liste, vous devriez être en mesure de naviguer à travers elle en utilisant les touches fléchées et de sortir en appuyant sur <kbd>Q</kbd>.

1. Accédez au répertoire du référentiel :

```shell
cd git-playground
```

2. Affichez la liste des branches fusionnées :

```shell
git branch -a --merged
```

Voici le résultat final :

```
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/feature-branch
  remotes/origin/master
```
