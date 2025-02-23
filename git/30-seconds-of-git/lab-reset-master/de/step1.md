# Lokale Master-Branch zurücksetzen, um der Remote zu entsprechen

Sie haben an einem Projekt gearbeitet und Änderungen an der lokalen `master`-Branch vorgenommen. Allerdings stellen Sie fest, dass die remote `master`-Branch mit neuen Änderungen aktualisiert wurde, die in Ihrer lokalen Branch nicht vorhanden sind. Sie müssen die lokale `master`-Branch zurücksetzen, um derjenigen auf der Remote zu entsprechen.

1. Wechseln Sie zur `master`-Branch:
   ```shell
   git checkout master
   ```
2. Holen Sie die neuesten Updates von der Remote:
   ```shell
   git fetch origin
   ```
3. Zeigen Sie den Commit-Verlauf der aktuellen Branch an:
   ```shell
   git log
   ```
4. Setzen Sie die lokale `master`-Branch zurück, um derjenigen auf der Remote zu entsprechen:
   ```shell
   git reset --hard origin/master
   ```
5. Vergewissern Sie sich, dass die lokale `master`-Branch jetzt mit der remote `master`-Branch synchron ist:
   ```shell
   git log
   ```

Dies ist das fertige Ergebnis:

```shell
commit d22f46ba8c2d4e07d773c5126e9c803933eb5898 (HEAD -> master, origin/master, origin/feature-branch, origin/HEAD)
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt

commit cf80005e40a3c661eb212fcea5fad06f8283f08f
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file1.txt

commit b00b9374a7c549d1af111aa777fdcc868d8a2a01
Author: Hang <huhuhang@gmail.com>
Date:   Wed Apr 26 14:16:00 2023 +0800

    Initial commit
```
