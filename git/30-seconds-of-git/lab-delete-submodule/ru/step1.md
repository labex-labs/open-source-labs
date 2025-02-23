# Удалить подмодуль

У вас есть Git-репозиторий, который включает подмодуль с именем `sha1collisiondetection`. Вы хотите удалить этот подмодуль из своего репозитория.

Для этого лабы мы будем использовать Git-репозиторий по адресу `https://github.com/git/git`. Этот репозиторий включает подмодуль с именем `sha1collisiondetection`.

Чтобы удалить подмодуль `sha1collisiondetection` из репозитория, следуйте шагам:

1. Откройте терминал и перейдите в корневую директорию вашего Git-репозитория:
   ```
   cd git
   ```
2. Выполните следующую команду, чтобы отменить регистрацию подмодуля `sha1collisiondetection`:
   ```
   git submodule deinit -f -- sha1collisiondetection
   ```
3. Выполните следующую команду, чтобы удалить директорию подмодуля `sha1collisiondetection`:
   ```
   rm -rf.git/modules/sha1collisiondetection
   ```
4. Выполните следующую команду, чтобы удалить рабочую дерево подмодуля `sha1collisiondetection`:
   ```
   git rm -f sha1collisiondetection
   ```

После этих шагов подмодуль `sha1collisiondetection` будет удален из вашего Git-репозитория. Если вы выполните команду `git submodule status`, вы не получите никакой информации о подмодуле.
