# Удалить файл из истории

Предположим, вы случайно зафиксировали в своем репозитории Git файл, содержащий конфиденциальную информацию, такую как API-ключи или пароли. Вы понимаете, что этот файл никогда не должен был быть зафиксирован, и хотите полностью удалить его из истории репозитория. Однако просто удалить файл и зафиксировать изменения не удалит его из истории репозитория. Файл по-прежнему будет доступен в предыдущих коммитах, что может представлять риск безопасности.

Для завершения этого лабара вы будете использовать репозиторий Git `git-playground` из вашего аккаунта на GitHub, который является форком репозитория `https://github.com/labex-labs/git-playground.git`. В этом репозитории есть файл с именем `file1.txt`, который никогда не должен был быть зафиксирован. Чтобы удалить `file1.txt` из истории репозитория, следуйте шагам:

1. Склонюйте репозиторий на свою локальную машину:

```shell
git clone https://github.com/your-username/git-playground
```

2. Используйте следующие команды, чтобы перейти в директорию и настроить идентификацию:

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

3. Удалите файл из индекса репозитория.

```shell
git rm --cached --ignore-unmatch file1.txt
```

4. Зафиксируйте это изменение с комментарием к коммиту "Удалить конфиденциальный файл file1.txt":

```shell
git commit -m "Remove sensitive file1.txt"
```

5. Перезапишите историю репозитория, удалив все вхождения `file1.txt`:

```shell
git filter-branch --force --index-filter "git rm --cached --ignore-unmatch file1.txt" --prune-empty --tag-name-filter cat -- --all
```

6. Принудительно отправьте изменения на удаленный репозиторий:

```shell
git push origin --force --all
```

После завершения этих шагов `file1.txt` будет полностью удален из истории репозитория, и после выполнения `git log --remotes` вы не увидите коммит по `file1.txt`.
