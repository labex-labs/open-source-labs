# Branches finden, die einen Commit enthalten

Es wurde Ihnen ein Git-Repository mit dem Namen `https://github.com/labex-labs/git-playground` zur Verfügung gestellt. Ihre Aufgabe besteht darin, alle Branches zu finden, die einen Hash mit der Commit-Nachricht "Added file2.txt" enthalten.

1. Wechsel in das Repository-Verzeichnis:

```shell
cd git-playground
```

2. Verwenden Sie den Befehl `git branch --contains`, um alle Branches zu finden, die einen Hash mit der Commit-Nachricht "Added file2.txt" enthalten:

```shell
git branch --contains d22f46b
```

Die Ausgabe sollte wie folgt sein:

```shell
* master
new-branch
new-branch-1
new-branch-2
```
