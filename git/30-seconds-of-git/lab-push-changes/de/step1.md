# Lokale Änderungen an Remote pushen

Als Entwickler musst du möglicherweise deine lokalen Änderungen in ein Remote-Repository pushen, um deine Arbeit mit anderen Teammitgliedern zu teilen oder deinen Code in eine Produktionsumgebung zu deployen. Der Befehl `git push` wird verwendet, um die neuesten Änderungen von der lokalen Branch in das Remote zu pushen. Bevor du die Änderungen jedoch pushen, musst du sicherstellen, dass deine lokale Branch mit der Remote-Branch aktuell ist. Wenn es Konflikte zwischen der lokalen und der Remote-Branch gibt, musst du sie vor dem Pushen der Änderungen auflösen.

Um diese Übung abzuschließen, wirst du das Git-Repository `git-playground` aus deinem GitHub-Account verwenden, das von einem Fork von `https://github.com/labex-labs/git-playground.git` stammt. Du hast einige Änderungen an der `master`-Branch vorgenommen und möchtest sie in das Remote-Repository pushen. Hier sind die Schritte, die du befolgen musst:

1. Klone das Repository auf deinen lokalen Computer und navigiere in das Verzeichnis, indem du die folgenden Befehle ausführst:

```shell
git clone https://github.com/your-username/git-playground
cd git-playground
```

2. Stelle sicher, dass deine lokale Branch mit der Remote-Branch aktuell ist, indem du folgenden Befehl ausführst:

```shell
git pull origin master
```

3. Nachdem du die neuesten Änderungen von der Remote-Branch heruntergeladen hast, kannst du deine Änderungen an der lokalen Branch vornehmen:

```shell
echo "hello,world" >> file1.txt
```

4. Nachdem du die Änderungen vorgenommen hast, stagiere sie mit dem Befehl `git add`:

```shell
git add.
```

5. Bestätige die Änderungen mit dem Befehl `git commit`:

```shell
git commit -m "Added new feature"
```

6. Schließlich pushe die Änderungen in das Remote-Repository mit dem Befehl `git push`:

```shell
git push origin master
```

Dies ist das Ergebnis von `git log`:

```shell
commit 1f1949955387a1549f1bb5286d3d0a2b993f87e0 (HEAD -> master,origin/master,origin/HEAD)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 19:26:57 2023 +0800

    Added new feature
```
