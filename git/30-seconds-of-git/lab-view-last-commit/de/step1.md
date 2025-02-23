# Letzten Commit anzeigen

Sie arbeiten an einem Projekt mit einem Team von Entwicklern und müssen den letzten Commit an das Git-Repository des Projekts anzeigen. Sie möchten die Details des Commits sehen, einschließlich der Commit-Nachricht, des Autors und des Datums.

Führen Sie zum Anzeigen des letzten Commits an einem Git-Repository die folgenden Schritte aus:

1. Öffnen Sie das Terminal auf Ihrem Computer.
2. Navigieren Sie zum Verzeichnis, in dem das Git-Repository gespeichert ist:

```shell
cd git-playground
```

3. Zeigen Sie den letzten Commit an:

```shell
git log -1
```

Die Ausgabe zeigt Ihnen die Details des letzten Commits, einschließlich der Commit-Nachricht, des Autors und des Datums:

```shell
commit d22f46ba8c2d4e07d773c5126e9c803933eb5898 (HEAD -> master, origin/master, origin/feature-branch, origin/HEAD)
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt
```
