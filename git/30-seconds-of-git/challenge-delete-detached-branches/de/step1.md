# Entfernen von detached branches

Sie haben ein Git-Repository mit mehreren detached branches, die Sie nicht mehr benötigen. Diese Branches verschmutzen Ihr Repository und erschweren die Verwaltung. Sie möchten alle detached branches löschen, um Ihr Repository aufzuräumen.

## Aufgaben

Um diese Herausforderung zu bewältigen, verwenden Sie das Git-Repository `git-playground` aus Ihrem GitHub-Konto, das von einem Fork von `https://github.com/labex-labs/git-playground.git` stammt. Aktivieren Sie nicht die Option "Nur die master-Branch kopieren".

1. Klonen Sie das Repository, navigieren Sie zum Verzeichnis und konfigurieren Sie die Identität.
2. Da es in dem Remote-Repository eine `feature-branch` gibt, wechseln Sie zu `feature-branch`, was dazu führt, dass die lokale `feature-branch` den `feature-branch`-Branch des Remote-Repositories verfolgt und den `feature-branch`-Branch im Remote-Repository löscht.
3. Zeigen Sie die Verfolgungsbeziehung zwischen lokalen Branches und den Remote-Branches, die sie verfolgen.
4. Wechseln Sie zurück zum `master`-Branch.
5. Entfernen Sie alle detached branches aus Ihrem lokalen Repository.
6. Vergewissern Sie sich, dass die detached branches gelöscht wurden.

Die Ausgabe sollte nur die Branches anzeigen, die mit einem bestimmten Branch assoziiert sind:

```shell
* master d22f46b [origin/master] Added file2.txt
```
