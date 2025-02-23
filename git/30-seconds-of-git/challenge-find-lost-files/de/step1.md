# Verlorene Dateien finden

Sie haben an einem Projekt im Repository `git-playground` gearbeitet. Sie haben jedoch festgestellt, dass einige Dateien fehlen und Sie sind sich nicht sicher, wann sie gelöscht wurden oder wie Sie sie wiederherstellen können. Ihre Aufgabe ist es, mit Git verlorene Dateien und Commits im Repository zu finden.

## Aufgaben

1. Navigieren Sie zum Verzeichnis und konfigurieren Sie die Identität.
2. Erstellen Sie und wechseln Sie zu einem Branch namens `one-branch`, löschen Sie `file2.txt` und committen Sie mit der Nachricht "Remove file2".
3. Wechseln Sie zurück zum `master`-Branch und löschen Sie den `one-branch`-Branch.
4. Finden Sie verlorene Dateien und Commits.
5. Überprüfen Sie das Verzeichnis `.git/lost-found`, um zu sehen, ob verlorene Dateien wiederhergestellt wurden.
6. Wenn verlorene Dateien gefunden wurden, überprüfen Sie sie, um zu bestimmen, ob es die fehlenden Dateien sind.

Dies ist das Ergebnis des Ausführens des Befehls `ls.git/lost-found`:

```shell
commit
```
