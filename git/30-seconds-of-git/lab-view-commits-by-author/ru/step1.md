# Просмотр коммитов по автору

Ваша задача - получить все коммиты, сделанные определенным автором в репозитории `git-playground`. В этом репозитории содержится коллекция примерных проектов, которые вы можете использовать для практики навыков Git.

Для завершения этой лабораторной работы вам понадобится использовать команду `git log` с параметром `--author`. Это позволит вам отфильтровать историю коммитов и показать только коммиты, сделанные указанным автором.

Для получения всех коммитов, сделанных автором "Hang" в репозитории `git-playground`, вы можете использовать следующую команду:

```shell
git log --author="Hang"
```

Это выведет список всех коммитов, сделанных "Hang" в репозитории, вместе с информацией о сообщении коммита, дате и других деталях:

```shell
commit d22f46ba8c2d4e07d773c5126e9c803933eb5898 (HEAD -> master, origin/
master, origin/feature-branch, origin/HEAD)
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
