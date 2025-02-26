# Использование функции zip()

Функция `zip()` наиболее часто используется для объединения данных. Например, вспомните, что вы создали переменную `headers`:

```python
>>> headers
['name','shares', 'price']
>>>
```

Это может быть полезно для комбинирования с другими данными строк:

```python
>>> row = rows[0]
>>> row
['AA', '100', '32.20']
>>> for col, val in zip(headers, row):
        print(col, val)

name AA
shares 100
price 32.20
>>>
```

Или, возможно, вы можете использовать ее для создания словаря:

```python
>>> dict(zip(headers, row))
{'name': 'AA','shares': '100', 'price': '32.20'}
>>>
```

Или, возможно, последовательности словарей:

```python
>>> for row in rows:
        record = dict(zip(headers, row))
        print(record)

{'name': 'AA','shares': '100', 'price': '32.20'}
{'name': 'IBM','shares': '50', 'price': '91.10'}
{'name': 'CAT','shares': '150', 'price': '83.44'}
{'name': 'MSFT','shares': '200', 'price': '51.23'}
{'name': 'GE','shares': '95', 'price': '40.37'}
{'name': 'MSFT','shares': '50', 'price': '65.10'}
{'name': 'IBM','shares': '100', 'price': '70.44'}
>>>
```
