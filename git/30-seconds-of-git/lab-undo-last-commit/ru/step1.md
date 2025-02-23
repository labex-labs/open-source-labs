# Отмена последнего коммита

Вы только что зафиксировали изменения в своем репозитории Git, но понимаете, что допустили ошибку. Вы хотите отменить последний коммит, не потеряв при этом никаких внесенных вами изменений. Как это можно сделать?

Для этого лабы давайте используем репозиторий из `https://github.com/labex-labs/git-playground`. Следуйте шагам:

1. Клонируйте репозиторий, перейдите в директорию и настройте идентификацию:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Проверьте историю коммитов:

```shell
git log
```

3. Отмените последний коммит, создав новый коммит с обратными изменениями коммита:

```shell
git revert HEAD
```

4. Проверьте историю коммитов снова:

```shell
git log
```

Вот результат выполнения команды `git log --oneline`:

```shell
532b49b (HEAD -> master) Revert "Added file2.txt"
d22f46b (origin/master, origin/HEAD) Added file2.txt
cf80005 Added file1.txt
b00b937 Initial commit
```
