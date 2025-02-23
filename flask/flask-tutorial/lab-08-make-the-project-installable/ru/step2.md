# Включить необходимые файлы

Бэкенд сборки setuptools требует еще одного файла с именем `MANIFEST.in`, чтобы включить в проект не - Python файлы.

Создайте `MANIFEST.in` с таким содержанием:

```none
# MANIFEST.in

include flaskr/schema.sql
graft flaskr/static
graft flaskr/templates
global - exclude *.pyc
```

Это говорит сборке скопировать все в директориях `static` и `templates`, а также файл `schema.sql`, при этом исключая все файлы байт - кода.
