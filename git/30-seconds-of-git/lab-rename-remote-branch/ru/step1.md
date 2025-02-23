# Переименование удаленной ветки

Для завершения этого лабара вы будете использовать репозиторий Git `git-playground` из вашего аккаунта GitHub, который является форком `https://github.com/labex-labs/git-playground.git`. Пожалуйста, снимите флажок "Копировать только ветку master" при создании форка.

У вас есть репозиторий Git по адресу `https://github.com/your-username/git-playground`. Вы создали ветку под названием `feature-branch` и отправили ее на удалённый репозиторий. Теперь вы хотите переименовать ветку в `new-feature-1` и локально, и удаленно.

1. Клонируйте репозиторий, перейдите в директорию и настройте свою личность:
   ```shell
   git clone https://github.com/your-username/git-playground.git
   cd git-playground
   git config --global user.name "your-username"
   git config --global user.email "your-email"
   ```
2. Переключитесь на ветку `feature-branch`:
   ```shell
   git checkout feature-branch
   ```
3. Переименуйте ветку и локально, и удаленно:
   ```shell
   git branch -m feature-branch new-feature-1
   git push origin --delete feature-branch
   git push -u origin new-feature-1
   ```
4. Проверьте, что ветка переименована:
   ```shell
   git branch -a
   ```

Вот результат выполнения `git branch -a`:

```shell
* master
new-feature-1
remotes/origin/HEAD - > origin/master
remotes/origin/master
remotes/origin/new-feature-1
```
