# Zeigen Sie einen kurzen Commit-Zusammenfassung an

Als Entwickler arbeiten Sie an einem Projekt mit mehreren Mitwirkenden. Sie müssen eine Zusammenfassung aller Commits für das Projekt anzeigen, um die vorgenommenen Änderungen zu verstehen und potenzielle Probleme zu identifizieren. Sie möchten jedoch nicht viel Zeit verbringen, um durch alle Commit-Nachrichten zu durchsuchen, um die Informationen zu finden, die Sie benötigen.

Um eine kurze Zusammenfassung aller Commits in einem Git-Repository anzuzeigen, können Sie den Befehl `git log --oneline` verwenden. Nehmen wir an, Sie arbeiten an einem Projekt auf GitHub namens `git-playground`.

1. Sie können das Repository auf Ihren lokalen Computer klonen, indem Sie folgenden Befehl verwenden:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Nachdem Sie das Repository geklont haben, navigieren Sie zum Projektverzeichnis und führen Sie folgenden Befehl aus, um eine kurze Zusammenfassung aller Commits anzuzeigen:

```shell
cd git-playground
git log --oneline
```

Dies wird eine Liste aller Commits für das Repository ausgeben, zusammen mit einer kurzen Zusammenfassung jeder Commit-Nachricht. Beispielsweise:

```shell
d22f46b (HEAD -> master, origin/master, origin/feature-branch, origin/HEAD) Added file2.txt
cf80005 Added file1.txt
b00b937 Initial commit
```
