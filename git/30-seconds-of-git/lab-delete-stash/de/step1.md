# Entfernen eines Git-Stashes

Sie haben ein Git-Repository namens `https://github.com/labex-labs/git-playground`. Sie haben einen Stash mit dem Befehl `git stash save "my stash"` erstellt. Jetzt möchten Sie diesen Stash löschen, da Sie ihn nicht mehr benötigen.

1. Wechseln Sie in das Repository-Verzeichnis mit dem Befehl `cd git-playground`.
2. Listen Sie alle Stashes mit dem Befehl `git stash list` auf. Sie sollten den gerade erstellten Stash sehen.
3. Löschen Sie den Stash mit dem Befehl `git stash drop stash@{0}`.
4. Listen Sie alle Stashes erneut mit dem Befehl `git stash list` auf.

Der Stash, den Sie gerade gelöscht haben, sollte nicht mehr vorhanden sein.
