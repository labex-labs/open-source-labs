# Git Cherry-Pick

Als Entwickler arbeitest du an einem Projekt mit mehreren Branches. Du hast eine spezifische Änderung identifiziert, die in einem früheren Commit vorgenommen wurde und die du auf deinen aktuellen Branch anwenden möchtest. Allerdings möchtest du nicht den gesamten Branch zusammenführen, da er andere Änderungen enthält, die du nicht benötigst.

## Aufgaben

Für diese Herausforderung verwenden wir das Repository von `https://github.com/labex-labs/git-playground`.

1. Navigiere zum Verzeichnis und konfiguriere die Identität.
2. Erstelle und wechsle zu einem Branch namens `one-branch`, erstelle eine Datei namens `hello.txt`, schreibe "hello,world" darin, füge sie zum Staging-Area hinzu und commite sie mit der Nachricht "add hello.txt".
3. Identifiziere den Hash des Commits, der im vorherigen Schritt erstellt wurde, um ihn auf den `master`-Branch anzuwenden.
4. Wechsel zum `master`-Branch und wende die Änderung auf den `master`-Branch an.
5. Verifiziere, dass die Änderung auf den `master`-Branch angewendet wurde.

Dies ist das Ergebnis von `git log` auf dem `master`-Branch:

```shell
commit e2f3c6af9570f4eac2580dea93ca8133f1547d53 (HEAD -> master)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Sat Jul 15 14:30:31 2023 +0800

    add hello.txt

commit d22f46ba8c2d4e07d773c5126e9c803933eb5898 (origin/master, origin/HEAD)
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt

commit cf80005e40a3c661eb212fcea5fad06f8283f08f
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file1.txt

commit b00b9374a7c549d1af111aa777fdcc868d8a2a01
Author: Hang <huhuhang@gmail.com>
Date:   Wed Apr 26 14:16:00 2023 +0800

    Initial commit
```
