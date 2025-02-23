# Найти ветви, содержащие коммит

Вам предоставлен репозиторий Git по адресу `https://github.com/labex-labs/git-playground`. Ваша задача — найти все ветви, которые содержат хэш с комментарием к коммиту "Added file2.txt".

1. Перейдите в директорию репозитория:

```shell
cd git-playground
```

2. Используйте команду `git branch --contains`, чтобы найти все ветви, которые содержат хэш с комментарием к коммиту "Added file2.txt":

```shell
git branch --contains d22f46b
```

Результат должен быть таким:

```shell
* master
new-branch
new-branch-1
new-branch-2
```
