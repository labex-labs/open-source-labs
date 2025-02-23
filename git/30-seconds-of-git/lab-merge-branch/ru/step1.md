# Объединить ветвь

Ваша задача - объединить ветвь в текущую ветвь с использованием Git. Вам нужно переключиться на целевую ветвь и затем объединить исходную ветвь в нее. Это может быть полезно, когда вы хотите объединить изменения из ветви `feature-branch-A` в ветвь `master` вашего проекта.

Для этого лабораторной работы давайте используем репозиторий из `https://github.com/labex-labs/git-playground`. Следуйте шагам, чтобы объединить `feature-branch-A` в ветвь `master`:

1. Клонируйте репозиторий, перейдите в директорию и настройте идентификацию:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Создайте ветвь `feature-branch-A`. Переключитесь на нее:

```shell
git checkout -b feature-branch-A
```

3. Добавьте "hello,world" в файл `file2.txt`, добавьте его в staging-область и зафиксируйте с сообщением "fix file2.txt":

```shell
echo "hello,world" >> file2.txt
git add.
git commit -m "fix file2.txt"
```

4. Переключитесь на ветвь `master`:

```shell
git checkout master
```

5. Объедините ветвь `feature-branch-A` в ветвь `master`:

```shell
git merge feature-branch-A
```

6. Resolve any conflicts that may arise during the merge process.

Это результат выполнения `git log`:

```shell
commit e2b80358ae6e4c3b8439cf111a4672a188739290 (HEAD -> master, feature-branch-A)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 18:51:00 2023 +0800

    fix file2.txt
```
