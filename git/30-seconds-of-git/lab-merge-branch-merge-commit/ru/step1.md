# Объединить ветвь и создать коммит слияния

В качестве разработчика вы, возможно, захотите объединить ветвь в текущую ветвь, создав коммит слияния. Это может быть немного сложно, если вы не знакомы с Git. Задача - объединить ветвь в текущую ветвь, создав коммит слияния, используя репозиторий Git по адресу `https://github.com/labex-labs/git-playground` в директории.

Для этого задания давайте используем репозиторий из `https://github.com/labex-labs/git-playground`.

1. Клонировать репозиторий из `https://github.com/labex-labs/git-playground.git`:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Перейти в директорию и настроить идентификацию:

```shell
cd git-playground
git config --global user.name "ваше-имя-пользователя"
git config --global user.email "ваша-email"
```

3. Создать и переключиться на ветвь с именем `feature-branch`:

```shell
git checkout -b feature-branch
```

4. Добавить "This is a new line." в файл `README.md`, добавить его в область подготовки и закоммитить, комментарий к коммиту - "Add new line to README.md":

```shell
echo "This is a new line." >> README.md
git add.
git commit -am "Add new line to README.md"
```

5. Переключиться на ветвь `master`:

```shell
git checkout master
```

6. Объединить ветвь `feature-branch` в ветвь `master`, что создаст коммит слияния с сообщением "Merge feature-branch":

```shell
git merge --no-ff -m "Merge feature-branch" feature-branch
```

Вот результат выполнения `git log`:

```shell



ADD new line to README.md
```
