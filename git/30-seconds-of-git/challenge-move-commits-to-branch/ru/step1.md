# Перемещение коммитов в новую ветку

Для этого испытания давайте используем репозиторий из `https://github.com/labex-labs/git-playground`. Вы работали над проектом в ветке `master`. Вы понимаете, что некоторые изменения, которые вы внесли, должны были быть сделаны на отдельной ветке. Вы хотите перенести эти изменения в новую ветку под названием `feature`.

## Задачи

1. Перейдите в директорию репозитория и настройте свою GitHub-identyfikатор.
2. Переключитесь на ветку `master`.
3. Создайте файл под названием `hello.txt`, добавьте в него "hello, world", добавьте его в staging-область и отправьте с сообщением "Added hello.txt".
4. Создайте новую ветку под названием `feature` без переключения на нее.
5. Отмените последний коммит на `master`.
6. Проверьте историю коммитов на ветке `master` и историю коммитов на ветке `feature`, чтобы проверить результаты.

Это результат выполнения `git log`:

```shell
commit 7969ab5d6606e2a40c9fd826c732206b835976e9 (HEAD -> feature)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 20:19:22 2023 +0800

    Added hello.txt
```
