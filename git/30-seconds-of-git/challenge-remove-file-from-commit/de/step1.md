# Entfernen einer Datei aus dem letzten Commit

Sie haben einer Datei in den letzten Commit hinzugefügt, die Sie nicht beabsichtigt haben, einzuschließen. Sie möchten die Datei aus dem letzten Commit entfernen, ohne dessen Nachricht zu ändern.

## Aufgaben

Für diese Herausforderung verwenden wir das Repository von `https://github.com/labex-labs/git-playground`. Stellen Sie sich vor, dass Sie ein Git-Repository namens `git-playground` haben, in dem eine Datei namens `file2.txt` vorhanden ist, die Sie versehentlich in den letzten Commit aufgenommen haben.

1. Navigieren Sie zum Repository-Verzeichnis und konfigurieren Sie Ihre GitHub-Identität.
2. Entfernen Sie die angegebene Datei `file2.txt` aus dem Index.
3. Aktualisieren Sie den Inhalt des letzten Commits, ohne dessen Nachricht zu ändern.

Nach Ausführung dieser Befehle wird die Datei `file2.txt` aus dem letzten Commit entfernt, ohne dessen Nachricht zu ändern.

Dies ist, was passiert, wenn Sie `file2.txt` aus der Git-Versionskontrolle entfernen:

```shell
On branch master

Changes to be committed:
(use "git restore --staged <file>..." to unstage)
deleted: file2.txt

Untracked files:
(use "git add <file>..." to include in what will be committed)
file2.txt
```
