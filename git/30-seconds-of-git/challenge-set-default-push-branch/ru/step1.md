# Установка имени ветки по умолчанию для отправки

При отправке изменений в удаленный репозиторий Git использует имя текущей локальной ветки в качестве имени ветки по умолчанию для удаленной ветки. Однако иногда вы можете захотеть отправить изменения в другую ветку. В этом случае вам нужно будет явно указывать имя удаленной ветки каждый раз при отправке изменений. Это может быть утомительно и подвержено ошибкам, особенно если вы работаете с несколькими ветками.

## Задачи

Для завершения этого испытания вы будете использовать репозиторий Git `git-playground` из вашего аккаунта GitHub, который является форком `https://github.com/labex-labs/git-playground.git`. Следуйте шагам ниже, чтобы установить имя ветки по умолчанию для отправки:

1. Склонруйте репозиторий из `https://github.com/your-username/git-playground.git`.
2. Перейдите в каталог репозитория.
3. Установите имя ветки по умолчанию для отправки в имя текущей локальной ветки.
4. Создайте новую ветку с именем `my-branch` и переключитесь на нее.
5. Создайте новый файл с именем `hello.txt` и запишите в него строку "Hello, World". Добавьте новый файл `hello.txt` в область подготовки Git и зафиксируйте его, используя комментарий к коммиту "Add hello.txt" для описания внесенных изменений в этом коммите.
6. Отправьте свои изменения в удаленный репозиторий. Git отправит ваши изменения в ветку с именем `my-branch` на удаленном репозитории.

Вот результат выполнения `git log`:

```shell
ADD hello.txt
```
