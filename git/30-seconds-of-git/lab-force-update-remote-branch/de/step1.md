# Remote-Branch aktualisieren, nachdem die Historie geändert wurde

Wenn Sie die Historie lokal ändern, erstellen Sie einen neuen Commit mit einem anderen SHA-1-Hash. Dies bedeutet, dass die Commit-Historie auf Ihrem lokalen Branch von der Commit-Historie auf dem Remote-Branch unterschiedlich ist. Wenn Sie versuchen, Ihre Änderungen an den Remote-Branch zu pushen, wird Git den Push ablehnen, da es die Commit-Historie als divergiert ansieht. Um dieses Problem zu lösen, müssen Sie eine Aktualisierung des Remote-Branchs erzwingen.

Um dieses Lab zu absolvieren, verwenden Sie das Git-Repository `git-playground` aus Ihrem GitHub-Konto, das von einem Fork von `https://github.com/labex-labs/git-playground.git` stammt.

1. Klonen Sie das `git-playground`-Repository auf Ihren lokalen Computer:

```shell
git clone https://github.com/your-username/git-playground.git
```

2. Aktualisieren Sie einen Commit mit der Nachricht "Added file2.txt" zu einem Commit mit der Nachricht "Update file2.txt":

```shell
git commit --amend
```

3. Pushen Sie Änderungen von Ihrem lokalen Branch zum Remote-Repository:

```shell
git push
```

4. Wenn Sie es nicht erfolgreich pushen können, drücken Sie bitte mit Zwang:

```shell
git push -f origin master
```

Das `-f`-Flag zwingt Git, den Remote-Branch mit Ihren Änderungen zu aktualisieren, auch wenn die Commit-Historie divergiert ist.

Dies ist das Endresultat:

```shell

```
