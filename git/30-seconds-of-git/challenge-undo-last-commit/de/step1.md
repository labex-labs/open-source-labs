# Den letzten Commit rückgängig machen

Du hast gerade Änderungen an deinem Git-Repository commited, stellst aber fest, dass du einen Fehler begangen hast. Du möchtest den letzten Commit rückgängig machen, ohne irgendwelche der von dir vorgenommenen Änderungen zu verlieren. Wie kannst du das tun?

## Aufgaben

Für diese Herausforderung verwenden wir das Repository von `https://github.com/labex-labs/git-playground`.

1. Überprüfe den Commithistory.
2. Mache den letzten Commit rückgängig, indem du einen neuen Commit mit der Umkehrung der Änderungen des Commits erstellst.

Dies ist das Ergebnis des Ausführens des Befehls `git log --oneline`:

```shell
532b49b (HEAD -> master) Revert "Added file2.txt"
d22f46b (origin/master, origin/HEAD) Added file2.txt
cf80005 Added file1.txt
b00b937 Initial commit
```
