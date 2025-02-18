# Anzeigen von Commits in einem bestimmten Datumsbereich

Ihre Aufgabe besteht darin, alle Commits in einem bestimmten Datumsbereich mit Git anzuzeigen. Sie müssen den Befehl `git log` mit den Optionen `--since` und `--until` verwenden, um den Datumsbereich anzugeben. Sie können entweder ein bestimmtes Datum oder ein relatives Datum verwenden (z.B. "vor 12 Wochen").

Um diese Herausforderung zu bewältigen, müssen Sie das Repository `https://github.com/labex-labs/git-playground` verwenden. Befolgen Sie diese Schritte:

1. Klonen Sie das Repository auf Ihren lokalen Rechner mit dem Befehl `git clone https://github.com/labex-labs/git-playground`.
2. Navigieren Sie in das Verzeichnis des Repositorys mit dem Befehl `cd git-playground`.
3. Verwenden Sie den Befehl `git log --since='Apr 25 2023' --until='Apr 27 2023'`, um alle Commits zwischen dem 25. April 2023 und dem 27. April 2023 anzuzeigen.
4. Verwenden Sie den Befehl `git log --since='12 weeks ago'`, um alle Commits anzuzeigen, die in den letzten zwölf Wochen vorgenommen wurden.

Dies ist das endgültige Ergebnis:

```
commit d22f46ba8c2d4e07d773c5126e9c803933eb5898 (HEAD -> master, origin/master, origin/feature-branch, origin/HEAD)
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt

commit cf80005e40a3c661eb212fcea5fad06f8283f08f
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file1.txt

commit b00b9374a7c549d1af111aa777fdcc868d8a2a01
Author: Hang <huhuhang@gmail.com>
Date:   Wed Apr 26 14:16:00 2023 +0800

    Initial commit
```
