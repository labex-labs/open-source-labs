# Ein Branch zusammenführen und einen Merge-Commit erstellen

Als Entwickler musst du möglicherweise einen Branch in den aktuellen Branch zusammenführen und dabei einen Merge-Commit erstellen. Dies kann etwas tricky sein, wenn du nicht vertraut mit Git bist. Das Problem besteht darin, einen Branch in den aktuellen Branch zusammenzuführen und dabei einen Merge-Commit zu erstellen, indem du das Git-Repository mit dem Namen `https://github.com/labex-labs/git-playground` verwendest.

## Aufgaben

Für diese Herausforderung verwenden wir das Repository von `https://github.com/labex-labs/git-playground`.

1. Klone das Repository, navigiere in das Verzeichnis und konfiguriere die Identität.
2. Erstelle und wechsle zu einem Branch namens `feature-branch`.
3. Füge die Zeile "Dies ist eine neue Zeile." zur Datei `README.md` hinzu, füge sie zum Staging-Area hinzu und commite sie, die Commit-Nachricht lautet "Füge neue Zeile zu README.md hinzu".
4. Wechsle zum `master`-Branch.
5. Führe den `feature-branch` in den `master`-Branch zusammen, was einen Merge-Commit mit der Nachricht "Merge feature-branch" erstellt.

Dies ist das Ergebnis von `git log`:

```shell



ADD new line to README.md
```
