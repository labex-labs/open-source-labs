# Einen Commit von einem anderen Autor erstellen

Angenommen, Sie arbeiten an einem Projekt mit einem Team von Entwicklern, und ein Teammitglied hat einige Änderungen am Code vorgenommen. Sie sind jedoch nicht verfügbar, um die Änderungen selbst zu committen, und Sie müssen einen Commit im Namen des anderen Teammitglieds erstellen. In diesem Szenario können Sie die Option `--author` verwenden, um den Namen und die E-Mail-Adresse des Autors des Commits zu ändern. Diese Option ist nützlich, wenn Sie einem Commit einen anderen Autor zuweisen müssen, z. B. wenn Sie im Namen eines Kollegen committen, der im Urlaub oder krank ist.

## Aufgaben

Angenommen, Sie arbeiten an einem Projekt, das auf dem Repository `https://github.com/labex-labs/git-playground` gehostet wird. Sie haben einige Änderungen am Code vorgenommen, z. B. "Fehler beheben" wurde zur Datei `README`.md in Ihrem GitHub-Account hinzugefügt, und Sie müssen einen Commit im Namen Ihres Kollegen John Doe erstellen, der diese Änderungen selbst nicht committen kann.

Dieser Befehl erstellt einen neuen Commit mit der Nachricht "Fehler beheben" und weist ihn John Doe zu:

![Git commit author command](../assets/challenge-commit-set-author-step1-1.png)
