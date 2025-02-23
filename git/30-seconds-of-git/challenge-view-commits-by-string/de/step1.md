# Commits finden, die einen bestimmten String manipuliert haben

Als Entwickler müssen Sie möglicherweise alle Commits finden, die in Ihrer Codebasis einen bestimmten String geändert haben. Beispielsweise möchten Sie alle Commits finden, die einen bestimmten Funktionsnamen oder Variablen hinzugefügt oder entfernt haben. Dies kann hilfreich sein, wenn Sie Probleme debuggen oder die Quelle eines Fehlers aufspüren.

## Aufgaben

Angenommen, Sie arbeiten an einem Projekt auf GitHub namens `git-playground`. Sie möchten alle Commits finden, die den String "Git Playground" in der Datei `README.md` geändert haben. Hier ist, wie Sie es tun können:

1. Navigieren Sie zum Repository-Verzeichnis.
2. Finden Sie alle Commits, die den String "Git Playground" in der Datei `README.md` geändert haben, und verwenden Sie die Pfeiltasten, um durch die Liste der Commits zu navigieren. Drücken Sie <kbd>Q</kbd>, um den Log zu verlassen.

Git wird eine Liste aller Commits ausgeben, die den String "Git Playground" in der Datei `README.md` geändert haben:

```shell
commit b00b9374a7c549d1af111aa777fdcc868d8a2a01
Author: Hang <huhuhang@gmail.com>
Date:   Wed Apr 26 14:16:00 2023 +0800

    Initial commit
```
