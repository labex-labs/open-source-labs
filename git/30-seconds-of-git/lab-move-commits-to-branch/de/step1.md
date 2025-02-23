# Commits zu einem neuen Branch verschieben

Für dieses Lab verwenden wir das Repository von `https://github.com/labex-labs/git-playground`. Sie haben an einem Projekt am `master`-Branch gearbeitet. Sie stellen fest, dass einige der Änderungen, die Sie vorgenommen haben, an einem separaten Branch vorgenommen werden sollten. Sie möchten diese Änderungen auf einen neuen Branch namens `feature` verschieben.

1. Klonen Sie das Repository, navigieren Sie zum Verzeichnis und konfigurieren Sie die Identität:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Wechseln Sie zum `master`-Branch:

```shell
git checkout master
```

3. Erstellen Sie eine Datei namens `hello.txt`, fügen Sie "hello, world" hinzu, fügen Sie sie zum Staging-Area hinzu und übermitteln Sie sie mit der Nachricht "Added hello.txt":

```shell
echo "hello,world" >> hello.txt
git add.
git commit -m "Added hello.txt"
```

4. Erstellen Sie einen neuen Branch namens `feature` ohne zu wechseln. Wenn Sie einen neuen Branch am `master`-Branch erstellen, ist der Zustand des neuen Branches der gleiche wie der des `master`-Branches, d.h., die Dateien im neuen Branch sind die gleichen wie die Dateien im `master`-Branch, mit dem gleichen Inhalt und der gleichen Versionsgeschichte:

```shell
git branch feature
```

5. Stornieren Sie den letzten Commit am `master`:

```shell
git reset HEAD~1 --hard
```

6. Überprüfen Sie den Commit-Verlauf am `master`-Branch und den Commit-Verlauf am `feature`-Branch, um die Ergebnisse zu verifizieren:

```shell
git log
git checkout feature
git log
```

Dies ist das Ergebnis von `git log`:

```shell
commit 7969ab5d6606e2a40c9fd826c732206b835976e9 (HEAD -> feature)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 20:19:22 2023 +0800

    Added hello.txt
```
