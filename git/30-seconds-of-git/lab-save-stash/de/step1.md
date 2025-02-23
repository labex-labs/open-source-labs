# Erstellen eines Git-Stashes

Als Entwickler können Sie sich in einer Situation befinden, in der Sie zu einem anderen Branch wechseln oder an einer anderen Funktion arbeiten müssen, aber Ihre Änderungen noch nicht committen möchten. Sie möchten Ihren Fortschritt nicht verlieren, aber Sie möchten auch keine unvollständige oder fehlerhafte Code committen. Hier kommt ein Stash sehr praktisch zum Einsatz.

Ein Stash ermöglicht es Ihnen, Ihre Änderungen zu speichern, ohne sie zu committen, sodass Sie zu einem anderen Branch wechseln oder an einer anderen Funktion arbeiten können. Sie können dann Ihren Stash später anwenden, wenn Sie bereit sind, fortzufahren und Ihre Änderungen fertigzustellen.

Um einen Stash zu erstellen, können Sie den Befehl `git stash save` verwenden. Angenommen, Sie arbeiten an einem Branch namens `feature` im Repository `git-playground` und möchten Ihre Änderungen speichern, bevor Sie zu einem anderen Branch wechseln:

1. Navigieren Sie zunächst zum Verzeichnis `git-playground`:

```shell
cd git-playground
```

2. Wechseln Sie zu einem Branch namens `feature`:

```shell
git checkout -b feature
```

3. Machen Sie einige Änderungen an den Dateien im Verzeichnis:

```shell
echo "Some changes" >> README.md
```

4. Speichern Sie Ihre Änderungen in einem Stash:

```shell
git stash save "My changes"
```

5. Wechseln Sie zu einem anderen Branch:

```shell
git checkout master
```

6. Wenn Sie mit den Änderungen am anderen Branch fertig sind, wechseln Sie zurück zum Branch `feature` und wenden Sie Ihren Stash an:

```shell
git stash apply
```

Dies ist das fertige Ergebnis:

```shell
stash@{0}: On feature: My changes
```
