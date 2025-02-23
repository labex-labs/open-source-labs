# Отбросить изменения, которые не отслеживаются

Вы работаете над проектом с использованием Git и внесли некоторые изменения в свою рабочую директорию. Однако, вы понимаете, что эти изменения вам не нужны и хотите их отбросить. Вы хотите отбросить все изменения, которые не отслеживаются, в текущей ветке.

Для завершения этого лабы вы будете использовать репозиторий Git по адресу `https://github.com/labex-labs/git-playground`. Следуйте шагам:

1. Перейдите в директорию репозитория:

```shell
cd git-playground
```

2. Проверьте статус своей рабочей директории:

```shell
git status
```

Вы должны увидеть следующий вывод:

```shell
On branch master
Your branch is up to date with 'origin/master'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        new-file.txt

nothing added to commit but untracked files present (use "git add" to track)
```

3. Отбросьте все изменения, которые не отслеживаются, в текущей ветке:

```shell
git clean -f -d
```

4. Проверьте статус своей рабочей директории снова:

```shell
git status
```

Вы должны увидеть следующий вывод:

```shell
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```

Команда `git clean -f -d` отбросила все изменения, которые не отслеживаются, в текущей ветке.
