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
commit b8c530558ecd004156dd05ac7d22d8cf07b2c28e (HEAD -> master, origin/master, origin/HEAD)
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Update file2.txt

commit cf80005e40a3c661eb212fcea5fad06f8283f08f
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file1.txt

commit b00b9374a7c549d1af111aa777fdcc868d8a2a01
Author: Hang <huhuhang@gmail.com>
Date:   Wed Apr 26 14:16:00 2023 +0800

    Initial commit
```
