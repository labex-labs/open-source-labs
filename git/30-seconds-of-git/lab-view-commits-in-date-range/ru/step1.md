# Клонирование Git-репозитория

Для начала исследования возможностей фильтрации по диапазону дат в Git нам сначала нужен Git-репозиторий, с которым мы будем работать. Мы будем использовать репозиторий `git-playground`, предоставленный LabEx.

Начнем с клонирования репозитория:

1. Откройте терминал в виртуальной машине LabEx.

![терминал](../assets/screenshot-20250306-shbu3WrQ@2x.png)

2. Выполните следующую команду для клонирования репозитория:

```bash
git clone https://github.com/labex-labs/git-playground
```

Вы должны увидеть вывод, похожий на следующий:

```
Cloning into 'git-playground'...
remote: Enumerating objects: 8, done.
remote: Counting objects: 100% (8/8), done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 8 (delta 0), reused 8 (delta 0), pack-reused 0
Receiving objects: 100% (8/8), done.
```

3. Перейдите в директорию репозитория:

```bash
cd git-playground
```

Теперь, когда у нас есть репозиторий на локальной машине, мы можем приступить к изучению истории коммитов (коммитов - это записи о внесенных изменениях в репозиторий).
