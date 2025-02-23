# Erstellen eines Git-Commits

Sie haben einige Änderungen an Ihrem Code vorgenommen und möchten sie als Momentaufnahme in Ihrem Git-Repository speichern. Sie möchten jedoch nicht alle Änderungen speichern, sondern nur die, die für das aktuelle Feature oder die Fehlerbehebung relevant sind. Wie können Sie einen Commit erstellen, der nur die relevanten Änderungen enthält?

Für dieses Lab verwenden wir das Repository von `https://github.com/labex-labs/git-playground`. Folgen Sie diesen Schritten:

1. Klonen Sie das Repository und navigieren Sie zu ihm:

   ```
   git clone https://github.com/labex-labs/git-playground
   cd git-playground
   ```

2. Konfigurieren Sie Ihr GitHub-Konto in der Umgebung:

   ```
   git config --global user.name "your-name"
   git config --global user.email "your-email"
   ```

3. Fügen Sie "hello,labex" zur Datei `README.md` hinzu, fügen Sie es zum Staging-Bereich hinzu und committen Sie es mit der Nachricht "Update README.md":

   ```
   echo "hello,labex" >> README.md
   git add.
   git commit -m "Update README.md"
   ```

   Die Option `-m` ermöglicht es Ihnen, eine Commit-Nachricht anzugeben. Stellen Sie sicher, dass die Nachricht aussagekräftig ist und erklärt, welche Änderungen der Commit enthält.

Dies ist das Ergebnis der Ausführung des Befehls `git log`:

![git log command output](../assets/challenge-create-commit-step1-1.png)
