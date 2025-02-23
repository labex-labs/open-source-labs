# Удаление файлов из staging-области

Вы работаете над проектом в репозитории `git-playground`. Вы внесли некоторые изменения в файлы и добавили их в staging-область с помощью команды `git add`. Однако, вы понимаете, что случайно добавили файл, который вы не хотите коммитить. Вам нужно удалить этот файл из staging-области.

1. Просмотреть текущее состояние рабочей директории:

```shell
git status
```

2. Удалить файл `newfile.txt` из staging-области с помощью команды `git restore --staged`:

```shell
git restore --staged newfile.txt
```

3. Проверить, что файл был удален из staging-области с помощью команды `git status`:

```shell
git status
```

Это конечный результат:

```shell
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
(use "git push" to publish your local commits)

Changes to be committed:
(use "git restore --staged <file>..." to unstage)
modified: README.md

Untracked files:
(use "git add <file>..." to include in what will be committed)
newfile.txt
```
