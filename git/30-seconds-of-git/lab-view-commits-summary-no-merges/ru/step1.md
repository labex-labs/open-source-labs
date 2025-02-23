# Просмотр краткой сводки коммитов без коммитов слияния

Вы работаете над проектом с несколькими другими разработчиками, и вы хотите увидеть сводку всех коммитов, сделанных в репозитории. Однако вы не хотите видеть коммиты слияния, так как они не содержат никаких реальных изменений в коде. Как можно просмотреть сводку всех коммитов, исключая коммиты слияния?

Для этого лабы давайте используем репозиторий из `https://github.com/labex-labs/git-playground`.

1. Склоняйте репозиторий, перейдите в директорию и настройте идентификацию:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Создайте и переключитесь на ветку с именем `feature1`, создайте файл с именем `file.txt` и запишите в него `feature 1`, добавьте его в staging-область и зафиксируйте с сообщением "Add feature 1":

```shell
git checkout -b feature1
echo "Feature 1" >> file.txt
git add.
git commit -m "Add feature 1"
```

3. Переключитесь обратно на ветку `master`, объедините ветку `feature1`, отключите прямой merge, сохраните и выйдите без изменения текста:

```shell
git checkout master
git merge --no-ff feature1
```

4. Просмотрите краткую сводку всех коммитов, исключая коммиты слияния:

```shell
git log --oneline --no-merges
```

Это выведет список всех коммитов, сделанных в репозитории, исключая любые коммиты слияния. Вывод будет выглядеть примерно так:

```shell
430b986 (feature1) Add feature 1
d22f46b (origin/master, origin/HEAD) Added file2.txt
cf80005 Added file1.txt
b00b937 Initial commit
```
