# Supprimer les branches fusionnées

Votre tâche consiste à supprimer toutes les branches locales qui ont été fusionnées dans la branche `master` du référentiel `https://github.com/labex-labs/git-playground`.

1. Accédez au répertoire du référentiel :

```shell
cd git-playground
```

2. Liste toutes les branches locales qui ont été fusionnées dans `master` :

```shell
git branch --merged
```

Sortie :

```
* master
  new-branch
  new-branch-1
  new-branch-2
  new-branch-3
```

3. Supprime toutes les branches fusionnées :

```shell
git branch --merged master | awk '!/^[ *]*$/ &&!/master/ {print $1}' | xargs git branch -d
```

4. Liste à nouveau toutes les branches :

```shell
git branch
```

Voici le résultat final :

```
* master
```
