# Скопировать файл из другой ветви

Вы работаете над проектом в репозитории Git по адресу `https://github.com/labex-labs/git-playground.git`. У вас есть две ветви с именами `feature-1` и `feature-2`. Вам нужно скопировать файл `hello.txt` из ветви `feature-1` в ветвь `feature-2`.

1. Клонировать репозиторий:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Перейти в директорию и настроить личность:

```shell
cd git-playground
git config --global user.name "ваше-имя-пользователя"
git config --global user.email "ваша-эл.почта"
```

3. Создать и переключиться на ветвь `feature-1` и создать текстовый файл с именем `hello.txt` и записать в него строку "hello,world" и закоммитить файл с сообщением "добавить hello.txt":

```shell
git checkout -b feature-1
echo "hello,world" > hello.txt
git add.
git commit -m "добавить hello.txt"
```

4. Создать и переключиться на ветвь `feature-2` после переключения на ветвь `master`:

```shell
git checkout master
git checkout -b feature-2
```

5. Скопировать файл `hello.txt` из ветви `feature-1` в ветвь `feature-2` и закоммитить его с сообщением коммита "скопировать hello.txt":

```shell
git checkout feature-1 hello.txt
git commit -am "скопировать hello.txt"
```

6. Проверить, что файл `hello.txt` был скопирован в ветвь `feature-2`:

```shell
ll
```

В списке файлов в ветви `feature-2` вы должны увидеть файл `hello.txt`:

```
-rw-r--r-- 1 labex labex 15 Jul 12 22:43 file1.txt
-rw-r--r-- 1 labex labex 15 Jul 12 22:43 file2.txt
-rw-r--r-- 1 labex labex 12 Jul 12 22:50 hello.txt
-rw-r--r-- 1 labex labex 32 Jul 12 22:43 README.md
```
