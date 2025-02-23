# Dateien zum Staging-Bereich hinzufügen

Sie haben an einem Projekt gearbeitet, das in einem Git-Repository namens `https://github.com/labex-labs/git-playground` gespeichert ist. Sie haben einige Änderungen an der Codebasis vorgenommen und möchten diese Änderungen in das Repository committen. Allerdings möchten Sie nur bestimmte Änderungen committen und nicht alle Änderungen, die Sie vorgenommen haben. Um dies zu tun, müssen Sie die Dateien in den Staging-Bereich hinzufügen.

1. Sie werden einige Änderungen im Verzeichnis `git-playground` vornehmen:

```shell
echo "hello" > index.html
echo "world" > style.css
echo "git" > one.js
echo "labex" > two.js
echo "hello git" > 1.py
echo "hello labex" > 2.py
```

2. Fügen Sie diese Dateien in den Staging-Bereich hinzu:

```shell
git add index.html style.css
```

3. Zeigen Sie den Status des aktuellen Arbeitsverzeichnisses und des Staging-Bereichs an, einschließlich Informationen darüber, welche Dateien geändert wurden, welche Dateien in den Staging-Bereich hinzugefügt wurden usw.:

```shell
git status
```

4. Alternativ können Sie alle Dateien mit einer `.js`-Erweiterung hinzufügen:

```shell
git add *.js
```

5. Zeigen Sie erneut den Status des aktuellen Arbeitsverzeichnisses und des Staging-Bereichs an:

```shell
git status
```

6. Sie können auch alle Änderungen in den Staging-Bereich hinzufügen:

```shell
git add.
```

7. Zeigen Sie erneut den Status des aktuellen Arbeitsverzeichnisses und des Staging-Bereichs an:

```shell
git status
```

Dies ist das fertige Ergebnis:

![Git staging area status](../assets/challenge-stage-files-step1-1.png)
