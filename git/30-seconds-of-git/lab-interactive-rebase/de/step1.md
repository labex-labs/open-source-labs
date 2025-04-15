# Führen Sie eine interaktive Neuverankerung durch

Sie arbeiten an einem Projekt mit einem Team von Entwicklern und haben mehrere Commits an Ihrem Branch durchgeführt. Sie stellen jedoch fest, dass einige der Commits unnötig sind oder zusammengefasst werden müssen. Sie möchten Ihre Commit-Historie aufräumen und sie besser strukturieren.

Für diese Übung verwenden wir das Repository von `https://github.com/labex-labs/git-playground`. Folgen Sie diesen Schritten:

1. Navigieren Sie zum Verzeichnis:
   ```shell
   cd git-playground
   ```
2. Führen Sie eine interaktive Neuverankerung der letzten 2 Commits durch:
   ```shell
   git rebase -i HEAD~2
   ```
   Die interaktive Neuverankerungsdatei wird in Ihrem Standardtexteditor geöffnet. Sie können die Reihenfolge der Commits und die Aktion ändern, die für jeden durchzuführen ist (pick, squash, drop, reword etc.).
3. Ändern Sie "pick" in "squash" in der Commit-Nachricht "Added file2.txt", drücken Sie <kbd>Esc</kbd> und geben Sie den Befehl <kbd>:wq</kbd> ein, drücken Sie dann <kbd>Enter</kbd>, um Ihre Änderungen zu speichern und den Editor zu verlassen, ändern Sie die Commit-Nachricht auf die gleiche Weise in "Added file1.txt and file2.txt" und beenden Sie.
4. Wenn es Mergekonflikte gibt oder Sie Änderungen vornehmen müssen, können Sie die Neuverankerung, wenn Sie fertig sind, mit `git rebase --continue` fortsetzen oder mit `git rebase --abort` abbrechen.

Das Ausführen von `git log` gibt Ihnen ein Ergebnis wie dieses:

```shell
[object Object]
```
