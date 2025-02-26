# Упражнение 3.4: Создание селектора столбцов

В многих случаях вам интересно только выбранные столбцы из CSV-файла, а не все данные. Измените функцию `parse_csv()`, чтобы она по выбору пользователя позволяла выбирать определенные столбцы следующим образом:

```python
>>> # Считываем все данные
>>> portfolio = parse_csv('/home/labex/project/portfolio.csv')
>>> portfolio
[{'name': 'AA','shares': '100', 'price': '32.20'}, {'name': 'IBM','shares': '50', 'price': '91.10'}, {'name': 'CAT','shares': '150', 'price': '83.44'}, {'name': 'MSFT','shares': '200', 'price': '51.23'}, {'name': 'GE','shares': '95', 'price': '40.37'}, {'name': 'MSFT','shares': '50', 'price': '65.10'}, {'name': 'IBM','shares': '100', 'price': '70.44'}]

>>> # Считываем только некоторые данные
>>> shares_held = parse_csv('/home/labex/project/portfolio.csv', select=['name','shares'])
>>> shares_held
[{'name': 'AA','shares': '100'}, {'name': 'IBM','shares': '50'}, {'name': 'CAT','shares': '150'}, {'name': 'MSFT','shares': '200'}, {'name': 'GE','shares': '95'}, {'name': 'MSFT','shares': '50'}, {'name': 'IBM','shares': '100'}]
>>>
```

Пример селектора столбцов был приведен в упражнении 2.23. Однако, вот один способ сделать это:

```python
# fileparse_3.4.py
import csv

def parse_csv(filename, select=None):
    '''
    Парсит CSV-файл в список записей
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # Считываем заголовки файла
        headers = next(rows)

        # Если был задан селектор столбцов, найдем индексы указанных столбцов.
        # Также уточним набор заголовков, используемых для результирующих словарей
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:    # Пропускаем строки без данных
                continue
            # Фильтруем строку, если были выбраны конкретные столбцы
            if indices:
                row = [ row[index] for index in indices ]

            # Создаем словарь
            record = dict(zip(headers, row))
            records.append(record)

    return records
```

В этом разделе есть несколько сложных моментов. Возможно, наиболее важный из них - это сопоставление выбора столбцов с индексами строк. Например, предположим, что входной файл имеет следующие заголовки:

```python
>>> headers = ['name', 'date', 'time','shares', 'price']
>>>
```

Теперь предположим, что выбранные столбцы следующие:

```python
>>> select = ['name','shares']
>>>
```

Для правильного выбора необходимо сопоставить имена выбранных столбцов с индексами столбцов в файле. Именно это делает эта часть:

```python
>>> indices = [headers.index(colname) for colname in select ]
>>> indices
[0, 3]
>>>
```

Другими словами, "name" - это столбец 0, а "shares" - столбец 3. Когда вы читаете строку данных из файла, индексы используются для ее фильтрации:

```python
>>> row = ['AA', '6/11/2007', '9:50am', '100', '32.20' ]
>>> row = [ row[index] for index in indices ]
>>> row
['AA', '100']
>>>
```
