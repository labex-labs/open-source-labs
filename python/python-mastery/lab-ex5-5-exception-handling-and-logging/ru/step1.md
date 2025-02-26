# Подготовка

В файле `reader.py` есть центральная функция `convert_csv()`, которая выполняет большую часть работы. Эта функция завершается с ошибкой, если ее запустить на данных с отсутствующими или некорректными данными. Например:

```bash
$ python
>>> from reader import read_csv_as_dicts
```

```python
>>> port = read_csv_as_dicts('missing.csv', types=[str, int, float])
Следующая ошибка произошла на более поздней стадии выполнения:
  File "<stdin>", line 1, in <module>
  File "reader.py", line 24, in read_csv_as_dicts
    return csv_as_dicts(file, types, headers=headers)
  File "reader.py", line 13, in csv_as_dicts
    lambda headers, row: { name: func(val) for name, func, val in zip(headers, types, row) })
  File "reader.py", line 9, in convert_csv
    return list(map(lambda row: converter(headers, row), rows))
  File "reader.py", line 9, in <lambda>
    return list(map(lambda row: converter(headers, row), rows))
  File "reader.py", line 13, in <lambda>
    lambda headers, row: { name: func(val) for name, func, val in zip(headers, types, row) })
  File "reader.py", line 13, in <dictcomp>
    lambda headers, row: { name: func(val) for name, func, val in zip(headers, types, row) })
ValueError: недействительный литерал для int() с основанием 10: ''
>>>
```
