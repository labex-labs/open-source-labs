# Eine gelöschte Datei wiederherstellen

Sie arbeiten an einem Projekt mit Git und haben versehentlich eine Datei namens `file2.txt` gelöscht, die Sie benötigen. Glücklicherweise kennen Sie den Commit, in dem die Datei gelöscht wurde. Ihre Aufgabe besteht darin, die gelöschte Datei mit Git wiederherzustellen.

Um dieses Lab zu absolvieren, verwenden Sie das Git-Repository `git-playground` von `https://github.com/labex-labs/git-playground.git`. Folgen Sie den Schritten unten:

1. Navigieren Sie zum Repository-Verzeichnis mit dem Befehl `cd git-playground`.
2. Führen Sie den Befehl `git log --oneline` aus, um die Commit-Historie anzuzeigen.
3. Identifizieren Sie einen Commit, in dem eine Datei mit der Nachricht "Added file2.txt" gelöscht wurde.
4. Führen Sie den Befehl `git checkout <commit> -- <file>` aus, um die angegebene `<file>` wiederherzustellen, die in dem angegebenen `<commit>` gelöscht wurde. Ersetzen Sie `<commit>` durch den Commit-Hash und `<file>` durch den Namen der gelöschten Datei.

Beispielsweise würde der Befehl lauten, wenn die Datei `file2.txt` im Commit `d22f46b` gelöscht wurde:

```shell
git checkout d22f46b -- file2.txt
```

Dadurch wird die Datei `file2.txt` in Ihr lokales Repository wiederhergestellt.

Dies ist das Ergebnis der Ausführung des Befehls `ll`:

```shell
total 12K
-rw-r--r-- 1 labex labex 15 Jun 18 18:05 file1.txt
-rw-r--r-- 1 labex labex 15 Jun 18 18:13 file2.txt
-rw-r--r-- 1 labex labex 32 Jun 18 18:05 README.md
```
