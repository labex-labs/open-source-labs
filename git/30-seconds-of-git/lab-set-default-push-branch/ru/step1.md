# Установка имени ветки по умолчанию для отправки

При отправке изменений в удаленный репозиторий Git будет использовать имя текущей локальной ветки в качестве имени ветки по умолчанию для удаленной ветки. Однако иногда вы можете захотеть отправить изменения в другую ветку. В этом случае вам нужно будет явно указывать имя удаленной ветки каждый раз, когда отправляете изменения. Это может быть утомительно и подвержено ошибкам, особенно если вы работаете с несколькими ветками.

Для завершения этого практического занятия вы будете использовать репозиторий Git `git-playground` из вашего аккаунта на GitHub, который является форком репозитория `https://github.com/labex-labs/git-playground.git`. Следуйте шагам ниже, чтобы установить имя ветки по умолчанию для отправки:

1. Склоняйте репозиторий с помощью следующей команды:
   ```
   git clone https://github.com/your-username/git-playground.git
   ```
2. Перейдите в каталог репозитория:
   ```
   cd git-playground
   ```
3. Установите имя ветки по умолчанию для отправки в имя текущей локальной ветки:
   ```
   git config push.default current
   ```
4. Создайте новую ветку и переключитесь на нее:
   ```
   git checkout -b my-branch
   ```
5. внесите в репозиторий некоторые изменения и зафиксируйте их:
   ```
   echo "Hello, World" > hello.txt
   git add hello.txt
   git commit -m "Add hello.txt"
   ```
6. Отправьте свои изменения в удаленный репозиторий:
   ```
   git push -u
   ```
   Git отправит ваши изменения в ветку с именем `my-branch` в удаленном репозитории.

Вот результат выполнения команды `git log`:

```shell
ADD hello.txt
```
