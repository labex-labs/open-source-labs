# Automatisieren der Erstellung von Upstream-Branches

Als Entwickler möchten Sie den Prozess der Erstellung von Upstream-Branches beim Push automatisieren, um das Ärger zu vermeiden, die Branch manuell auf dem Remote-Repository zu erstellen.

## Aufgaben

Um die Herausforderung zu bewältigen, verwenden Sie das Git-Repository `git-playground` in Ihrem GitHub-Konto, um bei jedem Push automatisch einen Upstream-Branch aus einem Fork von `https://github.com/labex-labs/git-playground.git` zu erstellen.

1. Klonen Sie das Repository, navigieren Sie zum Verzeichnis und konfigurieren Sie die Identität.
2. Aktivieren Sie die automatische Erstellung von Upstream-Branches beim Push.
3. Erstellen Sie und wechseln Sie zu einer Branch namens `new-feature`, fügen Sie die Datei `hello.txt` hinzu und schreiben Sie darin "hello,world", fügen Sie sie zum Staging-Bereich hinzu und bestätigen Sie sie mit der Nachricht "Added hello.txt".
4. Stellen Sie Ihre Änderungen auf eine neue Branch namens `new-feature` bereit, die auf dem Remote-Repository nicht existiert.

Dies ist das Ergebnis nach Abschluss der Herausforderung:

![automatic upstream branch result](../assets/challenge-automatic-push-upstream-step1-1.png)
