# Ручной поиск коммита, в котором был обнаружен баг

Ваша задача - вручную найти коммит, в котором был обнаружен баг в репозитории `git-playground`. Репозиторий можно найти по адресу `https://github.com/labex-labs/git-playground`.

Для завершения этого испытания вам нужно провести бинарный поиск по истории коммитов репозитория. Вам нужно помечать коммиты как "хорошие" (без багов) или "плохие" (с багами), пока не уточните коммит, в котором был обнаружен баг.

## Задачи

Сообщение об ошибке гласит, что файл `file2.txt` должен выводить "This is file2.txt.", а не "This is file2.".

1. Перейдите в директорию репозитория.
2. Начните бинарный поиск.
3. Пометьте текущий коммит как "плохой".
4. Пометьте коммит с сообщением "Initial commit" как "хороший". Git автоматически переключится на новый коммит для тестирования.
5. Если содержимое проверенного файла `file2.txt` не соответствует ошибке, пометьте его как "хороший".
6. Если содержимое проверенного файла `file2.txt` соответствует ошибке, пометьте его как "плохой".
7. Как только вы найдете коммит с багом, выйдите из бинарного поиска.

Теперь вы можете изучить изменения кода в коммите с багом, чтобы найти источник ошибки.

Вот результат теста:

```
d22f46ba8c2d4e07d773c5126e9c803933eb5898 - первый плохой коммит
commit d22f46ba8c2d4e07d773c5126e9c803933eb5898
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt

 file2.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 file2.txt
```
