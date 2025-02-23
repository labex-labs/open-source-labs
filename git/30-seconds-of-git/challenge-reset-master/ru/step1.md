# Сброс локальной ветки master для совпадения с удаленной

Вы работали над проектом и внесли изменения в локальную ветку `master`. Однако, вы понимаете, что удаленная ветка `master` была обновлена новыми изменениями, которых нет в вашей локальной ветке. Вам необходимо сбросить локальную ветку `master`, чтобы она совпадала с веткой на удаленном репозитории.

## Задачи

1. Переключиться на ветку `master`.
2. Получить последние обновления с удаленного репозитория.
3. Просмотреть историю коммитов текущей ветки.
4. Сбросить локальную ветку `master`, чтобы она совпадала с веткой на удаленном репозитории.
5. Проверить, что локальная ветка `master` теперь актуальна и совпадает с удаленной веткой `master`.

Вот результат:

```shell
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
