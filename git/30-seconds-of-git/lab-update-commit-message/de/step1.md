# Ändern der Nachricht des letzten Commits

Stellen Sie sich vor, Sie haben gerade einige Änderungen in Ihr Git-Repository commited, stellen Sie jedoch fest, dass Sie einen Tippfehler in der Commit-Nachricht gemacht haben. Sie möchten den Fehler beheben, ohne die tatsächlichen Änderungen zu verändern. Wie können Sie das tun?

Um zu demonstrieren, wie Sie die Nachricht des letzten Commits ändern, verwenden wir das Repository von `https://github.com/labex-labs/git-playground`. Folgen Sie diesen Schritten:

1. Klonen Sie das Repository, navigieren Sie zum Verzeichnis und konfigurieren Sie die Identität:
   ```
   git clone https://github.com/labex-labs/git-playground
   cd git-playground
   git config --global user.name "your-username"
   git config --global user.email "your-email"
   ```
2. Ändern Sie die Commit-Nachricht des letzten Commits, sodass sie "Fix the network bug" lautet:
   ```
   git commit --amend -m "Fix the network bug"
   ```
   Dies öffnet Ihren Standard-Texteditor, in dem Sie die Commit-Nachricht ändern können. Speichern Sie und schließen Sie den Editor, um den Prozess abzuschließen.
3. Vergewissern Sie sich, dass die Commit-Nachricht geändert wurde:
   ```
   git log --oneline
   ```

Sie sollten die aktualisierte Commit-Nachricht im Log sehen:

```
54b830b (HEAD -> master) Fix the network bug
cf80005 Added file1.txt
b00b937 Initial commit
```
