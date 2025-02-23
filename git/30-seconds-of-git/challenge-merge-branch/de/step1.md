# Ein Branch zusammenführen

Ihre Aufgabe besteht darin, einen Branch mit Git in den aktuellen Branch zusammenzuführen. Sie müssen in den Zielbranch wechseln und dann den Quellbranch in ihn zusammenführen. Dies kann nützlich sein, wenn Sie Änderungen aus einem `feature-branch-A`-Branch in den `master`-Branch Ihres Projekts kombinieren möchten.

## Aufgaben

Für diese Herausforderung verwenden wir das Repository von `https://github.com/labex-labs/git-playground`.

1. Navigieren Sie zum Verzeichnis und konfigurieren Sie die Identität.
2. Erstellen Sie einen `feature-branch-A`-Branch. Wechseln Sie zu ihm.
3. Fügen Sie "hello,world" zur `file2.txt`-Datei hinzu, fügen Sie es zum Staging-Area hinzu und bestätigen Sie es mit der Nachricht "fix file2.txt".
4. Wechseln Sie zum `master`-Branch.
5. Führen Sie das Zusammenführen des `feature-branch-A` in den `master`-Branch durch.
6. Beheben Sie alle Konflikte, die während des Zusammenführungsvorgangs auftreten können.

Dies ist das Ergebnis von `git log`:

```shell
commit e2b80358ae6e4c3b8439cf111a4672a188739290 (HEAD -> master, feature-branch-A)
Author: xiaoshengyunan <xiaoshengyunan@users.noreply.github.com>
Date:   Fri Jul 21 18:51:00 2023 +0800

    fix file2.txt
```
