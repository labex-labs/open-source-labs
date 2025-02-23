# Entfernen einer Datei aus der Geschichte

Angenommen, Sie haben versehentlich eine Datei, die sensible Informationen wie API-Schlüssel oder Passwörter enthält, in Ihr Git-Repository committet. Sie stellen fest, dass diese Datei niemals committet werden sollte und möchten sie vollständig aus der Repository-Geschichte entfernen. Ein einfaches Löschen der Datei und Committen der Änderung entfernt sie jedoch nicht aus der Repository-Geschichte. Die Datei bleibt in früheren Commits noch zugänglich, was ein Sicherheitsrisiko darstellen kann.

## Aufgaben

Um diese Herausforderung zu bewältigen, verwenden Sie das Git-Repository `git-playground` aus Ihrem GitHub-Konto, das von einem Fork von `https://github.com/labex-labs/git-playground.git` stammt. Dieses Repository enthält eine Datei namens `file1.txt`, die niemals committet werden sollte. Entfernen Sie bitte `file1.txt` aus der Repository-Geschichte.

1. Klonen Sie das Repository auf Ihren lokalen Computer von `https://github.com/your-username/git-playground`.
2. Navigieren Sie zum Verzeichnis und konfigurieren Sie die Identität.
3. Löschen Sie die Datei aus dem Repository-Index.
4. Überschreiben Sie die Repository-Geschichte, indem Sie alle Vorkommen von `file1.txt` entfernen.
5. Drücken Sie die Änderungen mit `force` auf das Remoterepository.

Nach Abschluss dieser Schritte wird `file1.txt` vollständig aus der Repository-Geschichte entfernt und nachdem Sie `git log --remotes` ausgeführt haben, werden Sie den Commit zu `file1.txt` nicht mehr sehen.
