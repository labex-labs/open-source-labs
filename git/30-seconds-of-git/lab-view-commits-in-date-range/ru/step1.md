# Просмотр коммитов (коммитов) в определенном диапазоне дат

Ваша задача - просмотреть все коммиты (коммиты) в определенном диапазоне дат с использованием Git. Вам нужно будет использовать команду `git log` с параметрами `--since` и `--until`, чтобы указать диапазон дат. Вы можете использовать как конкретную дату, так и относительную дату (например, "12 недель назад").

Для выполнения этого задания вам нужно будет использовать репозиторий `https://github.com/labex-labs/git-playground`. Следуйте этим шагам:

1. Клонируйте репозиторий на свою локальную машину с помощью команды `git clone https://github.com/labex-labs/git-playground`.
2. Перейдите в директорию репозитория с помощью команды `cd git-playground`.
3. Используйте команду `git log --since='Apr 25 2023' --until='Apr 27 2023'`, чтобы просмотреть все коммиты (коммиты) между 25 апреля 2023 года и 27 апреля 2023 года.
4. Используйте команду `git log --since='12 weeks ago'`, чтобы просмотреть все коммиты (коммиты), сделанные за последние двенадцать недель.

Вот конечный результат:

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
