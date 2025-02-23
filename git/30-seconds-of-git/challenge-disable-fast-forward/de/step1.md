# Deaktiviere das schnelle Zusammenführen

Standardmäßig verwendet Git das schnelle Zusammenführen, um Branches zusammenzuführen, die keine divergierenden Commits aufweisen. Dies bedeutet, dass wenn Sie einen Branch haben, der keine neuen Commits enthält, Git einfach den Zeiger des Branches, in den Sie zusammenführen, auf den neuesten Commit des Branches, aus dem Sie zusammenführen, verschieben wird. Während dies in einigen Fällen nützlich sein kann, kann es auch Probleme verursachen, insbesondere wenn an größeren Projekten mit mehreren Mitwirkenden gearbeitet wird. Beispielsweise können Konflikte entstehen, die schwer zu beheben sind, wenn zwei Entwickler am selben Branch arbeiten und beide Änderungen vornehmen.

## Aufgaben

Um das schnelle Zusammenführen zu deaktivieren, verwenden wir das Repository von `https://github.com/labex-labs/git-playground`.

1. Navigieren Sie zum Verzeichnis und konfigurieren Sie die Identität.
2. Erstellen Sie und wechseln Sie zu einem Branch namens `my-branch`, erstellen Sie eine Datei `hello.txt` und fügen Sie "hello,world" hinzu, fügen Sie sie zum Staging-Area hinzu und bestätigen Sie sie mit der Nachricht "Added hello.txt".
3. Deaktivieren Sie das schnelle Zusammenführen für alle Branches.
4. Wechseln Sie zurück zum `mater`-Branch und verschieben Sie den `my-branch`-Branch, speichern Sie und beenden Sie ohne den Text zu ändern.

Jetzt wird Git immer einen Merge-Commit erstellen, auch wenn es möglich wäre, das schnelle Zusammenführen durchzuführen:

```shell
commit 6e17a776ab51a89ace069614b0caf1c07915a92c (HEAD -> master)
Merge: ec5ea6d 6d7de91
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Mon Jul 17 13:30:44 2023 +0800

    Merge branch'my-branch'
```
