# Erstellen eines Fixup-Commits

Angenommen, Sie arbeiten an einem Projekt mit mehreren anderen Entwicklern und stellen einen kleinen Fehler in einem Commit fest, der vor ein paar Tagen gemacht wurde. Sie möchten den Fehler beheben, aber Sie möchten keinen neuen Commit erstellen und die Arbeit der anderen Entwickler stören. Hier kommen Fixup-Commits sehr praktisch. Indem Sie einen Fixup-Commit erstellen, können Sie die erforderlichen Änderungen vornehmen, ohne einen neuen Commit zu erstellen, und der Fixup-Commit wird automatisch mit dem ursprünglichen Commit während der nächsten Rebase zusammengeführt.

## Aufgaben

Ihre Aufgabe ist es, die Zeichenfolge "hello,world" in die Datei `hello.txt` zu schreiben und sie als "Fixup"-Commit zum Commit mit der Nachricht "Added file1.txt" hinzuzufügen, so dass sie automatisch in einem späteren Rebase-Vorgang zusammengeführt werden kann.

Für diese Herausforderung verwenden wir das Repository von `https://github.com/labex-labs/git-playground`.

1. Navigieren Sie zum Verzeichnis und konfigurieren Sie die Identität.
2. Erstellen Sie eine Datei `hello.txt`, schreiben Sie "hello,world" darin und fügen Sie sie in den Staging-Bereich hinzu.
3. Erstellen Sie einen Fixup-Commit für den Hash der Commit-Nachricht "Added file1.txt".
4. Nachdem Sie den Fixup-Commit erstellt haben, können Sie ihn automatisch mit dem ursprünglichen Commit während der nächsten Rebase zusammenführen. Wenn Sie den interaktiven Editor öffnen, müssen Sie den Text nicht ändern und können ihn einfach speichern, um zu beenden.

Dies ist das Ergebnis der Ausführung des Befehls `git show HEAD~1`:

```shell
[object Object]
```
