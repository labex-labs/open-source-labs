# Отключить быструю смерж

По умолчанию Git использует быструю смерж для объединения веток, у которых нет расходящихся коммитов. Это означает, что если у вас есть ветка без новых коммитов, Git просто переместит указатель ветки, в которую вы объединяете, на последний коммит ветки, из которой вы объединяете. Хотя это может быть полезно в некоторых случаях, это также может вызывать проблемы, особенно при работе над большими проектами с множеством участников. Например, если два разработчика работают над одной веткой и оба вносят изменения, быстрая смерж может вызвать конфликты, которые трудно разрешить.

Для отключения быстрой смержи давайте используем репозиторий из `https://github.com/labex-labs/git-playground`.

1. Клонируйте репозиторий, перейдите в директорию и настройте идентификацию:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Создайте и переключитесь на ветку под названием `my-branch`, создайте файл `hello.txt` и добавьте в него "hello,world", добавьте его в staging-область и зафиксируйте с сообщением "Added hello.txt":

```shell
git checkout -b my-branch
echo "hello,world" > hello.txt
git add.
git commit -m "Added hello.txt"
```

3. Запустите следующую команду, чтобы отключить быструю смерж:

```shell
git config --add merge.ff false
```

Это отключит быструю смерж для всех веток, даже если это возможно. Вы можете использовать флаг `--global`, чтобы настроить эту опцию глобально:

```shell
git config --global --add merge.ff false
```

4. Переключитесь обратно на ветку `mater` и объедините ветку `my-branch`, сохраните и выйдите без изменения текста:

```shell
git checkout master
git merge my-branch
```

Теперь Git всегда будет создавать коммит слияния, даже если быстрая смерж возможна:

```shell
commit 6e17a776ab51a89ace069614b0caf1c07915a92c (HEAD -> master)
Merge: ec5ea6d 6d7de91
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Mon Jul 17 13:30:44 2023 +0800

    Merge branch 'my-branch'
```
