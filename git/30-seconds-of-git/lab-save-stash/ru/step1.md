# Создание Git Stash

В качестве разработчика вы можете оказаться в ситуации, когда вам нужно переключиться на другую ветку или работать над другой функцией, но вы еще не готовы коммитить свои изменения. Вы не хотите потерять свой прогресс, но также не хотите коммитить неполный или ошибочный код. Именно здесь stash пригодится.

Stash позволяет сохранять ваши изменения без коммитов, чтобы вы могли переключиться на другую ветку или работать над другой функцией. Затем вы можете применить свой stash позже, когда будете готовы продолжить работу над своими изменениями.

Для создания stash вы можете использовать команду `git stash save`. Предположим, вы работаете в ветке `feature` в репозитории `git-playground` и хотите сохранить свои изменения, прежде чем переключиться на другую ветку:

1. Во - первых, перейдите в директорию `git-playground`:

```shell
cd git-playground
```

2. Переключитесь на ветку `feature`:

```shell
git checkout -b feature
```

3. Внесите некоторые изменения в файлы в директории:

```shell
echo "Some changes" >> README.md
```

4. Сохраните свои изменения в stash:

```shell
git stash save "My changes"
```

5. Переключитесь на другую ветку:

```shell
git checkout master
```

6. Когда закончите делать изменения на другой ветке, переключитесь обратно на ветку `feature` и примените свой stash:

```shell
git stash apply
```

Вот результат:

```shell
stash@{0}: On feature: My changes
```
