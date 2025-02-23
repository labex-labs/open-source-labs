# Fügen Sie eine Submodule hinzu

Ihre Aufgabe besteht darin, einer Git-Repository eine neue Submodule hinzuzufügen. Sie müssen den Befehl `git submodule add` verwenden, um die Submodule aus einem Upstream-Repository in ein lokales Verzeichnis in Ihrem Repository hinzuzufügen. Die Syntax für den Befehl lautet wie folgt:

```shell
git submodule add <upstream-path> <local-path>
```

- `<upstream-path>` ist die URL oder der Pfad zum Upstream-Repository, das Sie als Submodule hinzufügen möchten.
- `<local-path>` ist der Pfad, an dem Sie die Submodule in Ihrem lokalen Repository speichern möchten.

Angenommen, Sie haben ein Git-Repository namens `my-project` und möchten eine Submodule aus dem Git-Repository `https://github.com/labex-labs/git-playground.git` in ein Verzeichnis namens `git-playground` in Ihrem lokalen Repository hinzufügen. So können Sie es tun:

```shell
git init my-project
cd my-project
git submodule add https://github.com/labex-labs/git-playground.git./git-playground
```

Dies ist das Ergebnis nach Abschluss des Labs:

![Git submodule add result](../assets/challenge-add-submodule-step1-1.png)
