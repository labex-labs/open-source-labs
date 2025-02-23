# Den letzten Commit rückgängig machen

Du hast gerade Änderungen an deinem Git-Repository committet, stellst jedoch fest, dass du einen Fehler begangen hast. Du möchtest den letzten Commit rückgängig machen, ohne irgendwelche der von dir vorgenommenen Änderungen zu verlieren. Wie kannst du das tun?

Für dieses Lab verwenden wir das Repository von `https://github.com/labex-labs/git-playground`. Folgen Sie diesen Schritten:

1. Klonen Sie das Repository, navigieren Sie zum Verzeichnis und konfigurieren Sie die Identität:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Überprüfen Sie die Commit-Historie:

```shell
git log
```

3. Machen Sie den letzten Commit rückgängig, indem Sie einen neuen Commit mit der Umkehrung der Änderungen des Commits erstellen:

```shell
git revert HEAD
```

4. Überprüfen Sie die Commit-Historie erneut:

```shell
git log
```

Dies ist das Ergebnis der Ausführung des Befehls `git log --oneline`:

```shell
532b49b (HEAD -> master) Revert "Added file2.txt"
d22f46b (origin/master, origin/HEAD) Added file2.txt
cf80005 Added file1.txt
b00b937 Initial commit
```
