# Обновление удаленной ветки после переписывания истории

Когда вы переписываете историю локально, вы создаете новый коммит с другим хешем SHA-1. Это означает, что история коммитов на вашей локальной ветке отличается от истории коммитов на удаленной ветке. Если вы попытаетесь отправить свои изменения в удаленную ветку, Git отклонит отправку, потому что увидит историю коммитов как расходящуюся. Чтобы решить эту проблему, вам нужно принудительно обновить удаленную ветку.

Для завершения этого лабара вы будете использовать репозиторий Git `git-playground` из вашего аккаунта GitHub, который является форком от `https://github.com/labex-labs/git-playground.git`.

1. Клонируйте репозиторий `git-playground` на свою локальную машину:

```shell
git clone https://github.com/your-username/git-playground.git
```

2. Обновите коммит с сообщением "Added file2.txt" до коммита с сообщением "Update file2.txt":

```shell
git commit --amend
```

3. Отправьте изменения из локальной ветки в удаленный репозиторий:

```shell
git push
```

4. Если вы не можете отправить его успешно, выполните принудительную отправку:

```shell
git push -f origin master
```

Флаг `-f` заставляет Git обновить удаленную ветку с вашими изменениями, даже если история коммитов расходится.

Это конечный результат:

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
