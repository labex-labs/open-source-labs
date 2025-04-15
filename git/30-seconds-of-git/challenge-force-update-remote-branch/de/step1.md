# Remote-Branch aktualisieren, nachdem die Geschichte geändert wurde

Wenn Sie die Geschichte lokal ändern, erstellen Sie einen neuen Commit mit einem anderen SHA-1-Hash. Dies bedeutet, dass der Commit-History auf Ihrer lokalen Branch von der Commit-History auf der Remote-Branch unterschiedlich ist. Wenn Sie versuchen, Ihre Änderungen an die Remote-Branch zu pushen, wird Git den Push ablehnen, da es die Commit-History als divergiert ansieht. Um dieses Problem zu lösen, müssen Sie eine Aktualisierung der Remote-Branch erzwingen.

## Aufgaben

Um diese Herausforderung zu absolvieren, verwenden Sie das Git-Repository `git-playground` aus Ihrem GitHub-Konto, das von einem Fork von `https://github.com/labex-labs/git-playground.git` stammt.

1. Klonen Sie das `git-playground`-Repository auf Ihren lokalen Computer.
2. Aktualisieren Sie einen Commit mit der Nachricht "Added file2.txt" zu einem Commit mit der Nachricht "Update file2.txt".
3. Pushen Sie Änderungen von der lokalen Branch zum Remote-Repository.
4. Wenn Sie es nicht erfolgreich pushen können, versuchen Sie es mit einem Zwangspush.

Dies ist das Endresultat:

```shell
[object Object]
```
