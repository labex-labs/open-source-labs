# Einen Commit rückgängig machen

Angenommen, Sie haben einen Commit in Ihr Git-Repository gemacht, stellen Sie jedoch fest, dass ein Fehler enthalten ist. Sie möchten den Commit rückgängig machen, ohne die Geschichte Ihres Repositorys neu zu schreiben. Wie können Sie das tun?

Um zu demonstrieren, wie man einen Commit rückgängig macht, verwenden wir das Repository von `https://github.com/labex-labs/git-playground`. Folgen Sie diesen Schritten:

1. Klonen Sie das Repository, navigieren Sie zum Verzeichnis und konfigurieren Sie die Identität:
   ```
   git clone https://github.com/labex-labs/git-playground
   cd git-playground
   git config --global user.name "your-username"
   git config --global user.email "your-email"
   ```
2. Zeigen Sie die Commit-Geschichte an:
   ```
   git log
   ```
   Sie sollten eine Liste von Commits sehen, jeder mit einer eindeutigen Kennung (einer langen Zeichenfolge aus Buchstaben und Zahlen).
3. Wählen Sie einen Commit mit der Nachricht "Added file1.txt" und kopieren Sie seine Kennung.
4. Verwenden Sie den Befehl `git revert`, um den Commit rückgängig zu machen:
   ```
   git revert <commit>
   ```
   Ersetzen Sie `<commit>` durch die Kennung des Commits, den Sie rückgängig machen möchten.
5. Git öffnet einen Texteditor und lässt Sie eine Commit-Nachricht eingeben, wobei die Standardnachricht beibehalten bleibt.
6. Speichern Sie und schließen Sie den Texteditor.
7. Zeigen Sie die Commit-Geschichte erneut an:
   ```
   git log
   ```
   Sie sollten einen neuen Commit sehen, der die von dem ursprünglichen Commit vorgenommenen Änderungen rückgängig macht.

Dies ist das Ergebnis der Ausführung des Befehls `git log`:

```
commit 0d01f357a798f8960959546750d89a7e56a04a44 (HEAD -> master)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Mon Jul 24 21:52:43 2023 +0800

    Revert "Added file1.txt"

    This reverts commit cf80005e40a3c661eb212fcea5fad06f8283f08f.
```
