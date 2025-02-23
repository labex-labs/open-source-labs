# Führen Sie eine interaktive Rebase durch

Sie arbeiten an einem Projekt mit einem Team von Entwicklern und haben mehrere Commits an Ihrem Branch durchgeführt. Sie stellen jedoch fest, dass einige der Commits unnötig sind oder zusammengefasst werden müssen. Sie möchten Ihren Commit-History aufräumen und ihn organisierter gestalten.

## Aufgaben

Für diese Herausforderung verwenden wir das Repository von `https://github.com/labex-labs/git-playground`.

1. Navigieren Sie zum Verzeichnis.
2. Führen Sie eine interaktive Rebase der letzten 2 Commits durch.
3. Ändern Sie "pick" in "squash" in der Commit-Nachricht "Added file2.txt", drücken Sie <kbd>Esc</kbd> und geben Sie den Befehl <kbd>:wq</kbd> ein, drücken Sie dann <kbd>Enter</kbd>, um Ihre Änderungen zu speichern und den Editor zu verlassen. Ändern Sie die Commit-Nachricht auf die gleiche Weise in "Added file1.txt and file2.txt" und beenden Sie.

Wenn Sie `git log` ausführen, erhalten Sie ein Ergebnis, das wie folgt aussieht:

```shell
commit 7575ded485555c28ecb09487c68e90639bebbe9d (HEAD -> master)
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file1.txt and file2.txt

commit b00b9374a7c549d1af111aa777fdcc868d8a2a01
Author: Hang <huhuhang@gmail.com>
Date:   Wed Apr 26 14:16:00 2023 +0800

    Initial commit
```
