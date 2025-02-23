# Alle Git-Aliase auflisten

Als Entwickler möchtest du möglicherweise alle Git-Aliase auflisten, die auf deinem System eingerichtet wurden. Dies kann aus mehreren Gründen nützlich sein, wie z. B.:

- Überprüfen, welche Aliase verfügbar sind
- Ermitteln, welche Befehle einem Alias zugeordnet sind
- Entfernen oder Modifizieren von bestehenden Aliasen

## Aufgaben

Angenommen, du hast ein Git-Repository namens `git-playground` unter `https://github.com/labex-labs/git-playground`.

Du hast die folgenden Aliase eingerichtet:

```shell
alias.st=status
alias.co=checkout
alias.rb=rebase
```

1. Navigiere auf deinem lokalen Computer zu diesem Repository.
2. Verwende den Befehl `sed` beim Auflisten aller Git-Aliase.

Beim Ausführen des Befehls wird folgendes ausgegeben:

```shell
st=status
co=checkout
rb=rebase
```
