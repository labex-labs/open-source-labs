# Найти потерянные файлы

Вы работали над проектом в репозитории `git-playground`. Однако вы заметили, что некоторые файлы отсутствуют, и вы не знаете, когда они были удалены и как восстановить их. Ваша задача - использовать Git для поиска потерянных файлов и коммитов в репозитории.

1. Клонировать репозиторий `git-playground`:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Перейти в директорию и настроить идентификацию:

```shell
cd git-playground
git config --global user.name "ваше-имя-пользователя"
git config --global user.email "ваша-email"
```

3. Создать и переключиться на ветку с именем `one-branch`, удалить `file2.txt` и зафиксировать изменения с сообщением "Remove file2":

```shell
git checkout -b one-branch
git rm file2.txt
git commit -m "Remove file2"
```

4. Вернуться на ветку `master` и удалить ветку `one-branch`:

```shell
git checkout master
git branch -D one-branch
```

5. Выполнить команду `git fsck --lost-found`, чтобы найти потерянные файлы и коммиты:

```shell
git fsck --lost-found
```

6. Проверить директорию `.git/lost-found`, чтобы увидеть, были ли восстановлены какие-либо потерянные файлы:

```shell
ls.git/lost-found
```

7. Если были найдены потерянные файлы, проверить их, чтобы определить, являются ли они отсутствующими файлами.

Это результат выполнения команды `ls.git/lost-found`:

```shell
commit
```
