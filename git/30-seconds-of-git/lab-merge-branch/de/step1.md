# Ein Branch zusammenführen

Ihre Aufgabe besteht darin, einen Branch mit Git in den aktuellen Branch zu mergen. Dazu müssen Sie in den Zielbranch wechseln und dann den Quellbranch in ihn zusammenführen. Dies kann nützlich sein, wenn Sie Änderungen aus einem `feature-branch-A`-Branch in den `master`-Branch Ihres Projekts kombinieren möchten.

Für diese Übung verwenden wir das Repository von `https://github.com/labex-labs/git-playground`. Folgen Sie diesen Schritten, um den `feature-branch-A` in den `master`-Branch zu mergen:

1. Klonen Sie das Repository, navigieren Sie zum Verzeichnis und konfigurieren Sie die Identität:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Erstellen Sie einen `feature-branch-A`-Branch. Wechseln Sie zu ihm:

```shell
git checkout -b feature-branch-A
```

3. Fügen Sie "hello,world" zur `file2.txt`-Datei hinzu, fügen Sie sie zum Staging-Bereich hinzu und bestätigen Sie sie mit der Nachricht "fix file2.txt":

```shell
echo "hello,world" >> file2.txt
git add.
git commit -m "fix file2.txt"
```

4. Wechseln Sie zum `master`-Branch:

```shell
git checkout master
```

5. Führen Sie den `feature-branch-A` in den `master`-Branch zusammen:

```shell
git merge feature-branch-A
```

6. Beheben Sie alle Konflikte, die während des Zusammenführungsvorgangs auftreten können.

Dies ist das Ergebnis von `git log`:

```shell
commit e2b80358ae6e4c3b8439cf111a4672a188739290 (HEAD -> master, feature-branch-A)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 18:51:00 2023 +0800

    fix file2.txt
```
