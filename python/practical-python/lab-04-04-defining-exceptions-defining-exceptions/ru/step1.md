# Упражнение 4.11: Определение пользовательского исключения

Часто считается хорошей практикой для библиотек определять свои собственные исключения.

Это делает легче различать между исключениями Python, возникающими в ответ на общие ошибки программирования, и исключениями, которые специально вызывает библиотека, чтобы сигнализировать о конкретной проблеме использования.

Измените функцию `create_formatter()` из предыдущего упражнения так, чтобы она вызывала пользовательское исключение `FormatError`, когда пользователь указывает неправильное имя формата.

Например:

```python
>>> from tableformat import create_formatter
>>> formatter = create_formatter('xls')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "tableformat.py", line 80, in create_formatter
    raise FormatError(f"Unknown table format {name}")
tableformat.FormatError: Unknown table format xls
>>>
```
