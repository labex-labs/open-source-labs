# Удалить удаленную ветку

Иногда вам может потребоваться удалить удаленную ветку, которая больше не нужна. Например, если ветка с функцией была объединена в основную ветку, вы можете захотеть удалить удаленную ветку с функцией, чтобы оставить репозиторий в чистоте.

## Задачи

Предположим, что репозиторий GitHub с именем `git-playground` был склонирован из вашего аккаунта GitHub, который является форком репозитория `https://github.com/labex-labs/git-playground.git`. Вы хотите удалить удаленную ветку с именем `feature-branch`, которая больше не нужна.

1. Откройте терминал и перейдите в директорию локального репозитория.
2. Добавьте ветку `feature-branch` в удаленный репозиторий `origin`.
3. Список всех удаленных веток.
4. Удалите удаленную ветку `feature-branch` в удаленном репозитории `origin`.
5. Убедитесь, что удаленная ветка была удалена.

Вывод не должен содержать удаленную ветку `feature-branch`:

```
origin/HEAD -> origin/master
origin/master
```
