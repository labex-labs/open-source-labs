# Удалить удаленную ветку

Иногда вам может потребоваться удалить удаленную ветку, которая больше не нужна. Например, если ветка с функцией была объединена в основную ветку, вы, возможно, захотите удалить удаленную ветку с функцией, чтобы сделать репозиторий чище.

Предположим, что репозиторий GitHub под названием `git-playground` был склонирован из вашего аккаунта GitHub, который является форком `https://github.com/labex-labs/git-playground.git`. Вы хотите удалить удаленную ветку с именем `feature-branch`, которая больше не нужна. Вот шаги по удалению удаленной ветки:

1. Склоняйте репозиторий, перейдите в каталог и настройте идентификацию:
   ```shell
   git clone https://github.com/your-username/git-playground.git
   cd git-playground
   git config --global user.name "your-username"
   git config --global user.email "your-email"
   ```
2. Добавьте ветку `feature-branch` в удаленный репозиторий `origin`:
   ```shell
   git checkout -b feature-branch
   git push -u origin feature-branch
   ```
3. Используйте команду `git branch -r`, чтобы вывести список всех удаленных веток.
   ```shell
   git branch -r
   ```
   В выводе должен быть удаленный репозиторий `feature-branch`:
   ```
   origin/HEAD -> origin/master
   origin/feature-branch
   origin/master
   ```
4. Используйте команду `git push -d <remote> <branch>`, чтобы удалить указанную удаленную `<branch>` на заданном `<remote>`.
   ```shell
   git push -d origin feature-branch
   ```
   Эта команда удаляет удаленную ветку `feature-branch` в удаленном репозитории `origin`.
5. Используйте команду `git branch -r` снова, чтобы проверить, удалилась ли удаленная ветка.
   ```shell
   git branch -r
   ```
   В выводе не должно быть удаленной ветки `feature-branch`:
   ```
   origin/HEAD -> origin/master
   origin/master
   ```
