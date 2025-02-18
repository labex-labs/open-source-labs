# Git Cherry-Pick

Als Entwickler arbeitest du an einem Projekt mit mehreren Branches. Du hast eine bestimmte Änderung identifiziert, die in einem früheren Commit vorgenommen wurde und die du auf deinen aktuellen Branch anwenden möchtest. Allerdings möchtest du nicht den gesamten Branch zusammenführen (merge), da er andere Änderungen enthält, die du nicht benötigst. In diesem Szenario kannst du den Befehl `git cherry-pick` verwenden, um die spezifische Änderung auf deinen aktuellen Branch anzuwenden.

Für dieses Lab verwenden wir das Repository von `https://github.com/labex-labs/git-playground`. Befolge die folgenden Schritte, um die Herausforderung abzuschließen:

1. Klone das Repository, navigiere in das Verzeichnis und konfiguriere die Identität:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Erstelle einen Branch namens `one-branch` und wechsle zu ihm, erstelle eine Datei namens `hello.txt`, schreibe "hello,world" hinein, füge sie zur Staging-Area hinzu und committe sie mit der Nachricht "add hello.txt":

```shell
git checkout -b one-branch
echo "hello,world" > hello.txt
git add.
git commit -m "add hello.txt"
```

3. Identifiziere den Hash des im vorherigen Schritt erstellten Commits, um ihn auf den `master`-Branch anzuwenden:

```shell
git log
```

4. Wechsle zum `master`-Branch und wende die Änderung auf den `master`-Branch an:

```shell
git checkout master
git cherry-pick 1609c283ec86ee4
```

5. Überprüfe, ob die Änderung auf den `master`-Branch angewendet wurde:

```shell
git log
```

Dies ist das Ergebnis des Ausführens von `git log` auf dem `master`-Branch:

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
