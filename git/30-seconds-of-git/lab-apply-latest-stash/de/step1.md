# Den neuesten Stash anwenden

Sie arbeiten an einem Projekt in Ihrem Git-Repository und haben einige Änderungen vorgenommen, die noch nicht zum Committen bereit sind. Sie müssen jedoch zu einer anderen Branch oder einem anderen Commit wechseln, um an einer anderen Funktion zu arbeiten. Sie möchten Ihre Änderungen nicht verlieren, also entscheiden Sie sich, sie zu stashen. Später, wenn Sie bereit sind, mit Ihren Änderungen fortzufahren, müssen Sie den neuesten Stash auf Ihr Arbeitsverzeichnis anwenden.

Führen Sie die folgenden Schritte aus, um den neuesten Stash auf Ihr Git-Repository anzuwenden:

1. Klonen Sie das Git-Repository mit dem Namen `https://github.com/labex-labs/git-playground` auf Ihren lokalen Computer.
2. Navigieren Sie zum Verzeichnis `git-playground`.
3. Machen Sie einige Änderungen an der Datei `README.md`, z. B. schreiben Sie "Dies ist eine neue Zeile" in die Datei `README.md`.
4. Führen Sie den Befehl `git stash` aus, um Ihre Änderungen zu stashen.
5. Führen Sie den Befehl `git stash list` aus, um eine Liste Ihrer Stashes zu sehen. Sie sollten in der Liste einen Stash sehen.
6. Führen Sie den Befehl `git stash apply` aus, um den neuesten Stash auf Ihr Arbeitsverzeichnis anzuwenden.
7. Überprüfen Sie die Datei `README.md`, um zu sehen, dass Ihre Änderungen angewendet wurden.

```shell
git clone https://github.com/labex-labs/git-playground.git
cd git-playground
echo "This is a new line" >> README.md
git stash
git stash list
git stash apply
cat README.md
```

Dies ist das Ergebnis von `cat README.md`:

```shell
# git-playground
Git Playground
This is a new line
```
