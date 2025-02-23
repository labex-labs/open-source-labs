# Alle Git-Aliase auflisten

Als Entwickler möchtest du möglicherweise alle Git-Aliase auflisten, die auf deinem System eingerichtet wurden. Dies kann aus mehreren Gründen nützlich sein, wie z. B.:

- Überprüfen, welche Aliase verfügbar sind
- Ermitteln, welche Befehle einem Alias zugeordnet sind
- Entfernen oder Modifizieren von bestehenden Aliasen

Angenommen, du hast ein Git-Repository namens `git-playground` unter `https://github.com/labex-labs/git-playground`.

1. Navigiere auf deinem lokalen Computer zu diesem Repository:

```shell
cd git-playground
```

2. Setze die folgenden Aliase ein:

```shell
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.rb rebase
```

3. Verwende den Befehl `sed` beim Auflisten aller Git-Aliase:

```shell
git config -l | grep alias | sed 's/^alias\.//g'
```

Beim Ausführen des Befehls wird folgendes ausgegeben:

```shell
st=status
co=checkout
rb=rebase
```
