# Entfernen einer Datei aus der Historie

Angenommen, Sie haben versehentlich eine Datei, die sensible Informationen wie API-Schlüssel oder Passwörter enthält, in Ihr Git-Repository committet. Sie stellen fest, dass diese Datei niemals committet werden sollte und möchten sie vollständig aus der Repository-Historie entfernen. Ein einfaches Löschen der Datei und Committen der Änderung entfernt sie jedoch nicht aus der Repository-Historie. Die Datei bleibt in früheren Commits noch zugänglich, was ein Sicherheitsrisiko darstellen kann.

Um dieses Lab zu absolvieren, verwenden Sie das Git-Repository `git-playground` aus Ihrem GitHub-Konto, das von einem Fork von `https://github.com/labex-labs/git-playground.git` stammt. Dieses Repository enthält eine Datei namens `file1.txt`, die niemals committet werden sollte. Entfernen Sie `file1.txt` aus der Repository-Historie, befolgen Sie diese Schritte:

1. Klonen Sie das Repository auf Ihren lokalen Computer:

```shell
git clone https://github.com/your-username/git-playground
```

2. Verwenden Sie die folgenden Befehle, um in das Verzeichnis zu navigieren und die Identität zu konfigurieren:

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

3. Löschen Sie die Datei aus dem Repository-Index.

```shell
git rm --cached --ignore-unmatch file1.txt
```

4. Committen Sie diese Änderung mit der Commit-Nachricht "Remove sensitive file1.txt":

```shell
git commit -m "Remove sensitive file1.txt"
```

5. Überschreiben Sie die Repository-Historie, indem Sie alle Vorkommen von `file1.txt` entfernen:

```shell
git filter-branch --force --index-filter "git rm --cached --ignore-unmatch file1.txt" --prune-empty --tag-name-filter cat -- --all
```

6. Drücken Sie die Änderungen mit Gewalt auf das Remoterepository:

```shell
git push origin --force --all
```

Nach Abschluss dieser Schritte wird `file1.txt` vollständig aus der Repository-Historie entfernt und nachdem Sie `git log --remotes` ausgeführt haben, werden Sie den Commit zu `file1.txt` nicht mehr sehen.
