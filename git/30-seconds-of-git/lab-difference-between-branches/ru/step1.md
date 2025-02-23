# Различия между ветками

Вы работаете над проектом в своей команде и создали ветку с именем `feature-1`, чтобы работать над новой функцией. Ваш коллега также создал ветку с именем `feature-2`, чтобы работать над другой функцией. Вы хотите сравнить изменения между двумя ветками, чтобы увидеть, что было добавлено, изменено или удалено. Как можно просмотреть различия между двумя ветками?

Предположим, что ваш аккаунт на GitHub клонирует репозиторий под названием `git-playground` из `https://github.com/labex-labs/git-playground.git`. Следуйте шагам ниже:

1. Перейдите в директорию репозитория с помощью команды `cd git-playground`.
2. Настройте свой аккаунт GitHub в этой среде с помощью команд `git config --global user.name "Ваше имя"` и `git config --global user.email "ваш_электронная_почта@example.com"`.
3. Создайте и переключитесь на ветку `feature-1` с помощью команды `git checkout -b feature-1`, добавьте "hello" в файл `README.md`, добавьте его в staging-область и зафиксируйте изменения, комментарий к коммиту - "Add new content to README.md" с помощью команд `echo "hello" >> README.md `, `git add.` и `git commit -am "Add new content to README.md"`.
4. Переключитесь обратно на ветку `master`.
5. Создайте и переключитесь на ветку `feature-2` с помощью команды `git checkout -b feature-2`, добавьте "world" в файл `index.html`, добавьте его в staging-область и зафиксируйте изменения, комментарий к коммиту - "Update index.html file" с помощью команд `echo "world" > index.htm`, `git add.` и `git commit -am "Update index.html file"`.
6. Просмотрите различия между двумя ветками с помощью команды `git diff feature-1..feature-2`.

Вывод должен показать различия между ветками `feature-1` и `feature-2`. Это показывает, как будет выглядеть конечный результат:

```shell
diff --git a/README.md b/README.md
index b66215f..0164284 100644
--- a/README.md
+++ b/README.md
@@ -1,3 +1,2 @@
# git-playground
Git Playground
-hello
diff --git a/index.html b/index.html
new file mode 100644
index 0000000..cc628cc
--- /dev/null
+++ b/index.html
@@ -0,0 +1 @@
+world
```
