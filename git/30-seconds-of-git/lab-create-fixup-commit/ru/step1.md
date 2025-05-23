# Создание фиксационного коммита

Предположим, вы работаете над проектом с несколькими другими разработчиками, и вы замечаете небольшую ошибку в коммите, сделанном несколько дней назад. Вы хотите исправить ошибку, но не хотите создавать новый коммит и нарушать работу других разработчиков. Именно в этом случае фиксационные коммиты приносят пользу. Создав фиксационный коммит, вы можете внести необходимые изменения без создания нового коммита, и фиксационный коммит будет автоматически объединен с исходным коммитом в ходе следующего ребейса.

Например, ваша задача - записать строку "hello,world" в файл `hello.txt` и добавить ее в виде "фиксационного" коммита к коммиту с сообщением "Added file1.txt", чтобы она могла быть автоматически объединена в последующей операции ребейса.

Для этого лабораторного занятия давайте используем репозиторий из `https://github.com/labex-labs/git-playground`.

1. Клонируйте репозиторий, перейдите в директорию и настройте личность:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Создайте файл `hello.txt`, запишите в него "hello,world" и добавьте его в область подготовки к коммиту:

```shell
echo "hello,world" > hello.txt
git add.
```

3. Чтобы создать фиксационный коммит, вы можете использовать команду `git commit --fixup <commit>`:

```shell
git commit --fixup cf80005
# Это хэш коммита с сообщением "Added file1.txt".
```

Это создаст фиксационный коммит для указанного коммита. Обратите внимание, что вы должны подготовить свои изменения перед созданием фиксационного коммита. 4. После создания фиксационного коммита вы можете использовать команду `git rebase --interactive --autosquash`, чтобы автоматически объединить фиксационный коммит с исходным коммитом в ходе следующего ребейса. Например:

```shell
git rebase --interactive --autosquash HEAD~3
```

При открытии интерактивного редактора не нужно изменять текст и сохранять для выхода. Это выполнит ребейс по последним 3 коммитам и автоматически объединит любые фиксационные коммиты с их соответствующими исходными коммитами.

Вот результат выполнения команды `git show HEAD~1`:

```shell
[object Object]
```
