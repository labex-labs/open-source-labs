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

```
