# Сделать функции более гибкими

В настоящее время наши функции ограничены чтением из файлов, указанных по имени файла. Это ограничивает их применимость. В программировании часто бывает полезно сделать функции более гибкими, чтобы они могли обрабатывать различные типы входных данных. В нашем случае было бы здорово, если бы наши функции могли работать с любым итерируемым объектом, который генерирует строки, например, с объектами файлов или другими источниками. Таким образом, мы сможем использовать эти функции в более широком спектре сценариев, например, при чтении из сжатых файлов или других потоков данных.

Давайте рефакторинг нашего кода, чтобы обеспечить такую гибкость:

1. Откройте файл `reader.py`. Мы собираемся изменить его, добавив несколько новых функций. Эти новые функции позволят нашему коду работать с разными типами итерируемых объектов. Вот код, который вам нужно добавить:

```python
# reader.py

import csv

def csv_as_dicts(lines, types):
    '''
    Parse CSV data from an iterable into a list of dictionaries

    Args:
        lines: An iterable producing CSV lines
        types: List of type conversion functions for each column

    Returns:
        List of dictionaries with data from the CSV lines
    '''
    records = []
    rows = csv.reader(lines)
    headers = next(rows)
    for row in rows:
        record = { name: func(val)
                  for name, func, val in zip(headers, types, row) }
        records.append(record)
    return records

def csv_as_instances(lines, cls):
    '''
    Parse CSV data from an iterable into a list of class instances

    Args:
        lines: An iterable producing CSV lines
        cls: Class to create instances from

    Returns:
        List of class instances with data from the CSV lines
    '''
    records = []
    rows = csv.reader(lines)
    headers = next(rows)
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records

def read_csv_as_dicts(filename, types):
    '''
    Read CSV data into a list of dictionaries with optional type conversion

    Args:
        filename: Path to the CSV file
        types: List of type conversion functions for each column

    Returns:
        List of dictionaries with data from the CSV file
    '''
    with open(filename) as file:
        return csv_as_dicts(file, types)

def read_csv_as_instances(filename, cls):
    '''
    Read CSV data into a list of class instances

    Args:
        filename: Path to the CSV file
        cls: Class to create instances from

    Returns:
        List of class instances with data from the CSV file
    '''
    with open(filename) as file:
        return csv_as_instances(file, cls)
```

Давайте рассмотрим более подробно, как мы рефакторинг кода:

1. Мы создали две более общие функции, `csv_as_dicts()` и `csv_as_instances()`. Эти функции предназначены для работы с любым итерируемым объектом, который генерирует строки CSV. Это означает, что они могут обрабатывать различные типы источников входных данных, а не только файлы, указанные по имени файла.
2. Мы перереализовали `read_csv_as_dicts()` и `read_csv_as_instances()` так, чтобы они использовали эти новые функции. Таким образом, исходная функциональность чтения из файла по имени файла по-прежнему доступна, но теперь она основана на более гибких функциях.
3. Этот подход сохраняет обратную совместимость с существующим кодом. Это означает, что любой код, который использовал старые функции, по-прежнему будет работать как ожидается. В то же время наша библиотека становится более гибкой, так как теперь может обрабатывать различные типы источников входных данных.

4. Теперь давайте протестируем эти новые функции. Создайте файл с именем `test_reader_flexibility.py` и добавьте в него следующий код. Этот код протестирует новые функции с разными типами источников входных данных:

```python
# test_reader_flexibility.py

import reader
import stock
import gzip

# Test opening a regular file
with open('portfolio.csv') as file:
    portfolio = reader.csv_as_dicts(file, [str, int, float])
    print("First item from open file:", portfolio[0])

# Test opening a gzipped file
with gzip.open('portfolio.csv.gz', 'rt') as file:  # 'rt' means read text
    portfolio = reader.csv_as_instances(file, stock.Stock)
    print("\nFirst item from gzipped file:", portfolio[0])

# Test backward compatibility
portfolio = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
print("\nFirst item using backward compatible function:", portfolio[0])
```

3. После создания тестового файла нам нужно запустить тестовый скрипт из терминала. Откройте терминал и перейдите в директорию, где находится файл `test_reader_flexibility.py`. Затем выполните следующую команду:

```bash
python test_reader_flexibility.py
```

Вывод должен быть похож на следующий:

```
First item from open file: {'name': 'AA', 'shares': 100, 'price': 32.2}

First item from gzipped file: Stock('AA', 100, 32.2)

First item using backward compatible function: {'name': 'AA', 'shares': 100, 'price': 32.2}
```

Этот вывод подтверждает, что наши функции теперь работают с разными типами источников входных данных, сохраняя при этом обратную совместимость. Рефакторинг функции могут обрабатывать данные из:

- Обычных файлов, открытых с помощью `open()`
- Сжатых файлов, открытых с помощью `gzip.open()`
- Любых других итерируемых объектов, которые генерируют строки текста

Это делает наш код гораздо более гибким и легким в использовании в различных сценариях.
