# Löschen von gemergten Branches

Ihre Aufgabe ist es, alle lokalen Branches zu löschen, die in den `master`-Branch des Repositorys `https://github.com/labex-labs/git-playground` gemergt wurden.

1. Wechseln Sie in das Repository-Verzeichnis:

```shell
cd git-playground
```

2. Listen Sie alle lokalen Branches auf, die in `master` gemergt wurden:

```shell
git branch --merged
```

Ausgabe:

```
* master
  new-branch
  new-branch-1
  new-branch-2
  new-branch-3
```

3. Löschen Sie alle gemergten Branches:

```shell
git branch --merged master | awk '!/^[ *]*$/ &&!/master/ {print $1}' | xargs git branch -d
```

4. Listen Sie alle Branches erneut auf:

```shell
git branch
```

Dies ist das Endresultat:

```
* master
```
