# Erstellen eines Git-Stashes

Als Entwickler können Sie sich in einer Situation befinden, in der Sie zu einer anderen Branch wechseln oder an einer anderen Funktion arbeiten müssen, aber Sie sind noch nicht bereit, Ihre Änderungen zu committen. Sie möchten Ihren Fortschritt nicht verlieren, aber Sie möchten auch keine unvollständigen oder fehlerhaften Code committen. Hier kommt ein Stash sehr praktisch.

Ein Stash ermöglicht es Ihnen, Ihre Änderungen zu speichern, ohne sie zu committen, sodass Sie zu einer anderen Branch wechseln oder an einer anderen Funktion arbeiten können. Sie können dann Ihren Stash später anwenden, wenn Sie bereit sind, fortzufahren, Ihre Änderungen zu bearbeiten.

## Aufgaben

Angenommen, Sie arbeiten an einer Branch namens `feature` im Repository `git-playground` und möchten Ihre Änderungen speichern, bevor Sie zu einer anderen Branch wechseln:

1. Navigieren Sie zunächst zum Verzeichnis `git-playground`.
2. Wechseln Sie zu einer Branch namens `feature`.
3. Fügen Sie die Zeile "Einige Änderungen" zur Datei `README.md` hinzu.
4. Speichern Sie Ihre Änderungen in einen Stash und fügen Sie eine beschreibende Nachricht "Meine Änderungen" zu diesem Stash hinzu.
5. Wechseln Sie zu einer anderen Branch.
6. Wenn Sie mit den Änderungen an der anderen Branch fertig sind, wechseln Sie zurück zur Branch `feature` und wenden Sie Ihren Stash an.

Dies ist das fertige Ergebnis:

```shell
stash@{0}: On feature: Meine Änderungen
```
