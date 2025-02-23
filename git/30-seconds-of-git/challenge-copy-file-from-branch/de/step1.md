# Kopiere eine Datei von einer anderen Branch

Du arbeitest an einem Projekt in einem Git-Repository namens `https://github.com/labex-labs/git-playground.git`. Du hast zwei Branches namens `feature-1` und `feature-2`. Du musst die Datei `hello.txt` von der Branch `feature-1` in die Branch `feature-2` kopieren.

## Aufgaben

1. Navigiere zum Verzeichnis und konfiguriere die Identität.
2. Erstelle und wechsle zur Branch `feature-1` und erstelle eine Textdatei namens `hello.txt` und schreibe die Zeichenfolge "hello,world" hinein und commite die Datei mit der Nachricht "add hello.txt".
3. Erstelle und wechsle zur Branch `feature-2` nachdem du zur Branch `master` gewechselt bist.
4. Kopiere die Datei `hello.txt` von der Branch `feature-1` in die Branch `feature-2` und commite sie mit der Commit-Nachricht "copy hello.txt".
5. Verifiziere, dass die Datei `hello.txt` in die Branch `feature-2` kopiert wurde.

Du solltest die Datei `hello.txt` in der Dateiliste der Branch `feature-2` sehen:

```
-rw-r--r-- 1 labex labex 15 Jul 12 22:43 file1.txt
-rw-r--r-- 1 labex labex 15 Jul 12 22:43 file2.txt
-rw-r--r-- 1 labex labex 12 Jul 12 22:50 hello.txt
-rw-r--r-- 1 labex labex 32 Jul 12 22:43 README.md
```
