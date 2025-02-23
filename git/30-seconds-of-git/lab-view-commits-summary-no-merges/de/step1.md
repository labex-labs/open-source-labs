# Zeigen Sie einen kurzen Überblick über die Commits ohne Merge-Commits

Sie arbeiten an einem Projekt mit mehreren anderen Entwicklern und möchten einen Überblick über alle Commits im Repository erhalten. Sie möchten jedoch keine Merge-Commits sehen, da diese keine tatsächlichen Änderungen am Code enthalten. Wie können Sie einen Überblick über alle Commits ohne Merge-Commits anzeigen?

Für dieses Lab verwenden wir das Repository von `https://github.com/labex-labs/git-playground`.

1. Klonen Sie das Repository, navigieren Sie zum Verzeichnis und konfigurieren Sie die Identität:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Erstellen Sie und wechseln Sie zu einer Branch namens `feature1`, erstellen Sie eine Datei namens `file.txt` und schreiben Sie `Feature 1` hinein, fügen Sie sie zum Staging-Area hinzu und committen Sie sie mit der Nachricht "Add feature 1":

```shell
git checkout -b feature1
echo "Feature 1" >> file.txt
git add.
git commit -m "Add feature 1"
```

3. Wechseln Sie zurück zur `master`-Branch, verschmelzen Sie die `feature1`-Branch, deaktivieren Sie das Vorwärts-Verschmelzen, speichern Sie und beenden Sie ohne den Text zu ändern:

```shell
git checkout master
git merge --no-ff feature1
```

4. Zeigen Sie einen kurzen Überblick über alle Commits ohne Merge-Commits:

```shell
git log --oneline --no-merges
```

Dies wird eine Liste aller Commits im Repository ausgeben, ohne jegliche Merge-Commits. Die Ausgabe sieht ungefähr so aus:

```shell
430b986 (feature1) Add feature 1
d22f46b (origin/master, origin/HEAD) Added file2.txt
cf80005 Added file1.txt
b00b937 Initial commit
```
