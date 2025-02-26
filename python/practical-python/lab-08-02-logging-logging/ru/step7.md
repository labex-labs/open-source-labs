# Упражнение 8.2: Добавление журналирования в модуль

В `fileparse.py` есть некоторые обработчики ошибок, связанные с исключениями, вызванными неправильными входными данными. Они выглядят так:

```python
# fileparse.py
import csv

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records with type conversion.
    '''
    if select and not has_headers:
        raise RuntimeError('select requires column headers')

    rows = csv.reader(lines, delimiter=delimiter)

    # Read the file headers (if any)
    headers = next(rows) if has_headers else []

    # If specific columns have been selected, make indices for filtering and set output columns
    if select:
        indices = [ headers.index(colname) for colname in select ]
        headers = select

    records = []
    for rowno, row in enumerate(rows, 1):
        if not row:     # Skip rows with no data
            continue

        # If specific column indices are selected, pick them out
        if select:
            row = [ row[index] for index in indices]

        # Apply type conversion to the row
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {rowno}: Couldn't convert {row}")
                    print(f"Row {rowno}: Reason {e}")
                continue

        # Make a dictionary or a tuple
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records
```

Обратите внимание на инструкции `print`, которые выводят диагностические сообщения. Замена этих `print` на операции журналирования относительно проста. Измените код так:

```python
# fileparse.py
import csv
import logging
log = logging.getLogger(__name__)

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records with type conversion.
    '''
    if select and not has_headers:
        raise RuntimeError('select requires column headers')

    rows = csv.reader(lines, delimiter=delimiter)

    # Read the file headers (if any)
    headers = next(rows) if has_headers else []

    # If specific columns have been selected, make indices for filtering and set output columns
    if select:
        indices = [ headers.index(colname) for colname in select ]
        headers = select

    records = []
    for rowno, row in enumerate(rows, 1):
        if not row:     # Skip rows with no data
            continue

        # If specific column indices are selected, pick them out
        if select:
            row = [ row[index] for index in indices]

        # Apply type conversion to the row
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    log.warning("Row %d: Couldn't convert %s", rowno, row)
                    log.debug("Row %d: Reason %s", rowno, e)
                continue

        # Make a dictionary or a tuple
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records
```

Теперь, когда вы внесли эти изменения, попробуйте использовать часть своего кода с неправильными данными.

```python
>>> import report
>>> a = report.read_portfolio('missing.csv')
Row 4: Bad row: ['MSFT', '', '51.23']
Row 7: Bad row: ['IBM', '', '70.44']
>>>
```

Если вы ничего не сделаете, вы получите только сообщения журнала уровня `WARNING` и выше. Вывод будет выглядеть как простые инструкции `print`. Однако, если вы настроите модуль журналирования, вы получите дополнительную информацию о уровнях журналирования, модуле и т.д. Введите эти шаги, чтобы увидеть это:

```python
>>> import logging
>>> logging.basicConfig()
>>> a = report.read_portfolio('missing.csv')
WARNING:fileparse:Row 4: Bad row: ['MSFT', '', '51.23']
WARNING:fileparse:Row 7: Bad row: ['IBM', '', '70.44']
>>>
```

Вы заметите, что не видите вывод операции `log.debug()`. Введите это, чтобы изменить уровень.

```python
>>> logging.getLogger('fileparse').setLevel(logging.DEBUG)
>>> a = report.read_portfolio('missing.csv')
WARNING:fileparse:Row 4: Bad row: ['MSFT', '', '51.23']
DEBUG:fileparse:Row 4: Reason: invalid literal for int() with base 10: ''
WARNING:fileparse:Row 7: Bad row: ['IBM', '', '70.44']
DEBUG:fileparse:Row 7: Reason: invalid literal for int() with base 10: ''
>>>
```

Отключите все, кроме наиболее критичных сообщений журнала:

```python
>>> logging.getLogger('fileparse').setLevel(logging.CRITICAL)
>>> a = report.read_portfolio('missing.csv')
>>>
```
