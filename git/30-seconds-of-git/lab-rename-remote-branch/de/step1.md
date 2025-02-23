# Remote Branch umbenennen

Um dieses Lab abzuschließen, verwendest du das Git-Repository `git-playground` aus deinem GitHub-Konto, das von einem Fork von `https://github.com/labex-labs/git-playground.git` stammt. Bitte deaktivieren Sie das Kontrollkästchen "Nur master-Branch kopieren", wenn Sie forken.

Du hast ein Git-Repository namens `https://github.com/your-username/git-playground`. Du hast einen Branch namens `feature-branch` erstellt und ihn auf den Remote geschoben. Jetzt möchtest du den Branch sowohl lokal als auch remote in `new-feature-1` umbenennen.

1. Klone das Repository, navigiere zum Verzeichnis und konfiguriere die Identität:
   ```shell
   git clone https://github.com/your-username/git-playground.git
   cd git-playground
   git config --global user.name "your-username"
   git config --global user.email "your-email"
   ```
2. Wechsel zum Branch namens `feature-branch`:
   ```shell
   git checkout feature-branch
   ```
3. Benenne den Branch sowohl lokal als auch remote um:
   ```shell
   git branch -m feature-branch new-feature-1
   git push origin --delete feature-branch
   git push -u origin new-feature-1
   ```
4. Verifiziere, dass der Branch umbenannt wurde:
   ```shell
   git branch -a
   ```

Dies ist das Ergebnis von `git branch -a`:

```shell
* master
new-feature-1
remotes/origin/HEAD - > origin/master
remotes/origin/master
remotes/origin/new-feature-1
```
