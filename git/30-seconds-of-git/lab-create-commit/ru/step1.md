# Создать Git-коммит

Вы внесли некоторые изменения в свой код и хотите сохранить их как снимок в своем репозитории Git. Однако, вы не хотите сохранять все внесенные изменения, только те, которые связаны с текущей функцией или исправлением ошибки. Как можно создать коммит, содержащий только соответствующие изменения?

Для этого лабы давайте используем репозиторий из `https://github.com/labex-labs/git-playground`, следуя шагам:

1. Клонируйте репозиторий и перейдите в него:

   ```
   git clone https://github.com/labex-labs/git-playground
   cd git-playground
   ```

2. Configure your github account in the environment:

   ```
   git config --global user.name "your-name"
   git config --global user.email "your-email"
   ```

3. Добавьте "hello,labex" в файл `README.md`, добавьте его в staging-область и зафиксируйте с сообщением "Update README.md":

   ```
   echo "hello,labex" >> README.md
   git add.
   git commit -m "Update README.md"
   ```

   Параметр `-m` позволяет вам указать сообщение коммита. Убедитесь, что сообщение информативно и объясняет, какие изменения содержит коммит.

Вот результат выполнения команды `git log`:

![git log command output](../assets/challenge-create-commit-step1-1.png)
