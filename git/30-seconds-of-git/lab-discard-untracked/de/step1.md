# Unüberwachte Änderungen verwerfen

Sie arbeiten an einem Projekt mit Git und haben einige Änderungen an Ihrem Arbeitsverzeichnis vorgenommen. Sie stellen jedoch fest, dass Sie diese Änderungen nicht benötigen und möchten sie verwerfen. Sie möchten alle unüberwachten Änderungen an der aktuellen Branch verwerfen.

Um dieses Lab zu absolvieren, verwenden Sie das Git-Repository unter `https://github.com/labex-labs/git-playground`. Folgen Sie diesen Schritten:

1. Navigieren Sie zum Repository-Verzeichnis:

```shell
cd git-playground
```

2. Überprüfen Sie den Status Ihres Arbeitsverzeichnisses:

```shell
git status
```

Sie sollten die folgende Ausgabe sehen:

```shell
[object Object]
```

3. Verwerfen Sie alle unüberwachten Änderungen an der aktuellen Branch:

```shell
git clean -f -d
```

4. Überprüfen Sie erneut den Status Ihres Arbeitsverzeichnisses:

```shell
git status
```

Sie sollten die folgende Ausgabe sehen:

```shell
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```

Der Befehl `git clean -f -d` hat alle unüberwachten Änderungen an der aktuellen Branch verworfen.
