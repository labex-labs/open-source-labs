# Создать пустой коммит

Вам необходимо создать пустой коммит в вашем репозитории Git. Это может быть полезно в нескольких сценариях, таких как:

- Запуск процесса сборки
- Создание коммита-заполнителя (placeholder commit)
- Отметка определенной точки в истории репозитория

Для этого лабы давайте используем репозиторий из `https://github.com/labex-labs/git-playground`:

1. Скопируйте репозиторий на свою локальную машину с помощью команды `git clone https://github.com/labex-labs/git-playground`.
2. Перейдите в директорию репозитория с помощью команды `cd git-playground` и настройте свою учетную запись GitHub в среде с помощью команд `git config --global user.name "ваше-имя"` и `git config --global user.email "ваш-email"`.
3. Используйте команду `git commit --allow-empty -m "Empty commit"` для создания пустого коммита с сообщением "Empty commit".
4. Проверьте, был ли создан пустой коммит, используя команду `git log --name-status HEAD^..HEAD`.

Вот где вы запускаете `git log --name-status HEAD^..HEAD` и результат:

![git log empty commit result](../assets/challenge-create-empty-commit-step1-1.png)
