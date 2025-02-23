# Alle Submodule von Remote herunterladen

Sie haben ein Git-Repository mit Submodulen, die von ihren jeweiligen Remotes aktualisiert werden müssen. Das manuelle Herunterladen jeder Submodul kann zeitaufwendig und fehleranfällig sein. Sie brauchen eine Möglichkeit, alle Submodule auf einmal herunterzuladen.

Angenommen, Sie haben ein Git-Repository namens `git`, das Submodule enthält. Sie können alle Submodule von ihren jeweiligen Remotes herunterladen, indem Sie den folgenden Befehl verwenden:

```shell
cd git
git submodule update --recursive --remote
```

Dieser Befehl aktualisiert alle Submodule im Repository auf die neueste Version, die in ihren jeweiligen Remotes verfügbar ist.
