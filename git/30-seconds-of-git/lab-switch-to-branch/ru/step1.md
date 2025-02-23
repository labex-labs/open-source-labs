# Переключение на ветку

Вы работали над проектом в репозитории Git по адресу `https://github.com/labex-labs/git-playground`. Вашей команде создана новая ветка под названием `feature-1` для работы над новой функцией. Вам нужно переключиться на ветку `feature-1`, чтобы продолжить работу над функцией.

1. Клонируйте репозиторий Git:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Перейдите в директорию репозитория:

```shell
cd git-playground
```

3. Список всех веток в репозитории:

```shell
git branch
```

Результат:

```shell
feature-1
* master
```

4. Переключитесь на ветку `feature-1`:

```shell
git checkout feature-1
```

Результат:

```shell
Switched to branch 'feature-1'
```

5. Убедитесь, что вы сейчас на ветке `feature-1`:

```shell
git branch
```

Результат:

```shell
* feature-1
master
```
