# Настройка текстового редактора Git

Для этого лабораторийского занятия давайте используем репозиторий из `https://github.com/labex-labs/git-playground`. Вы хотите настроить текстовый редактор, используемый Git, на свой предпочитаемый редактор.

1. Клонируйте репозиторий `git-playground`:

```shell
git clone https://github.com/labex-labs/git-playground
```

2. Перейдите в клонированный репозиторий и настройте идентификацию:

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

3. Настройте Git для использования вашего предпочитаемого текстового редактора (в этом примере мы будем использовать vim):

```shell
git config --global core.editor "vim"
```

4. внесите изменения в файл и подготовьте его к коммиту:

```shell
echo "Hello, Git" > hello.txt
git add hello.txt
```

5. Зафиксируйте изменения:

```shell
git commit
```

6. Ваш предпочитаемый текстовый редактор (в этом примере vim) должен открыться с сообщением коммита. Запишите сообщение коммита "Update hello.txt" и сохраните файл.
7. Закройте текстовый редактор. Коммит будет сделан с сообщением, которое вы написали.

Вот результат:

```shell
commit 1f19499s5387a1549f1bb5286d3d0a2b993f87e0 (HEAD -> master)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 19:26:57 2023 +0800

    Update hello.txt
```
