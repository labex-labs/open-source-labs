# Anzeige von zusammengeführten Branches

Ihre Aufgabe ist es, eine Liste aller zusammengeführten lokalen Branches im Git-Repository mit dem Namen `https://github.com/labex-labs/git-playground` auszugeben. Sie müssen den Befehl `git branch -a --merged` verwenden, um die Liste der zusammengeführten Branches anzuzeigen. Nachdem Sie die Liste haben, sollten Sie mithilfe der Pfeiltasten durch sie navigieren können und indem Sie <kbd>Q</kbd> drücken, beenden.

1. Navigieren Sie zum Repository-Verzeichnis:

```shell
cd git-playground
```

2. Zeigen Sie die Liste der zusammengeführten Branches an:

```shell
git branch -a --merged
```

Dies ist das Endresultat:

```
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/feature-branch
  remotes/origin/master
```
