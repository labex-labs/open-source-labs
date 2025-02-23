# Zeige einen kurzen Überblick über Commits ohne Merge-Commits

Sie arbeiten an einem Projekt mit mehreren anderen Entwicklern und möchten einen Überblick über alle Commits im Repository haben. Sie möchten jedoch keine Merge-Commits sehen, da diese keine tatsächlichen Änderungen am Code enthalten. Wie können Sie einen Überblick über alle Commits ohne Merge-Commits anzeigen?

## Aufgaben

Für diese Herausforderung verwenden wir das Repository von `https://github.com/labex-labs/git-playground`.

1. Navigiere zum Verzeichnis und konfiguriere die Identität.
2. Erstelle und wechsle zu einer Branch namens `feature1`, erstelle eine Datei namens `file.txt` und schreibe "feature 1" hinein, füge sie zum Staging-Area hinzu und commite sie mit der Nachricht "Add feature 1".
3. Wechsel zurück zur `master`-Branch, merke die `feature1`-Branch zusammen, deaktiviere das Vorwärts-Merging, speichere und beende ohne den Text zu ändern.
4. Zeige einen kurzen Überblick über alle Commits ohne Merge-Commits an.

Dies wird eine Liste aller Commits im Repository ausgeben, ohne jegliche Merge-Commits. Die Ausgabe wird ungefähr so aussehen:

```shell
430b986 (feature1) Add feature 1
d22f46b (origin/master, origin/HEAD) Added file2.txt
cf80005 Added file1.txt
b00b937 Initial commit
```
