# Deaktiviere das schnelle Zusammenführen

Standardmäßig verwendet Git das schnelle Zusammenführen, um Branches zusammenzuführen, die keine divergierenden Commits aufweisen. Dies bedeutet, dass wenn Sie einen Branch haben, in dem keine neuen Commits vorliegen, Git einfach den Zeiger des Branches, in den Sie zusammenführen, auf den neuesten Commit des Branches setzen, aus dem Sie zusammenführen. Während dies in einigen Fällen nützlich sein kann, kann es auch Probleme verursachen, insbesondere wenn an größeren Projekten mit mehreren Mitwirkenden gearbeitet wird. Beispielsweise können Konflikte entstehen, die schwer zu beheben sind, wenn zwei Entwickler am selben Branch arbeiten und beide Änderungen vornehmen.

Um das schnelle Zusammenführen zu deaktivieren, verwenden wir das Repository von `https://github.com/labex-labs/git-playground`.

1. Klone das Repository, navigiere zum Verzeichnis und konfiguriere die Identität:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Erstelle und wechsle zu einem Branch namens `my-branch`, erstelle eine Datei `hello.txt` und füge "hello,world" hinzu, füge sie zum Staging-Bereich hinzu und commite sie mit der Nachricht "Added hello.txt":

```shell
git checkout -b my-branch
echo "hello,world" > hello.txt
git add.
git commit -m "Added hello.txt"
```

3. Führe den folgenden Befehl aus, um das schnelle Zusammenführen zu deaktivieren:

```shell
git config --add merge.ff false
```

Dies deaktiviert das schnelle Zusammenführen für alle Branches, auch wenn es möglich wäre. Sie können das `--global`-Flag verwenden, um diese Option global zu konfigurieren:

```shell
git config --global --add merge.ff false
```

4. Wechsel zurück zum `mater`-Branch und merke den `my-branch`-Branch zusammen, speichere und beende ohne den Text zu ändern:

```shell
git checkout master
git merge my-branch
```

Jetzt wird Git immer einen Merge-Commit erstellen, auch wenn es möglich wäre, ein schnelles Zusammenführen durchzuführen:

```shell
commit 6e17a776ab51a89ace069614b0caf1c07915a92c (HEAD -> master)
Merge: ec5ea6d 6d7de91
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Mon Jul 17 13:30:44 2023 +0800

    Merge branch'my-branch'
```
