# Git Cherry-Pick

Как разработчик, вы работаете над проектом с несколькими ветками. Вы обнаружили конкретное изменение, которое было внесено в предыдущем коммите и которое вы хотите применить к текущей ветке. Однако вы не хотите объединять всю ветку, так как она содержит другие изменения, которые вам не нужны. В таком сценарии вы можете использовать команду `git cherry-pick`, чтобы применить конкретное изменение к текущей ветке.

Для этого практического занятия используем репозиторий из `https://github.com/labex-labs/git-playground`. Следуйте шагам ниже, чтобы выполнить задание:

1. Клонируйте репозиторий, перейдите в его директорию и настройте свои идентификационные данные:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Создайте и переключитесь на ветку с именем `one-branch`, создайте файл с именем `hello.txt`, запишите в него "hello,world", добавьте его в staging area и закоммитьте с сообщением "add hello.txt":

```shell
git checkout -b one-branch
echo "hello,world" > hello.txt
git add.
git commit -m "add hello.txt"
```

3. Определите хэш коммита, созданного на предыдущем шаге, чтобы применить его к ветке `master`:

```shell
git log
```

4. Переключитесь на ветку `master` и примените изменения к этой ветке:

```shell
git checkout master
git cherry-pick 1609c283ec86ee4
```

5. Проверьте, что изменения были применены к ветке `master`:

```shell
git log
```

Вот результат выполнения команды `git log` на ветке `master`:

```shell
commit e2f3c6af9570f4eac2580dea93ca8133f1547d53 (HEAD -> master)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Sat Jul 15 14:30:31 2023 +0800

    add hello.txt

commit d22f46ba8c2d4e07d773c5126e9c803933eb5898 (origin/master, origin/HEAD)
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt

commit cf80005e40a3c661eb212fcea5fad06f8283f08f
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file1.txt

commit b00b9374a7c549d1af111aa777fdcc868d8a2a01
Author: Hang <huhuhang@gmail.com>
Date:   Wed Apr 26 14:16:00 2023 +0800

    Initial commit
```
