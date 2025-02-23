# Änderungen zwischen Commits anzeigen

Als Entwickler arbeiten Sie an einem Projekt, das auf dem Repository `https://github.com/labex-labs/git-playground` gehostet ist. Sie haben mehrere Commits an das Repository vorgenommen und möchten einen Überblick über die Änderungen zwischen zwei bestimmten Commits erhalten. Sie sind sich jedoch nicht sicher, wie Sie dies mit Git tun.

Um einen Überblick über die Änderungen zwischen zwei Commits zu erhalten, sagen wir, Sie möchten die Änderungen zwischen dem `HEAD`-Commit und dem Commit mit der Nachricht "Initial commit" anzeigen. Hier ist, wie Sie es tun können:

1. Öffnen Sie ein Terminalfenster und navigieren Sie zum Verzeichnis, in dem das `git-playground`-Repository gespeichert ist:

```
cd git-playground
```

2. Führen Sie den folgenden Befehl aus:

```
git shortlog 3050fc0de..HEAD
```

Git wird einen Überblick über die Änderungen zwischen den beiden Commits anzeigen. Sie können die Pfeiltasten verwenden, um durch den Überblick zu navigieren, und drücken Sie `Q`, um zu beenden.

Hier ist ein Beispiel dafür, wie die Ausgabe aussehen könnte:

```shell
Hang (2):
      Added file1.txt
      Added file2.txt
```

In diesem Beispiel zeigt Git, dass es zwischen dem Commit `3050fc0de` und dem `HEAD`-Commit zwei Commits gab. Der erste Commit hat `file1.txt` hinzugefügt, und der zweite Commit hat `file2.txt` hinzugefügt.
