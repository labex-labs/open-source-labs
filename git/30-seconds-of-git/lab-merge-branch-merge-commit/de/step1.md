# Ein Branch zusammenführen und einen Merge-Commit erstellen

Als Entwickler musst du möglicherweise einen Branch in den aktuellen Branch zusammenführen und dabei einen Merge-Commit erstellen. Dies kann etwas tricky sein, wenn du nicht vertraut mit Git bist. Das Problem besteht darin, einen Branch in den aktuellen Branch zusammenzuführen und dabei einen Merge-Commit zu erstellen, unter Verwendung des Git-Repositorys im Verzeichnis `https://github.com/labex-labs/git-playground`.

Für diese Herausforderung verwenden wir das Repository von `https://github.com/labex-labs/git-playground`.

1. Klone ein Repository von `https://github.com/labex-labs/git-playground.git`:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Navigiere zum Verzeichnis und konfiguriere die Identität:

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

3. Erstelle und wechsle zu einem Branch namens `feature-branch`:

```shell
git checkout -b feature-branch
```

4. Füge die Zeile "This is a new line." zur Datei `README.md` hinzu, füge sie zum Staging-Area hinzu und commite sie, die Commit-Nachricht lautet "Add new line to README.md":

```shell
echo "This is a new line." >> README.md
git add.
git commit -am "Add new line to README.md"
```

5. Wechsle zum `master`-Branch:

```shell
git checkout master
```

6. Führe den `feature-branch` in den `master`-Branch zusammen, was einen Merge-Commit mit der Nachricht "Merge feature-branch" erstellt:

```shell
git merge --no-ff -m "Merge feature-branch" feature-branch
```

Dies ist das Ergebnis von `git log`:

```shell
ADD new line to README.md
```
