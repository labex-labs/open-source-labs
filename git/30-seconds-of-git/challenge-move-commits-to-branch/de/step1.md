# Commits zu einem neuen Branch verschieben

Für diese Herausforderung verwenden wir das Repository von `https://github.com/labex-labs/git-playground`. Sie haben an einem Projekt am `master`-Branch gearbeitet. Sie stellen fest, dass einige der Änderungen, die Sie vorgenommen haben, an einem separaten Branch vorgenommen werden sollten. Sie möchten diese Änderungen auf einen neuen Branch namens `feature` verschieben.

## Aufgaben

1. Navigieren Sie zum Repository-Verzeichnis und konfigurieren Sie Ihre GitHub-Identität.
2. Wechseln Sie zum `master`-Branch.
3. Erstellen Sie eine Datei namens `hello.txt`, fügen Sie "hello, world" hinzu, fügen Sie sie zum Staging-Bereich hinzu und übermitteln Sie sie mit der Nachricht "Added hello.txt".
4. Erstellen Sie einen neuen Branch namens `feature`, ohne zu wechseln.
5. Stornieren Sie den letzten Commit auf `master`.
6. Überprüfen Sie die Commit-Historie auf dem `master`-Branch und die Commit-Historie auf dem `feature`-Branch, um die Ergebnisse zu verifizieren.

Dies ist das Ergebnis von `git log`:

```shell
commit 7969ab5d6606e2a40c9fd826c732206b835976e9 (HEAD -> feature)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 20:19:22 2023 +0800

    Added hello.txt
```
