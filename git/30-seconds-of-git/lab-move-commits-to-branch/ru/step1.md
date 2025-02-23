# Перемещение коммитов в новую ветку

Для этого лабы давайте используем репозиторий из `https://github.com/labex-labs/git-playground`. Вы работали над проектом в ветке `master`. Вы понимаете, что некоторые из внесенных вами изменений должны были быть сделаны на отдельной ветке. Вы хотите перенести эти изменения в новую ветку под названием `feature`.

1. Клонируйте репозиторий, перейдите в директорию и настройте идентификацию:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Переключитесь на ветку `master`:

```shell
git checkout master
```

3. Создайте файл под названием `hello.txt`, добавьте в него "hello, world", добавьте его в staging-область и отправьте с сообщением "Added hello.txt":

```shell
echo "hello,world" >> hello.txt
git add.
git commit -m "Added hello.txt"
```

4. Создайте новую ветку под названием `feature`, не переключаясь на нее. Когда вы создаете новую ветку на основе ветки `master`, состояние новой ветки такое же, как и у ветки `master`, то есть файлы в новой ветке такие же, как и файлы в ветке `master`, с тем же содержанием и историей версий:

```shell
git branch feature
```

5. Отмените последний коммит на `master`:

```shell
git reset HEAD~1 --hard
```

6. Проверьте историю коммитов на ветке `master` и историю коммитов на ветке `feature`, чтобы проверить результаты:

```shell
git log
git checkout feature
git log
```

Вот результат выполнения `git log`:

```shell
commit 7969ab5d6606e2a40c9fd826c732206b835976e9 (HEAD -> feature)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 20:19:22 2023 +0800

    Added hello.txt
```
