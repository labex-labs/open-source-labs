# Скопировать файл из другой ветви

Вы работаете над проектом в репозитории Git по адресу `https://github.com/labex-labs/git-playground.git`. У вас есть две ветви с именами `feature-1` и `feature-2`. Вам нужно скопировать файл `hello.txt` из ветви `feature-1` в ветвь `feature-2`.

## Задачи

1. Перейдите в директорию и настройте идентификацию.
2. Создайте и переключитесь на ветвь `feature-1`, создайте текстовый файл с именем `hello.txt` и запишите в него строку "hello,world", а затем зафиксируйте файл с комментарием "add hello.txt".
3. Создайте и переключитесь на ветвь `feature-2` после переключения на ветвь `master`.
4. Скопируйте файл `hello.txt` из ветви `feature-1` в ветвь `feature-2` и зафиксируйте его с комментарием "copy hello.txt".
5. Проверьте, что файл `hello.txt` был скопирован в ветвь `feature-2`.

В списке файлов в ветви `feature-2` вы должны увидеть файл `hello.txt`:

```
-rw-r--r-- 1 labex labex 15 Jul 12 22:43 file1.txt
-rw-r--r-- 1 labex labex 15 Jul 12 22:43 file2.txt
-rw-r--r-- 1 labex labex 12 Jul 12 22:50 hello.txt
-rw-r--r-- 1 labex labex 32 Jul 12 22:43 README.md
```
