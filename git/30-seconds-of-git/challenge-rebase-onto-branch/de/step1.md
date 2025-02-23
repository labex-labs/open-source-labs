# Umstellen auf eine andere Branch

Als Entwickler arbeitest du an einem Projekt mit mehreren Branches. Du hast Änderungen an deiner Branch vorgenommen und möchtest diese Änderungen in eine andere Branch integrieren. Du möchtest jedoch nicht die Branches zusammenführen, da du einen sauberen und linearen Verlauf aufrechterhalten möchtest.

## Aufgaben

Für diese Herausforderung verwenden wir das Repository von `https://github.com/labex-labs/git-playground`.

1. Navigiere zum Verzeichnis und konfiguriere die Identität.
2. Erstelle und wechsle zu einer Branch namens `one-branch`.
3. Füge "hello,world" zur Datei `README.md` hinzu, füge es zum Staging-Area hinzu und commite es mit der Nachricht "Added some changes to README.md".
4. Wechsle zur `master`-Branch.
5. Stelle sicher, dass deine lokale `master`-Branch mit dem Remote-Repository aktuell ist.
6. Stelle die `one-branch` auf die `master`-Branch um.
7. Behandle alle Konflikte, die während des Umstellprozesses auftauchen.

Dies ist das Ergebnis von `git log`:

```shell
commit eccff423dd6bf5335f76f2f364fa3b95130ff805 (HEAD -> master, one-branch)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Sat Jul 22 23:10:04 2023 +0800

    Added some changes to README.md
```
