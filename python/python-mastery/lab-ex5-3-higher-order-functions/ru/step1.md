# Использование функций высшего порядка

В настоящее время программа `reader.py` состоит из двух основных функций: `csv_as_dicts()` и `csv_as_instances()`. Код в этих двух функциях почти идентичен. Например:

```python
def csv_as_dicts(lines, types, *, headers=None):
    '''
    Преобразует строки CSV-данных в список словарей
    '''
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = { name: func(val)
                   for name, func, val in zip(headers, types, row) }
        records.append(record)
    return records

def csv_as_instances(lines, cls, *, headers=None):
    '''
    Преобразует строки CSV-данных в список экземпляров
    '''
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records
```

Объедините ядро этих функций в одну функцию `convert_csv()`, которая принимает пользовательскую функцию преобразования в качестве аргумента. Например:

```python
>>> def make_dict(headers, row):
        return dict(zip(headers, row))

>>> lines = open('portfolio.csv')
>>> convert_csv(lines, make_dict)
[{'name': 'AA','shares': '100', 'price': '32.20'}, {'name': 'IBM','shares': '50', 'price': '91.10'},
 {'name': 'CAT','shares': '150', 'price': '83.44'}, {'name': 'MSFT','shares': '200', 'price': '51.23'},
 {'name': 'GE','shares': '95', 'price': '40.37'}, {'name': 'MSFT','shares': '50', 'price': '65.10'},
 {'name': 'IBM','shares': '100', 'price': '70.44'}]
>>>
```

Перепишите функции `csv_as_dicts()` и `csv_as_instances()` с использованием новой функции `convert_csv()`.
