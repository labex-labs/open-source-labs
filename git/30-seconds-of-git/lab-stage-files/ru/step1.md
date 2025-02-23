# Добавление файлов в staging-область

Вы работали над проектом, хранящимся в репозитории Git по адресу `https://github.com/labex-labs/git-playground`. Вы внесли некоторые изменения в кодовую базу и хотите зафиксировать эти изменения в репозитории. Однако вы хотите зафиксировать только определенные изменения, а не все внесенные вами изменения. Для этого вам нужно добавить файлы в staging-область.

1. Вы внесете некоторые изменения в директорию `git-playground`:

```shell
echo "hello" > index.html
echo "world" > style.css
echo "git" > one.js
echo "labex" > two.js
echo "hello git" > 1.py
echo "hello labex" > 2.py
```

2. Добавьте эти файлы в staging-область:

```shell
git add index.html style.css
```

3. Просмотрите статус текущей рабочей директории и staging-области, включая информацию о том, какие файлы были изменены, какие файлы были добавлены в staging-область и т.д.:

```shell
git status
```

4. Альтернативно, добавьте все файлы с расширением `.js`:

```shell
git add *.js
```

5. Просмотрите статус текущей рабочей директории и staging-области снова:

```shell
git status
```

6. Вы также можете добавить все изменения в staging-область:

```shell
git add.
```

7. Просмотрите статус текущей рабочей директории и staging-области снова:

```shell
git status
```

Вот результат:

![Git staging area status](../assets/challenge-stage-files-step1-1.png)
