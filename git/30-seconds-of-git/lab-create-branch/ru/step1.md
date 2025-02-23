# Создать новую ветку

Для этого практического занятия создайте форк репозитория Git по адресу `https://github.com/labex-labs/git-playground` в своем аккаунте на GitHub. Вы работаете над проектом в репозитории Git по адресу `https://github.com/your-username/git-playground`. Вам нужно создать новую ветку с именем `feature-1` для работы над новой функцией.

1. Клонируйте репозиторий, перейдите в каталог и настройте идентификацию:

```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Проверьте текущую ветку:

```shell
git branch
```

3. Создайте новую ветку с именем `feature-1`:

```shell
git checkout -b feature-1
```

4. Убедитесь, что вы сейчас на ветке `feature-1`:

```shell
git branch
```

5. Отправьте изменения в удаленный репозиторий:

```shell
git push -u origin feature-1
```

Вот что происходит, когда вы запускаете команду `git branch -r`:

![git branch remote output](../assets/challenge-create-branch-step1-1.png)
