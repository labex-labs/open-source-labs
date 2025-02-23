# Lade die neuesten Änderungen aus Remote herunter

Sie arbeiten an einem Projekt mit einem Team von Entwicklern und müssen sicherstellen, dass Ihre lokale Kopie der Codebasis mit den neuesten Änderungen Ihrer Teammitglieder aktuell ist. Dazu müssen Sie die neuesten Änderungen aus dem Remote-Repository herunterladen.

Für dieses Lab verwenden wir das Git-Repository unter `https://github.com/labex-labs/git-playground`. Folgen Sie den Schritten unten, um das Lab abzuschließen:

1. Wechsel in das Verzeichnis des geklonten Repositories:

```shell
cd git-playground
```

2. Lade die neuesten Änderungen aus der `master`-Branche des Remote-Repositories herunter:

```shell
git pull origin master
```

Nach Ausführung des Befehls `git pull` sollten Sie eine Meldung sehen, die angibt, dass Ihre lokale Kopie des Repositories mit dem Remote-Repository aktuell ist.

Dies ist das Ergebnis nach dem Herunterladen:

![git pull command output](../assets/challenge-pull-changes-step1-1.png)
