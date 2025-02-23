# Abrufen der neuesten Änderungen aus Remote

Angenommen, Sie arbeiten an einem Projekt mit einem Entwicklerteam, und das Projekt ist in einem Remote-Repository gespeichert. Sie möchten die neuesten Änderungen aus dem Remote-Repository abrufen, ohne sie auf Ihr lokales Repository anzuwenden. Hier kommt der Befehl `git fetch` sehr praktisch zum Einsatz.

Der Befehl `git fetch` lädt die neuesten Änderungen aus dem Remote-Repository in Ihr lokales Repository herunter, wendet sie jedoch nicht auf Ihr Arbeitsverzeichnis an. Dies bedeutet, dass Sie die Änderungen prüfen können, bevor Sie sie in Ihr lokales Repository zusammenführen.

Um zu demonstrieren, wie man die neuesten Änderungen aus einem Remote-Repository abruft, werden wir das Git-Repository `git-playground` aus Ihrem GitHub-Account verwenden, das von einem Fork von `https://github.com/labex-labs/git-playground.git` stammt. Folgen Sie den Schritten unten:

1. Klonen Sie das Repository und navigieren Sie zum Verzeichnis:

```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
```

2. Finden Sie das Repository `git-playground` in Ihrem Konto auf der Github-Website, erstellen Sie und wechseln Sie zu einer Branch namens `fetch-branch`, erstellen Sie eine Datei namens `hello.txt`, fügen Sie "hello, world" hinzu und bestätigen Sie mit der Nachricht "Create hello.txt".
3. Zeigen Sie die Branches in Remote-Repositorys an:

```shell
git branch -r
```

4. Abrufen Sie die neuesten Änderungen aus dem Remote-Repository:

```shell
git fetch
```

5. Zeigen Sie erneut die Branches in Remote-Repositorys an und vergewissern Sie sich, dass die neuesten Änderungen abgerufen wurden:

```shell
git branch -r
git log origin/fetch-branch
```

Dies wird Ihnen die neuesten Commits auf der Branch `origin/fetch-branch` anzeigen. Dies ist das Ergebnis von `git log origin/fetch-branch`:

```shell
commit f3125b4c99e0ef2ce58bc0b1287c966c9e68c577 (origin/fetch-branch)
Author: xiaoshengyunan <131872312+xiaoshengyunan@users.noreply.github.com>
Date:   Thu Jul 20 20:17:23 2023 +0800

    Create hello.txt
```
