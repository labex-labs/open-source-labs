# Dateien aus dem Staging-Bereich entfernen

Du arbeitest an einem Projekt im Repository `git-playground`. Du hast einige Änderungen an den Dateien vorgenommen und sie mit dem Befehl `git add` in den Staging-Bereich hinzugefügt. Allerdings stellst du fest, dass du versehentlich eine Datei hinzugefügt hast, die du nicht committen möchtest. Du musst diese Datei aus dem Staging-Bereich entfernen.

1. Zeige den Status des aktuellen Arbeitsverzeichnisses an:

```shell
git status
```

2. Entferne die Datei `newfile.txt` aus dem Staging-Bereich mit dem Befehl `git restore --staged`:

```shell
git restore --staged newfile.txt
```

3. Verifiziere, dass die Datei aus dem Staging-Bereich entfernt wurde, indem du den Befehl `git status` verwendest:

```shell
git status
```

Dies ist das Endresultat:

```shell
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
(use "git push" to publish your local commits)

Changes to be committed:
(use "git restore --staged <file>..." to unstage)
modified: README.md

Untracked files:
(use "git add <file>..." to include in what will be committed)
newfile.txt
```
