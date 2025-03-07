# Пересмотреть ветку на другую ветку

Вашей работе, как разработчику, посвящена проект с несколькими ветками. Вы внесли изменения в свою ветку и хотите включить эти изменения в другую ветку. Однако вы не хотите объединять ветки, так как хотите сохранить чистую и линейную историю.

## Задачи

Для этого испытания давайте используем репозиторий из `https://github.com/labex-labs/git-playground`.

1. Перейдите в директорию и настройте личность.
2. Создайте и переключитесь на ветку с именем `one-branch`.
3. Добавьте "hello,world" в файл `README.md`, добавьте его в область подготовки и зафиксируйте с комментарием "Added some changes to README.md".
4. Переключитесь на ветку `master`.
5. Убедитесь, что ваша локальная ветка `master` соответствует удаленному репозиторию.
6. Пересмотрите ветку `one-branch` на ветку `master`.
7. Разрешите любые конфликты, возникающие в процессе пересмотра.

Вот результат выполнения `git log`:

```shell
commit eccff423dd6bf5335f76f2f364fa3b95130ff805 (HEAD -> master, one-branch)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Sat Jul 22 23:10:04 2023 +0800

    Added some changes to README.md
```
