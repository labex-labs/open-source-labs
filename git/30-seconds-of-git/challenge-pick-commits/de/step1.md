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

ADD hello.txt
```
