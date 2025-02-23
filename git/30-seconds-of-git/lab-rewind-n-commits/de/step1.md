# Commits rückgängig machen

Als Entwickler haben Sie an einem Projekt gearbeitet und mehrere Commits durchgeführt. Allerdings stellen Sie fest, dass die letzten paar Commits Fehler enthalten und Sie zu einer früheren Version Ihres Codes zurückkehren müssen. Sie müssen Git verwenden, um Ihre Commits rückgängig zu machen und zur vorherigen Version Ihres Codes zurückzukehren.

Um diesen Lab zu absolvieren, verwenden Sie das Git-Repository `git-playground` aus Ihrem GitHub-Konto, das von einem Fork von `https://github.com/labex-labs/git-playground.git` stammt. Folgen Sie diesen Schritten:

1. Klonen Sie das Repository auf Ihren lokalen Computer:

```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
```

2. Erstellen Sie einen neuen Branch namens `rewind-commits`:

```shell
git checkout -b rewind-commits
```

3. Zeigen Sie den Commit-Verlauf des Repositories an und erkennen Sie, dass der letzte Commit Fehler enthält und Sie zu einer früheren Version Ihres Codes zurückkehren müssen:

```shell
git log
```

4. Verwenden Sie Git, um Ihre Commits um 1 rückgängig zu machen:

```shell
git reset HEAD~1 --hard
```

5. Vergewissern Sie sich, dass Sie Ihre Commits erfolgreich rückgängig gemacht haben:

```shell
git log
```

6. Stellen Sie Ihre Änderungen auf den Branch `rewind-commits` hoch:

```shell
git push --force origin rewind-commits
```

Dies ist das Endresultat:

```shell
cf80005 (HEAD -> rewind-commits, origin/rewind-commits) Added file1.txt
b00b937 Initial commit
```
