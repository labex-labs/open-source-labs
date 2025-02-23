# Zurückspringen zu einem bestimmten Commit

Als Entwickler müssen Sie möglicherweise Änderungen an Ihrer Codebasis rückgängig machen. Beispielsweise haben Sie einen Fehler gemacht und müssen zu einer früheren Version Ihres Codes zurückkehren. In dieser Herausforderung verwenden Sie Git, um zurück zu einem bestimmten Commit in einem Repository zu springen.

Um dieses Lab zu absolvieren, verwenden Sie das Git-Repository `git-playground` von `https://github.com/labex-labs/git-playground.git`. Folgen Sie diesen Schritten, um die Herausforderung zu beenden:

1. Klonen Sie das Repository auf Ihren lokalen Computer:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Navigieren Sie zum Repository:

```shell
cd git-playground
```

3. Zeigen Sie die Commit-Historie des Repositories an:

```shell
git log --oneline
```

4. Stellen Sie sicher, dass die Commit-Nachricht, zu der Sie zurückspringen möchten, der Commit-Hash des "Initial commit" ist.
5. Verwenden Sie den Befehl `git reset <commit>`, um zurück zum angegebenen Commit zu springen. Beispielsweise möchten Sie zurück zum Commit mit dem Hash `3050fc0d3` springen:

```shell
git reset 3050fc0d3
```

6. Zeigen Sie erneut die Commit-Historie des Repositories an:

```shell
git log --oneline
```

7. Wenn Sie die Änderungen löschen und zu der früheren Version Ihres Codes zurückkehren möchten, verwenden Sie den Befehl `git reset --hard <commit>`. Beispielsweise möchten Sie die Änderungen löschen und zu dem Commit mit dem Hash `c0d30f305` zurückkehren:

```shell
git reset --hard c0d30f305
```

Dies ist das Ergebnis von `git log --oneline`:

```shell
c0d30f305 (HEAD -> master) Initial commit
```
