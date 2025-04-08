# Standard-Push-Branch-Namen festlegen

Wenn Sie Änderungen in ein Remote-Repository pushen, verwendet Git den Namen des aktuellen lokalen Branches als Standardnamen für den Remote-Branch. Manchmal möchten Sie jedoch Ihre Änderungen in einen anderen Branch pushen. In diesem Fall müssten Sie den Namen des Remote-Branches jedes Mal explizit angeben, wenn Sie Ihre Änderungen pushen. Dies kann mühsam und fehleranfällig sein, insbesondere wenn Sie mit mehreren Branches arbeiten.

## Aufgaben

Um diese Herausforderung zu absolvieren, verwenden Sie das Git-Repository `git-playground` aus Ihrem GitHub-Konto, das von einem Fork von `https://github.com/labex-labs/git-playground.git` stammt. Folgen Sie den Schritten unten, um den Standard-Push-Branch-Namen festzulegen:

1. Klonen Sie das Repository von `https://github.com/your-username/git-playground.git`.
2. Wechseln Sie in das Repository-Verzeichnis.
3. Legen Sie den Standard-Push-Branch-Namen auf den Namen des aktuellen lokalen Branches fest.
4. Erstellen Sie einen neuen Branch namens `my-branch` und wechseln Sie zu ihm.
5. Erstellen Sie eine neue Datei namens `hello.txt` und schreiben Sie die Zeichenfolge "Hello, World" hinein. Fügen Sie die neu erstellte Datei `hello.txt` in den Git-Staging-Bereich hinzu und committen Sie sie, wobei Sie als Commit-Nachricht "Add hello.txt" verwenden, um die in diesem Commit vorgenommenen Änderungen zu beschreiben.
6. Pushen Sie Ihre Änderungen in das Remote-Repository. Git wird Ihre Änderungen in einen Branch namens `my-branch` im Remote-Repository pushen.

Dies ist das Ergebnis von `git log`:

```shell

ADD hello.txt
```
