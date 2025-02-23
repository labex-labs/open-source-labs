# Добавить подмодуль

Ваша задача - добавить новый подмодуль в репозиторий Git. Вам понадобится использовать команду `git submodule add`, чтобы добавить подмодуль из репозитория-исходника в локальную директорию в вашем репозитории. Синтаксис команды выглядит так:

```shell
git submodule add <upstream-path> <local-path>
```

- `<upstream-path>` - это URL или путь к репозиторию-исходнику, который вы хотите добавить в качестве подмодуля.
- `<local-path>` - это путь, где вы хотите хранить подмодуль в вашем локальном репозитории.

Предположим, у вас есть репозиторий Git под названием `my-project`, и вы хотите добавить подмодуль из репозитория Git `https://github.com/labex-labs/git-playground.git` в директорию с именем `git-playground` в вашем локальном репозитории. Вот, как вы можете это сделать:

```shell
git init my-project
cd my-project
git submodule add https://github.com/labex-labs/git-playground.git./git-playground
```

Вот результат после завершения лабы:

![Git submodule add result](../assets/challenge-add-submodule-step1-1.png)
