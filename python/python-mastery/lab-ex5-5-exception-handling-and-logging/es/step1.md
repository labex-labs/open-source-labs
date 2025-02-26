# Preparación

En el archivo `reader.py`, hay una función central `convert_csv()` que realiza la mayor parte del trabajo. Esta función se detiene si se ejecuta con datos faltantes o incorrectos. Por ejemplo:

```bash
$ python
>>> from reader import read_csv_as_dicts
```

```python
>>> port = read_csv_as_dicts('missing.csv', types=[str, int, float])
Traceback (most recent call last):
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
ValueError: invalid literal for int() with base 10: ''
>>>
```
