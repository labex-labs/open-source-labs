# Zurück zum vorherigen Branch

Als Entwickler arbeiten Sie an einem Projekt und haben sich zu einem anderen Branch gewechselt, um an einer neuen Funktion zu arbeiten. Nachdem Sie einige Änderungen vorgenommen haben, stellen Sie fest, dass Sie zurück zum vorherigen Branch wechseln müssen, um einen Bug zu beheben. Sie können Ihre Änderungen in einem neuen Branch committen und einen Befehl verwenden, um schnell zum vorherigen Branch zu wechseln.

Um zu demonstrieren, wie man zurück zum vorherigen Branch wechselt, verwenden wir das Git-Repository mit dem Namen `https://github.com/labex-labs/git-playground`. Folgen Sie den Schritten unten:

1. Klonen Sie das Repository mit dem folgenden Befehl:
   ```
   git clone https://github.com/labex-labs/git-playground.git
   ```
2. Wechseln Sie in das Repository-Verzeichnis:
   ```
   cd git-playground
   ```
3. Erstellen Sie einen neuen Branch mit dem Namen `feature-branch`:
   ```
   git checkout -b feature-branch
   ```
4. Überprüfen Sie den aktuellen Branch und wechseln Sie schnell zum vorherigen Branch. Der Name Ihres neuen Branches ist `feature-branch` und der Name des vorherigen Branches, zu dem Sie zurückwechseln möchten, ist `master`:
   ```
   git checkout -
   ```
   Dies wird Sie zurück zum `master`-Branch wechseln, und Ihre Änderungen werden weiterhin dort sein.
