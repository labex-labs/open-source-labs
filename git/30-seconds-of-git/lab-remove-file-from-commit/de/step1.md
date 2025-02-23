# Entfernen einer Datei aus dem letzten Commit

Sie haben einer Datei zum letzten Commit hinzugefügt, die Sie nicht einschließen wollten. Sie möchten die Datei aus dem letzten Commit entfernen, ohne die Commit-Nachricht zu ändern.

Für diese Übung verwenden wir das Repository von `https://github.com/labex-labs/git-playground`. Nehmen wir an, Sie haben ein Git-Repository namens `git-playground` mit einer Datei namens `file2.txt`, die Sie versehentlich zum letzten Commit hinzugefügt haben. Hier sind die Schritte, um die Datei aus dem letzten Commit zu entfernen:

1. Klonen Sie das Repository, navigieren Sie zum Verzeichnis und konfigurieren Sie die Identität:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Verwenden Sie `git rm --cached <file>`, um die angegebene `<file>` aus dem Index zu entfernen:

```shell
git rm --cached file2.txt
```

3. Verwenden Sie `git commit --amend`, um den Inhalt des letzten Commits zu aktualisieren, ohne die Commit-Nachricht zu ändern:

```shell
git commit --amend --allow-empty
```

Wenn der Commit nach dem Löschen der Datei ein leerer Commit ist, verwenden Sie `--allow-empty`, andernfalls können Sie es weglassen.

Nach Ausführung dieser Befehle wird die Datei `file2.txt` aus dem letzten Commit entfernt, ohne die Commit-Nachricht zu ändern.

Dies ist, was passiert, wenn Sie `file2.txt` aus der Git-Versionskontrolle entfernen:

```shell
On branch master

Changes to be committed:
(use "git restore --staged <file>..." to unstage)
deleted: file2.txt

Untracked files:
(use "git add <file>..." to include in what will be committed)
file2.txt
```
