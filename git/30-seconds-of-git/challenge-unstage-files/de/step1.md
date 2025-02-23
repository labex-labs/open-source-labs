# Dateien aus dem Staging-Bereich entfernen

Sie arbeiten an einem Projekt im Repository `git-playground`. Sie haben einige Änderungen an den Dateien vorgenommen und sie in den Staging-Bereich hinzugefügt. Allerdings stellen Sie fest, dass Sie versehentlich eine Datei hinzugefügt haben, die Sie nicht committen möchten. Sie müssen diese Datei aus dem Staging-Bereich entfernen.

## Aufgaben

1. Zeigen Sie den Status des aktuellen Arbeitsverzeichnisses an.
2. Entfernen Sie die Datei `newfile.txt` aus dem Staging-Bereich.
3. Vergewissern Sie sich, dass die Datei aus dem Staging-Bereich entfernt wurde.

Dies ist das Endresultat:

```shell
Auf Branch master
Ihr Branch ist um 1 Commit vor 'origin/master'.
(verwenden Sie "git push", um Ihre lokalen Commits zu veröffentlichen)

Änderungen, die committet werden sollen:
(verwenden Sie "git restore --staged <file>..." zum Entfernen aus dem Staging)
verändert: README.md

Nicht verfolgte Dateien:
(verwenden Sie "git add <file>..." zum Einbeziehen in das, was committet werden soll)
newfile.txt
```
