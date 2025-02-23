# Aktuelle Änderungen aus Remote abrufen

Angenommen, Sie arbeiten an einem Projekt mit einem Team von Entwicklern, und das Projekt ist in einem Remote-Repository gespeichert. Sie möchten die neuesten Änderungen aus dem Remote-Repository abrufen, ohne sie auf Ihr lokales Repository anzuwenden.

## Aufgaben

Um zu demonstrieren, wie man die neuesten Änderungen aus einem Remote-Repository abruft, verwenden wir das Git-Repository `git-playground` aus Ihrem GitHub-Konto, das von einem Fork von `https://github.com/labex-labs/git-playground.git` stammt.

1. Klonen Sie das Repository und navigieren Sie zum Verzeichnis.
2. Finden Sie das Repository `git-playground` in Ihrem Konto auf der Github-Website, erstellen und wechseln Sie zu einem Branch namens `fetch-branch`, erstellen Sie eine Datei namens `hello.txt`, fügen Sie "hello, world" hinzu und bestätigen Sie mit der Nachricht "Create hello.txt".
3. Zeigen Sie die Branches in Remote-Repositorys an.
4. Ruft die neuesten Änderungen aus dem Remote-Repository ab.
5. Zeigen Sie erneut die Branches in Remote-Repositorys an und vergewissern Sie sich, dass die neuesten Änderungen abgerufen wurden.

Dies ist das Ergebnis von `git log origin/fetch-branch`:

```shell
commit f3125b4c99e0ef2ce58bc0b1287c966c9e68c577 (origin/fetch-branch)
Author: xiaoshengyunan <131872312+xiaoshengyunan@users.noreply.github.com>
Date:   Thu Jul 20 20:17:23 2023 +0800

    Create hello.txt
```
