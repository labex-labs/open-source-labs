# Удаление объединенных веток

Ваша задача - удалить все локальные ветки, которые были объединены в ветку `master` репозитория `https://github.com/labex-labs/git-playground`.

1. Перейдите в директорию репозитория:

```shell
cd git-playground
```

2. Список всех локальных веток, которые были объединены в `master`:

```shell
git branch --merged
```

Результат:

```
* master
  new-branch
  new-branch-1
  new-branch-2
  new-branch-3
```

3. Удалите все объединенные ветки:

```shell
git branch --merged master | awk '!/^[ *]*$/ &&!/master/ {print $1}' | xargs git branch -d
```

4. Снова выведите список всех веток:

```shell
git branch
```

Это окончательный результат:

```
* master
```
