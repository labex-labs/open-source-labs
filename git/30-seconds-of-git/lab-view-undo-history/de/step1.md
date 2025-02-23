# "Rückgängigmachungs"-Geschichte anzeigen

Als Entwickler möchtest du möglicherweise Änderungen rückgängig machen, die du an deiner Codebasis vorgenommen hast. Git bietet mehrere Möglichkeiten, Änderungen rückgängig zu machen, wie zum Beispiel die Verwendung der Befehle `git reset` oder `git revert`. Es kann jedoch schwierig sein, alle von dir ausgeführten Aktionen zu verfolgen, insbesondere wenn du fortgeschrittene Befehle wie `git rebase` verwendet hast. Hier kommt der Befehl `git reflog` zum Einsatz.

Der Befehl `git reflog` zeigt das Git-Referenzprotokoll an, das eine Aufzeichnung aller von dir in deinem Repository ausgeführten Aktionen ist. Dies umfasst nicht nur Commits, sondern auch andere Aktionen wie Branch-Merges, Rebases und Resets. Indem du das Referenzprotokoll anzeigst, kannst du eine vollständige Geschichte aller Änderungen sehen, die du an deinem Repository vorgenommen hast, auch wenn sie nicht im Commit-Verlauf erscheinen.

Um die "Rückgängigmachungs"-Geschichte in Git anzuzeigen, kannst du den Befehl `git reflog` verwenden. Angenommen, du hast einige Änderungen an einem Repository vorgenommen und möchtest sie rückgängig machen.

1. Navigiere zu dem Repository über die Befehlszeile:

```shell
cd git-playground
```

2. Nehmen wir an, du stellst fest, dass du einen Fehler gemacht hast und den letzten Commit rückgängig machen möchtest. Du kannst dazu den Befehl `git reset` verwenden:

```shell
git reset HEAD~1
```

3. Nachdem du diesen Befehl ausgeführt hast, stellst du möglicherweise fest, dass du einen weiteren Fehler gemacht hast und den Reset rückgängig machen möchtest. Hier kommt der Befehl `git reflog` zum Einsatz. Du kannst ihn verwenden, um das Referenzprotokoll anzuzeigen und den Commit-Hash des vorherigen Commits zu finden:

```shell
git reflog
```

Dies wird eine Liste aller von dir in dem Repository ausgeführten Aktionen anzeigen, einschließlich des Resets:

```shell
cf80005 (HEAD -> master) HEAD@{0}: reset: moving to HEAD~1
d22f46b (origin/master, origin/feature-branch, origin/HEAD) HEAD@{1}: clone: from https://github.com/labex-labs/git-playground.git
```

4. Aus dieser Ausgabe kannst du sehen, dass der vorherige Commit-Hash `d22f46b` ist. Du kannst diesen Hash verwenden, um das Repository zurück auf den vorherigen Commit zurückzusetzen:

```shell
git reset d22f46b
```

5. Zeige historische Commit-Protokolle an, um die Ergebnisse zu verifizieren:

```shell
git log
```
