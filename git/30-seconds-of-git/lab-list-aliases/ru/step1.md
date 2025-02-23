# Список всех алиасов Git

В качестве разработчика вы, возможно, захотите вывести список всех настроенных на вашей системе алиасов Git. Это может быть полезно по нескольким причинам, например:

- Проверка доступных алиасов
- Узнать, какие команды соответствуют определенному алиасу
- Удаление или изменение существующих алиасов

Предположим, у вас есть репозиторий Git с именем `git-playground`, расположенный по адресу `https://github.com/labex-labs/git-playground`.

1. Перейдите к этому репозиторию на локальной машине:

```shell
cd git-playground
```

2. Настройте следующие алиасы:

```shell
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.rb rebase
```

3. Используйте команду `sed` при выводе списка всех алиасов Git:

```shell
git config -l | grep alias | sed 's/^alias\.//g'
```

Запуск команды выведет:

```shell
st=status
co=checkout
rb=rebase
```
