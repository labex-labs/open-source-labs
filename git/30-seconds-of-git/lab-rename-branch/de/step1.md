# Einen Branch umbenennen

Als Entwickler musst du aus verschiedenen Gründen möglicherweise einen Branch umbenennen, etwa um ihn beschreibender zu gestalten oder um einer Namenskonvention zu folgen. Ein Branch umzubenennen kann eine einfache Aufgabe sein, erfordert aber einige Kenntnisse über Git-Befehle. In dieser Herausforderung wirst du lernen, wie du einen Branch mit Git umbenennst.

Für diese Übung verwenden wir das Git-Repository unter `https://github.com/labex-labs/git-playground`.

Angenommen, du erstellst einen Branch namens `old-branch`, um an einer neuen Funktion zu arbeiten. Nachdem du die Funktion abgeschlossen hast, stellst du fest, dass der Branchname nicht ausreichend beschreibend ist. Du möchtest den Branch in `new-branch` umbenennen, um ihn sinnvoller zu gestalten. Um den Branch umzubenennen, folge diesen Schritten:

1. Öffne das Terminal und navigiere zum Verzeichnis des lokalen Repositories.
2. Verwende den Befehl `git checkout -b old-branch`, um einen Branch namens `old-branch` zu erstellen, und den Befehl `git branch -m <old-name> <new-name>`, um den Branch umzubenennen. Im Beispiel wäre der Befehl `git branch -m old-branch new-branch`.
3. Verifiziere, dass der Branch umbenannt wurde, indem du den Befehl `git branch` verwendest.

Die Ausgabe sollte den neuen Branchnamen anzeigen:

```shell
master
* new-branch
```
