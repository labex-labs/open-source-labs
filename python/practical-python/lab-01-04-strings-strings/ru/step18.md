# Комментарий

Когда вы начинаете экспериментировать с интерпретатором, часто хочется узнать больше о операциях, поддерживаемых различными объектами. Например, как выяснить, какие операции доступны для строки?

В зависимости от вашей среды Python вы, возможно, сможете увидеть список доступных методов с помощью автодополнения по табуляции. Например, попробуйте ввести это:

```python
>>> s = 'hello world'
>>> s.<tab key>
>>>
```

Если нажатие клавиши Tab не имеет эффекта, вы можете использовать встроенную функцию `dir()`. Например:

```python
>>> s = 'hello'
>>> dir(s)
['__add__', '__class__', '__contains__',..., 'find', 'format',
'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace',
'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition',
'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit',
'rstrip','split','splitlines','startswith','strip','swapcase',
'title', 'translate', 'upper', 'zfill']
>>>
```

`dir()` возвращает список всех операций, которые могут следовать после `(.)`. Используйте команду `help()` для получения дополнительной информации о конкретной операции:

```python
>>> help(s.upper)
Help on built-in function upper:

upper(...)
    S.upper() -> string

    Return a copy of the string S converted to uppercase.
>>>
```
