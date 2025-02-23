# Ein Branch zusammenführen und einen Merge-Commit erstellen

Als Entwickler musst du möglicherweise einen Branch in den aktuellen Branch zusammenführen und dabei einen Merge-Commit erstellen. Dies kann etwas tricky sein, wenn du nicht vertraut mit Git bist. Das Problem besteht darin, einen Branch in den aktuellen Branch zusammenzuführen und dabei einen Merge-Commit zu erstellen, indem du das Git-Repository mit dem Namen `https://github.com/labex-labs/git-playground` verwendest.

## Aufgaben

Für diese Herausforderung verwenden wir das Repository von `https://github.com/labex-labs/git-playground`.

1. Klone das Repository, navigiere in das Verzeichnis und konfiguriere die Identität.
2. Erstelle und wechsle zu einem Branch namens `feature-branch`.
3. Füge die Zeile "Dies ist eine neue Zeile." zur Datei `README.md` hinzu, füge sie zum Staging-Area hinzu und commite sie, die Commit-Nachricht lautet "Füge neue Zeile zu README.md hinzu".
4. Wechsle zum `master`-Branch.
5. Führe den `feature-branch` in den `master`-Branch zusammen, was einen Merge-Commit mit der Nachricht "Merge feature-branch" erstellt.

Dies ist das Ergebnis von `git log`:

```shell
commit 45b7e0fa8656d0aa751c7ca3cee29422e3d6cf05 (HEAD -> master)
Merge: d22f46b 1f19499
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 19:26:57 2023 +0800

    Merge feature-branch

commit 1f1949955387a154ff1bb5286d3d0a2b993f87e0 (feature-branch)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 19:26:57 2023 +0800

    Add new line to README.md
```
