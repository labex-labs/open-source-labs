# Проблема: Главные скрипты

Запуск подмодуля пакета в качестве основного скрипта завершается ошибкой.

```bash
$ python porty/pcost.py # BREAKS
...
```

_Причина: Вы запускаете Python на одном файле, и Python не видит остальную структуру пакета правильно (`sys.path` неправильный)._

Все импорты завершаются ошибкой. Чтобы исправить это, вам нужно запускать программу по-другому, используя параметр `-m`.

```bash
$ python -m porty.pcost # WORKS
...
```
