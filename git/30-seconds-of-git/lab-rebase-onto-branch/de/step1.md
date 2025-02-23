# Umstellen auf eine andere Branch

Als Entwickler arbeitest du an einem Projekt mit mehreren Branches. Du hast Änderungen an deiner Branch vorgenommen und möchtest diese Änderungen in eine andere Branch integrieren. Du willst jedoch nicht die Branches zusammenführen, da du einen sauberen und linearen Verlauf aufrechterhalten möchtest. In diesem Fall kannst du den Befehl `git rebase` verwenden, um deine Branch auf eine andere Branch umzustellen.

Für dieses Lab verwenden wir das Repository von `https://github.com/labex-labs/git-playground`. Folgen Sie den Schritten unten, um das Lab abzuschließen:

1. Klonen Sie das Repository, navigieren Sie zum Verzeichnis und konfigurieren Sie die Identität:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Erstellen Sie und wechseln Sie zu einer Branch namens `one-branch`:

```shell
git checkout -b one-branch
```

3. Fügen Sie "hello,world" zur Datei `README.md` hinzu, fügen Sie es zum Staging-Area hinzu und bestätigen Sie es mit der Nachricht "Added some changes to README.md":

```shell
echo "hello,world" >> README.md
git add.
git commit -am "Added some changes to README.md"
```

4. Wechseln Sie zur `master`-Branch:

```shell
git checkout master
```

5. Stellen Sie sicher, dass Ihre lokale `master`-Branch mit dem Remote-Repository aktuell ist:

```shell
git pull
```

6. Stellen Sie die `one-branch` auf die `master`-Branch um:

```shell
git rebase one-branch
```

7. Beheben Sie alle Konflikte, die während des Umstellprozesses auftreten.

Dies ist das Ergebnis von `git log`:

```shell
commit eccff423dd6bf5335f76f2f364fa3b95130ff805 (HEAD -> master, one-branch)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Sat Jul 22 23:10:04 2023 +0800

    Added some changes to README.md
```
