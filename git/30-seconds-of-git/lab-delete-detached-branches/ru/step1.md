# Удаление отсоединённых ветвей

У вас есть репозиторий Git с несколькими отсоединёнными ветвями, которые вы больше не нуждаетесь. Эти ветви засоряют ваш репозиторий и затрудняют его управление. Вы хотите удалить все отсоединённые ветви, чтобы очистить репозиторий.

Для завершения этого лабы вы будете использовать репозиторий Git `git-playground` из вашего аккаунта на GitHub, который является форком от `https://github.com/labex-labs/git-playground.git`. Не проверяйте пункт "Копировать только ветку master".

1. Клонируйте репозиторий, перейдите в директорию и настройте идентификацию:

```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Поскольку в удаленном репозитории есть ветка `feature-branch`, переключитесь на `feature-branch`, что приведет к тому, что локальная ветка `feature-branch` будет отслеживать ветку `feature-branch` удаленного репозитория, и удалите ветку `feature-branch` в удаленном репозитории:

```shell
git checkout feature-branch
git push origin --delete feature-branch
```

3. Просмотрите связь между локальными ветвями и ветвями удаленного репозитория, которые они отслеживают:

```shell
git branch -vv
```

4. Переключитесь обратно на ветку `master`:

```shell
git checkout master
```

5. Удалите все отсоединённые ветви из локального репозитория:

```shell
git branch -vv | grep ': gone]' | awk '{print $1}' | xargs git branch -D
```

6. Проверьте, были ли удалены отсоединённые ветви:

```shell
git branch
```

Вывод должен показывать только те ветви, которые связаны с какой-либо конкретной ветвью:

```shell
* master d22f46b [origin/master] Added file2.txt
```
