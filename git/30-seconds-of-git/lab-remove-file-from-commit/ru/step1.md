# Удалить файл из последнего коммита

Вы добавили файл в последний коммит, который вы не планировали включать. Теперь вы хотите удалить этот файл из последнего коммита, не меняя при этом его сообщение.

Для этого лабораторной работы давайте используем репозиторий из `https://github.com/labex-labs/git-playground`. Предположим, у вас есть репозиторий Git под названием `git-playground` с файлом `file2.txt`, который вы случайно добавили в последний коммит. Вот шаги по удалению файла из последнего коммита:

1. Клонируйте репозиторий, перейдите в директорию и настройте идентификацию:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Используйте `git rm --cached <file>`, чтобы удалить указанный `<file>` из индекса:

```shell
git rm --cached file2.txt
```

3. Используйте `git commit --amend`, чтобы обновить содержимое последнего коммита, не меняя при этом его сообщение:

```shell
git commit --amend --allow-empty
```

Если коммит становится пустым после удаления файла, используйте `--allow-empty`, в противном случае можно опустить его.

После выполнения этих команд файл `file2.txt` будет удален из последнего коммита без изменения его сообщения.

Вот что происходит, когда вы удаляете `file2.txt` из контроля версий Git:

```shell
On branch master

Changes to be committed:
(use "git restore --staged <file>..." to unstage)
deleted: file2.txt

Untracked files:
(use "git add <file>..." to include in what will be committed)
file2.txt
```
