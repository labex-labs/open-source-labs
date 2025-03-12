# Обработка CSV-файлов без заголовков

В мире обработки данных не все CSV-файлы имеют заголовки в первой строке. Заголовки - это имена, присвоенные каждой колонке в CSV-файле, которые помогают нам понять, какого рода данные содержит каждая колонка. Когда в CSV-файле отсутствуют заголовки, нам нужно уметь правильно с ним работать. В этом разделе мы модифицируем наши функции, чтобы позволить вызывающему коду вручную задавать заголовки, так что мы сможем работать как с CSV-файлами с заголовками, так и без них.

1. Откройте файл `reader.py` и обновите его, добавив обработку заголовков:

```python
# reader.py

import csv

def csv_as_dicts(lines, types, headers=None):
    '''
    Parse CSV data from an iterable into a list of dictionaries

    Args:
        lines: An iterable producing CSV lines
        types: List of type conversion functions for each column
        headers: Optional list of column names. If None, first row is used as headers

    Returns:
        List of dictionaries with data from the CSV lines
    '''
    records = []
    rows = csv.reader(lines)

    if headers is None:
        # Use the first row as headers if none provided
        headers = next(rows)

    for row in rows:
        record = { name: func(val)
                  for name, func, val in zip(headers, types, row) }
        records.append(record)
    return records

def csv_as_instances(lines, cls, headers=None):
    '''
    Parse CSV data from an iterable into a list of class instances

    Args:
        lines: An iterable producing CSV lines
        cls: Class to create instances from
        headers: Optional list of column names. If None, first row is used as headers

    Returns:
        List of class instances with data from the CSV lines
    '''
    records = []
    rows = csv.reader(lines)

    if headers is None:
        # Skip the first row if no headers provided
        next(rows)

    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records

def read_csv_as_dicts(filename, types, headers=None):
    '''
    Read CSV data into a list of dictionaries with optional type conversion

    Args:
        filename: Path to the CSV file
        types: List of type conversion functions for each column
        headers: Optional list of column names. If None, first row is used as headers

    Returns:
        List of dictionaries with data from the CSV file
    '''
    with open(filename) as file:
        return csv_as_dicts(file, types, headers)

def read_csv_as_instances(filename, cls, headers=None):
    '''
    Read CSV data into a list of class instances

    Args:
        filename: Path to the CSV file
        cls: Class to create instances from
        headers: Optional list of column names. If None, first row is used as headers

    Returns:
        List of class instances with data from the CSV file
    '''
    with open(filename) as file:
        return csv_as_instances(file, cls, headers)
```

Понять ключевые изменения, которые мы внесли в эти функции:

1. Мы добавили параметр `headers` во все функции и установили его значение по умолчанию равным `None`. Это означает, что если вызывающий код не предоставит заголовки, функции будут использовать поведение по умолчанию.
2. В функции `csv_as_dicts` мы используем первую строку как заголовки только в том случае, если параметр `headers` равен `None`. Это позволяет нам автоматически обрабатывать файлы с заголовками.
3. В функции `csv_as_instances` мы пропускаем первую строку только в том случае, если параметр `headers` равен `None`. Это связано с тем, что если мы предоставляем свои собственные заголовки, первая строка файла содержит реальные данные, а не заголовки.

4. Протестируем эти изменения на файле без заголовков. Создайте файл с именем `test_headers.py`:

```python
# test_headers.py

import reader
import stock

# Define column names for the file without headers
column_names = ['name', 'shares', 'price']

# Test reading a file without headers
portfolio = reader.read_csv_as_dicts('portfolio_noheader.csv',
                                     [str, int, float],
                                     headers=column_names)
print("First item from file without headers:", portfolio[0])
print("Total items:", len(portfolio))

# Test reading the same file as instances
portfolio = reader.read_csv_as_instances('portfolio_noheader.csv',
                                        stock.Stock,
                                        headers=column_names)
print("\nFirst item as Stock instance:", portfolio[0])
print("Total items:", len(portfolio))

# Verify that original functionality still works
portfolio = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
print("\nFirst item from file with headers:", portfolio[0])
```

В этом тестовом скрипте мы сначала определяем имена колонок для файла без заголовков. Затем тестируем чтение файла без заголовков в виде списка словарей и в виде списка экземпляров класса. Наконец, проверяем, что исходная функциональность по-прежнему работает, читая файл с заголовками.

3. Запустите тестовый скрипт из терминала:

```bash
python test_headers.py
```

Вывод должен быть похож на следующий:

```
First item from file without headers: {'name': 'AA', 'shares': 100, 'price': 32.2}
Total items: 7

First item as Stock instance: Stock('AA', 100, 32.2)
Total items: 7

First item from file with headers: {'name': 'AA', 'shares': 100, 'price': 32.2}
```

Этот вывод подтверждает, что наши функции теперь могут обрабатывать как CSV-файлы с заголовками, так и без них. Пользователь может задавать имена колонок при необходимости или полагаться на поведение по умолчанию, которое считывает заголовки из первой строки.

Благодаря этой модификации наши функции для чтения CSV-файлов стали более универсальными и могут обрабатывать более широкий спектр форматов файлов. Это важный шаг в направлении создания более надежного и полезного кода в различных сценариях.
