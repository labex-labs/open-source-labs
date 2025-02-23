# Lokale Änderungen an Remote pushen

Als Entwickler musst du möglicherweise deine lokalen Änderungen in ein Remote-Repository pushen, um deine Arbeit mit anderen Teammitgliedern zu teilen oder deinen Code in eine Produktionsumgebung zu deployen. Bevor du die Änderungen pushen, musst du jedoch sicherstellen, dass deine lokale Branch mit der Remote-Branch aktuell ist. Wenn es Konflikte zwischen der lokalen und der Remote-Branch gibt, musst du sie vor dem Pushen der Änderungen auflösen.

## Aufgaben

Um diese Herausforderung zu bewältigen, verwendest du das Git-Repository `git-playground` aus deinem GitHub-Account, das von einem Fork von `https://github.com/labex-labs/git-playground.git` stammt. Du hast einige Änderungen an der `master`-Branch vorgenommen und möchtest sie in das Remote-Repository pushen.

1. Klone das Repository auf deinen lokalen Computer von `https://github.com/your-username/git-playground`, navigiere zum Verzeichnis und konfiguriere die Identität.
2. Stelle sicher, dass deine lokale Branch mit der Remote-Branch aktuell ist.
3. Nachdem du die neuesten Änderungen von der Remote-Branch abgerufen hast, kannst du in der `file1.txt`-Datei auf der `master`-Branch "hello,world" schreiben, die Änderungen zur Staging-Area hinzufügen und sie mit der Nachricht "Added new feature " committen.
4. Schließe schließlich die Änderungen in das Remote-Repository pushen.

Dies ist das Ergebnis von `git log`:

```shell
commit 1f1949955387a1549f1bb5286d3d0a2b993f87e0 (HEAD -> master,origin/master,origin/HEAD)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 19:26:57 2023 +0800

    Added new feature
```
