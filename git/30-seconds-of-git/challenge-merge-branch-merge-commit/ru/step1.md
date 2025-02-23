# Объединить ветвь и создать коммит слияния

В качестве разработчика вы, возможно, захотите объединить ветвь в текущую ветвь, создав коммит слияния. Это может быть немного сложно, если вы не знакомы с Git. Задача - объединить ветвь в текущую ветвь, создав коммит слияния, используя репозиторий Git по адресу `https://github.com/labex-labs/git-playground` в директории.

## Задачи

Для этого испытания давайте используем репозиторий из `https://github.com/labex-labs/git-playground`.

1. Склоняйте репозиторий, перейдите в директорию и настройте личность.
2. Создайте и переключитесь на ветвь с именем `feature-branch`.
3. Добавьте в файл `README.md` строку "This is a new line.", добавьте ее в область подготовки и закоммитьте, комментарий к коммиту - "Add new line to README.md".
4. Переключитесь на ветвь `master`.
5. Объедините ветвь `feature-branch` в ветвь `master`, что создаст коммит слияния с сообщением "Merge feature-branch".

Вот результат выполнения команды `git log`:

```shell
commit 45b7e0fa8656d0aa751c7ca3cee29422e3d6cf05 (HEAD -> master)
Merge: d22f46b 1f19499
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 19:26:57 2023 +0800

    Merge feature-branch

commit 1f1949955387a154ff1bb5286d3d0a2b993f87e0 (feature-branch)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 19:26:57 2023 +0800

    Add new line to README.md
```
