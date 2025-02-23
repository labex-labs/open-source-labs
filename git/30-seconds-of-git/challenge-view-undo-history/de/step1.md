# "Rückgängigmachen" - Historie anzeigen

Als Entwickler möchtest du möglicherweise Änderungen rückgängig machen, die du an deiner Codebasis vorgenommen hast. Git bietet mehrere Möglichkeiten, Änderungen rückgängig zu machen, wie z. B. mit den Befehlen `git reset` oder `git revert`. Es kann jedoch schwierig sein, alle von dir ausgeführten Aktionen zu verfolgen, insbesondere wenn du fortgeschrittene Befehle wie `git rebase` verwendet hast.

## Aufgaben

Angenommen, du hast einige Änderungen an einem Repository vorgenommen und möchtest sie rückgängig machen.

1. Navigiere zu dem Repository.
2. Jetzt stellst du fest, dass du einen Fehler gemacht hast und den letzten Commit rückgängig machen möchtest.
3. Du stellst möglicherweise fest, dass du einen weiteren Fehler gemacht hast und den Reset rückgängig machen möchtest. Zeige den Referenzprotokoll an und finde den Commit-Hash des vorherigen Commits.
4. Du siehst, dass der vorherige Commit-Hash `d22f46b` ist und verwendest diesen Hash, um das Repository zurück auf den vorherigen Commit zurückzusetzen.
5. Zeige die historischen Commit-Protokolle an, um die Ergebnisse zu verifizieren.

Hier ist das Ergebnis von Schritt 3. Dies wird eine Liste aller von dir in dem Repository ausgeführten Aktionen anzeigen, einschließlich des Resets:

```shell
cf80005 (HEAD -> master) HEAD@{0}: reset: moving to HEAD~1
d22f46b (origin/master, origin/feature-branch, origin/HEAD) HEAD@{1}: clone: from https://github.com/labex-labs/git-playground.git
```
