# Загрузка модуля

Каждый модуль загружается и выполняется только _один раз_. _Примечание: Повторный импорт просто возвращает ссылку на ранее загруженный модуль._

`sys.modules` - это словарь всех загруженных модулей.

```python
>>> import sys
>>> sys.modules.keys()
['copy_reg', '__main__', 'site', '__builtin__', 'encodings', 'encodings.encodings', 'posixpath',...]
>>>
```

**Внимание:** Часто возникает путаница, если вы повторяете инструкцию `import` после изменения исходного кода модуля. В силу кеша модулей `sys.modules`, повторный импорт всегда возвращает ранее загруженный модуль - даже если были внесены изменения. Самый безопасный способ загрузить измененный код в Python - выйти и перезапустить интерпретатор.
