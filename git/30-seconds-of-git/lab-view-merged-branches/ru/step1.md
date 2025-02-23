# Просмотр объединенных ветвей

Ваша задача — вывести список всех объединенных локальных ветвей в репозитории Git по адресу `https://github.com/labex-labs/git-playground`. Вам понадобится использовать команду `git branch -a --merged`, чтобы отобразить список объединенных ветвей. Когда у вас появится список, вы должны быть в состоянии перемещаться по нему с помощью клавиш-стрелок и выйти, нажав <kbd>Q</kbd>.

1. Перейдите в каталог репозитория:

```shell
cd git-playground
```

2. Просмотрите список объединенных ветвей:

```shell
git branch -a --merged
```

Вот окончательный результат:

```
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/feature-branch
  remotes/origin/master
```
