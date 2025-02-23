# Git Cherry-Pick

Вашей работе в качестве разработчика посвящена проект с несколькими ветками. Вы обнаружили определенное изменение, которое было внесено в предыдущем коммите, и хотите применить его к своей текущей ветке. Однако вы не хотите объединять целую ветку, так как она содержит другие изменения, которые вам не нужны.

## Задачи

Для этого испытания давайте используем репозиторий из `https://github.com/labex-labs/git-playground`.

1. Перейдите в директорию и настройте личность.
2. Создайте и переключитесь на ветку под названием `one-branch`, создайте файл под названием `hello.txt`, запишите в него "hello,world", добавьте его в зону подготовки и зафиксируйте с комментарием "add hello.txt".
3. Определите хэш коммита, созданного на предыдущем шаге, чтобы применить его к ветке `master`.
4. Переключитесь на ветку `master` и примените изменения к ветке `master`.
5. Проверьте, что изменения были применены к ветке `master`.

Вот результат выполнения команды `git log` для ветки `master`:

```shell
commit e2f3c6af9570f4eac2580dea93ca8133f1547d53 (HEAD -> master)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Sat Jul 15 14:30:31 2023 +0800

    add hello.txt

commit d22f46ba8c2d4e07d773c5126e9c803933eb5898 (origin/master, origin/HEAD)
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
