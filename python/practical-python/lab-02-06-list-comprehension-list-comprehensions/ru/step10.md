# Упражнение 2.23: Извлечение данных из CSV-файлов

Знание, как использовать различные комбинации списочных, множественных и словарных включений, может быть полезно при различных формах обработки данных. Вот пример, который показывает, как извлекать выбранные столбцы из CSV-файла.

Во - первых, прочитайте строку с информацией о заголовках из CSV-файла:

```python
>>> import csv
>>> f = open('portfoliodate.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> headers
['name', 'date', 'time','shares', 'price']
>>>
```

Далее, определите переменную, которая перечисляет столбцы, которые вас на самом деле интересуют:

```python
>>> select = ['name','shares', 'price']
>>>
```

Теперь, определите индексы вышеперечисленных столбцов в исходном CSV-файле:

```python
>>> indices = [ headers.index(colname) for colname in select ]
>>> indices
[0, 3, 4]
>>>
```

Наконец, прочитайте строку данных и превратите ее в словарь с использованием словарного включения:

```python
>>> row = next(rows)
>>> record = { colname: row[index] for colname, index in zip(select, indices) }   # dict-comprehension
>>> record
{'price': '32.20', 'name': 'AA','shares': '100'}
>>>
```

Если вы чувствуете себя комфортно с тем, что только произошло, прочитайте остальную часть файла:

```python
>>> portfolio = [ { colname: row[index] for colname, index in zip(select, indices) } for row in rows ]
>>> portfolio
[{'price': '91.10', 'name': 'IBM','shares': '50'}, {'price': '83.44', 'name': 'CAT','shares': '150'},
  {'price': '51.23', 'name': 'MSFT','shares': '200'}, {'price': '40.37', 'name': 'GE','shares': '95'},
  {'price': '65.10', 'name': 'MSFT','shares': '50'}, {'price': '70.44', 'name': 'IBM','shares': '100'}]
>>>
```

О, боже мой, вы только что свели большую часть функции `read_portfolio()` до одного выражения.
