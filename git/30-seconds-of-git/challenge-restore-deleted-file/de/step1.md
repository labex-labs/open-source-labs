# Eine gelöschte Datei wiederherstellen

Sie arbeiten an einem Projekt mit Git und haben versehentlich eine Datei namens `file2.txt` gelöscht, die Sie benötigen. Glücklicherweise kennen Sie den Commit, in dem die Datei gelöscht wurde. Ihre Aufgabe ist es, die gelöschte Datei mit Git wiederherzustellen.

## Aufgaben

Um diese Herausforderung zu lösen, verwenden Sie das Git-Repository `git-playground` von `https://github.com/labex-labs/git-playground.git`.

1. Identifizieren Sie einen Commit, in dem eine Datei mit der Nachricht "Added file2.txt" gelöscht wurde.
2. Stellen Sie die gelöschte Datei her, indem Sie den Commit vor der Löschung auschecken.

Dadurch wird die Datei `file2.txt` in Ihr lokales Repository wiederhergestellt.

Dies ist das Ergebnis des Ausführens des Befehls `ll`:

```shell
total 12K
-rw-r--r-- 1 labex labex 15 Jun 18 18:05 file1.txt
-rw-r--r-- 1 labex labex 15 Jun 18 18:13 file2.txt
-rw-r--r-- 1 labex labex 32 Jun 18 18:05 README.md
```
