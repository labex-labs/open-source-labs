# Manuell den Commit finden, der einen Fehler eingeführt hat

Ihre Aufgabe ist es, manuell den Commit zu finden, der einen Fehler im Repository `git-playground` eingeführt hat. Das Repository befindet sich unter `https://github.com/labex-labs/git-playground`.

Um diese Herausforderung zu bewältigen, müssen Sie eine binäre Suche durch den Commit-Verlauf des Repositorys durchführen. Sie müssen die Commits als "gut" (fehlerfrei) oder "schlecht" (fehlerhaft) markieren, bis Sie den Commit gefunden haben, der den Fehler eingeführt hat.

## Aufgaben

Die Fehlermeldung lautet, dass die Datei `file2.txt` "This is file2.txt." anstatt "This is file2." ausgeben sollte.

1. Wechsel in das Repository-Verzeichnis.
2. Beginne eine binäre Suche.
3. Markiere den aktuellen Commit als "schlecht".
4. Markiere einen Commit mit der Nachricht "Initial commit" als "gut". Git wird automatisch einen neuen Commit auschecken, den Sie testen können.
5. Wenn der Inhalt der überprüften Datei `file2.txt` nicht mit dem Fehler übereinstimmt, markiere ihn als "gut".
6. Wenn der Inhalt der überprüften Datei `file2.txt` mit dem Fehler übereinstimmt, markiere ihn als "schlecht".
7. Sobald Sie den fehlerhaften Commit gefunden haben, beende die binäre Suche.

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
