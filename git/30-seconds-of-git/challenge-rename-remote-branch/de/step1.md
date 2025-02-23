# Remote Branch umbenennen

Um diese Herausforderung zu absolvieren, verwendest du das Git-Repository `git-playground` aus deinem GitHub-Konto, das von einem Fork von `https://github.com/labex-labs/git-playground.git` stammt. Bitte deaktivieren Sie das Kontrollkästchen "Nur master-Branch kopieren", wenn Sie forken.

Sie haben ein Git-Repository namens `https://github.com/your-username/git-playground`. Sie haben einen Branch namens `feature-branch` erstellt und ihn auf den Remote-Push übertragen. Jetzt möchten Sie den Branch sowohl lokal als auch remote in `new-feature-1` umbenennen.

## Aufgaben

1. Klonen Sie das Repository, navigieren Sie zum Verzeichnis und konfigurieren Sie die Identität.
2. Wechseln Sie zum `feature-branch`-Branch.
3. Benennen Sie den Branch sowohl lokal als auch remote um.
4. Vergewissern Sie sich, dass der Branch umbenannt wurde.

Dies ist das Ergebnis von `git branch -a`:

```shell
* master
new-feature-1
remotes/origin/HEAD - > origin/master
remotes/origin/master
remotes/origin/new-feature-1
```
