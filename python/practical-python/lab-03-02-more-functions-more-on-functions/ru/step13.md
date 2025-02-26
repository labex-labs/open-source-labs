# Упражнение 3.3: Чтение CSV-файлов

Для начала давайте сосредоточимся на задаче чтения CSV-файла в список словарей. В файле `fileparse_3.3.py` определите функцию, которая выглядит так:

```python
# fileparse_3.3.py
import csv

def parse_csv(filename):
    '''
    Парсит CSV-файл в список записей
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # Считываем заголовки файла
        headers = next(rows)
        records = []
        for row in rows:
            if not row:    # Пропускаем строки без данных
                continue
            record = dict(zip(headers, row))
            records.append(record)

    return records
```

Эта функция читает CSV-файл в список словарей, скрывая при этом детали открытия файла, оборачивания его с использованием модуля `csv`, игнорирования пустых строк и т.д.

Попробуйте ее:

Совет: `python3 -i fileparse_3.3.py`.

```python
>>> portfolio = parse_csv('/home/labex/project/portfolio.csv')
>>> portfolio
[{'name': 'AA','shares': '100', 'price': '32.20'}, {'name': 'IBM','shares': '50', 'price': '91.10'}, {'name': 'CAT','shares': '150', 'price': '83.44'}, {'name': 'MSFT','shares': '200', 'price': '51.23'}, {'name': 'GE','shares': '95', 'price': '40.37'}, {'name': 'MSFT','shares': '50', 'price': '65.10'}, {'name': 'IBM','shares': '100', 'price': '70.44'}]
>>>
```

Это хорошо, за исключением того, что с данными нельзя производить никакие полезные вычисления, потому что все представлено в виде строк. Мы скоро это исправим, но давайте продолжим работать над этим.
