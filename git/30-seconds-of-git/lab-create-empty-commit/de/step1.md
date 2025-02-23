# Einen leeren Commit erstellen

Sie müssen in Ihrem Git-Repository einen leeren Commit erstellen. Dies kann in mehreren Szenarien nützlich sein, wie z. B.:

- Auslösen eines Build-Prozesses
- Erstellen eines Platzhalter-Commits
- Markieren eines bestimmten Punktes in der Repository-Geschichte

Für dieses Lab verwenden wir das Repository von `https://github.com/labex-labs/git-playground`:

1. Klonen Sie das Repository auf Ihren lokalen Computer, indem Sie den Befehl `git clone https://github.com/labex-labs/git-playground` verwenden.
2. Navigieren Sie zum Verzeichnis des Repositorys, indem Sie den Befehl `cd git-playground` verwenden, und konfigurieren Sie Ihr GitHub-Konto in der Umgebung, indem Sie die Befehle `git config --global user.name "your-uername"` und `git config --global user.email "your-email"` verwenden.
3. Verwenden Sie den Befehl `git commit --allow-empty -m "Empty commit"`, um einen leeren Commit mit der Nachricht "Empty commit" zu erstellen.
4. Vergewissern Sie sich, dass der leere Commit erstellt wurde, indem Sie den Befehl `git log --name-status HEAD^..HEAD` verwenden.

Hier führen Sie `git log --name-status HEAD^..HEAD` aus und das Ergebnis:

![git log empty commit result](../assets/challenge-create-empty-commit-step1-1.png)
