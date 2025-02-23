# Manuell den Commit finden, der einen Fehler eingeführt hat

Ihre Aufgabe ist es, manuell den Commit zu finden, der einen Fehler im Repository `git-playground` eingeführt hat. Das Repository befindet sich unter `https://github.com/labex-labs/git-playground`. Der Fehler besteht darin, dass die Datei `file2.txt` "This is file2.txt." anstatt "This is file2." ausgeben sollte.

Um diesen Lab zu absolvieren, müssen Sie den Befehl `git bisect` verwenden, um eine binäre Suche durch den Commit-Verlauf des Repositorys durchzuführen. Sie müssen Commits als "gut" (fehlerfrei) oder "schlecht" (fehlerhaft) markieren, bis Sie den Commit eingeschränkt haben, der den Fehler eingeführt hat.

1. Wechsel in das Repository-Verzeichnis:

```
cd git-playground
```

2. Starte den `git bisect`-Prozess:

```
git bisect start
```

3. Markiere den aktuellen Commit als "schlecht":

```
git bisect bad HEAD
```

4. Markiere einen Commit mit der Nachricht "Initial commit" als "gut". Git wird automatisch einen neuen Commit auschecken, den Sie testen können:

```
git bisect good 3050fc0de
```

Git wird automatisch einen neuen Commit auschecken, den Sie testen können. 5. Wenn der Inhalt der ausgesuchten Datei `file2.txt` nicht mit dem Fehler übereinstimmt, markiere ihn als "gut":

```
cat file2.txt
git bisect good
```

6. Wenn der Inhalt der ausgesuchten Datei `file2.txt` mit dem Fehler übereinstimmt, markiere ihn als "schlecht":

```
git bisect bad
```

7. Nachdem Sie den fehlerhaften Commit gefunden haben, setzen Sie den `git bisect`-Prozess zurück:

```
git bisect reset
```

Sie können jetzt die Codeänderungen im fehlerhaften Commit untersuchen, um die Quelle des Fehlers zu finden.

Dies ist das Ergebnis des Tests:

```
d22f46ba8c2d4e07d773c5126e9c803933eb5898 ist der erste schlechte Commit
commit d22f46ba8c2d4e07d773c5126e9c803933eb5898
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt

 file2.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 file2.txt
```
