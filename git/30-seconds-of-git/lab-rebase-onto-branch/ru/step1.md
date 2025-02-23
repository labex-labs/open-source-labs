# Пересмотреть ветку на другую ветку

Вашей работе в качестве разработчика посвящена проект с несколькими ветками. Вы внесли изменения в свою ветку и хотите включить эти изменения в другую ветку. Однако вы не хотите объединять ветки, так как хотите сохранить чистую и линейную историю. В этом случае вы можете использовать команду `git rebase`, чтобы пересмотреть свою ветку на другую ветку.

Для этого лабораторной работы используйте репозиторий из `https://github.com/labex-labs/git-playground`. Следуйте шагам ниже, чтобы завершить лабораторную работу:

1. Склоняйте репозиторий, перейдите в каталог и настройте идентификацию:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Создайте и переключитесь на ветку с именем `one-branch`:

```shell
git checkout -b one-branch
```

3. Добавьте "hello,world" в файл `README.md`, добавьте его в область подготовки и зафиксируйте с сообщением "Added some changes to README.md":

```shell
echo "hello,world" >> README.md
git add.
git commit -am "Added some changes to README.md"
```

4. Переключитесь на ветку `master`:

```shell
git checkout master
```

5. Убедитесь, что ваша локальная ветка `master` соответствует удаленному репозиторию:

```shell
git pull
```

6. Пересмотрите ветку `one-branch` на ветку `master`:

```shell
git rebase one-branch
```

7. Resolve any conflicts that arise during the rebase process.

Это результат выполнения `git log`:

```shell
commit eccff423dd6bf5335f76f2f364fa3b95130ff805 (HEAD -> master, one-branch)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Sat Jul 22 23:10:04 2023 +0800

    Added some changes to README.md
```
