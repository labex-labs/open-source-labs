# Добавление подсказок по типам

В Python 3.5 и более поздних версиях поддерживаются подсказки по типам (type hints). Подсказки по типам - это способ указать ожидаемые типы данных переменных, параметров функций и возвращаемых значений в вашем коде. Они не влияют на то, как код выполняется, но делают код более читаемым и могут помочь обнаружить определенные типы ошибок до того, как код будет фактически запущен. Теперь давайте добавим подсказки по типам в наши функции для чтения CSV-файлов.

1. Откройте файл `reader.py` и обновите его, добавив подсказки по типам:

```python
# reader.py

import csv
from typing import List, Callable, Dict, Any, Type, Optional, TextIO, Iterator, TypeVar

# Define a generic type for the class parameter
T = TypeVar('T')

def csv_as_dicts(lines: Iterator[str],
                types: List[Callable[[str], Any]],
                headers: Optional[List[str]] = None) -> List[Dict[str, Any]]:
    '''
    Parse CSV data from an iterable into a list of dictionaries

    Args:
        lines: An iterable producing CSV lines
        types: List of type conversion functions for each column
        headers: Optional list of column names. If None, first row is used as headers

    Returns:
        List of dictionaries with data from the CSV lines
    '''
    records: List[Dict[str, Any]] = []
    rows = csv.reader(lines)

    if headers is None:
        # Use the first row as headers if none provided
        headers = next(rows)

    for row in rows:
        record = { name: func(val)
                  for name, func, val in zip(headers, types, row) }
        records.append(record)
    return records

def csv_as_instances(lines: Iterator[str],
                    cls: Type[T],
                    headers: Optional[List[str]] = None) -> List[T]:
    '''
    Parse CSV data from an iterable into a list of class instances

    Args:
        lines: An iterable producing CSV lines
        cls: Class to create instances from
        headers: Optional list of column names. If None, first row is used as headers

    Returns:
        List of class instances with data from the CSV lines
    '''
    records: List[T] = []
    rows = csv.reader(lines)

    if headers is None:
        # Skip the first row if no headers provided
        next(rows)

    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records

def read_csv_as_dicts(filename: str,
                     types: List[Callable[[str], Any]],
                     headers: Optional[List[str]] = None) -> List[Dict[str, Any]]:
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

def read_csv_as_instances(filename: str,
                         cls: Type[T],
                         headers: Optional[List[str]] = None) -> List[T]:
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

Понять ключевые изменения, которые мы внесли в код:

1. Мы импортировали типы из модуля `typing`. Этот модуль предоставляет набор типов, которые мы можем использовать для определения подсказок по типам. Например, `List`, `Dict` и `Optional` - это типы из этого модуля.
2. Мы добавили обобщенную переменную типа `T` для представления типа класса. Обобщенная переменная типа позволяет нам писать функции, которые могут работать с разными типами в типобезопасном режиме.
3. Мы добавили подсказки по типам для всех параметров функций и возвращаемых значений. Это делает ясным, какие типы аргументов ожидает функция и какой тип значения она возвращает.
4. Мы использовали соответствующие типы контейнеров, такие как `List`, `Dict` и `Optional`. `List` представляет список, `Dict` представляет словарь, а `Optional` указывает, что параметр может иметь определенный тип или быть `None`.
5. Мы использовали `Callable` для функций преобразования типов. `Callable` используется для указания, что параметр - это функция, которую можно вызвать.
6. Мы использовали обобщенный тип `T` для указания, что `csv_as_instances` возвращает список экземпляров переданного класса. Это помогает IDE и другим инструментам понять тип возвращаемых объектов.

7. Теперь давайте создадим простой тестовый файл, чтобы убедиться, что все по-прежнему работает правильно:

```python
# test_types.py

import reader
import stock

# The functions should work exactly as before
portfolio = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
print("First item:", portfolio[0])

# But now we have better type checking and IDE support
stock_portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
print("\nFirst stock:", stock_portfolio[0])

# We can see that stock_portfolio is a list of Stock objects
# This helps IDEs provide better code completion
first_stock = stock_portfolio[0]
print(f"\nName: {first_stock.name}")
print(f"Shares: {first_stock.shares}")
print(f"Price: {first_stock.price}")
print(f"Value: {first_stock.shares * first_stock.price}")
```

3. Запустите тестовый скрипт из терминала:

```bash
python test_types.py
```

Вывод должен быть похож на следующий:

```
First item: {'name': 'AA', 'shares': 100, 'price': 32.2}

First stock: Stock('AA', 100, 32.2)

Name: AA
Shares: 100
Price: 32.2
Value: 3220.0
```

Подсказки по типам не влияют на то, как код выполняется, но они предоставляют несколько преимуществ:

1. Они обеспечивают лучшую поддержку IDE с автодополнением кода. Когда вы используете IDE, такое как PyCharm или VS Code, оно может использовать подсказки по типам, чтобы предложить правильные методы и атрибуты для ваших переменных.
2. Они предоставляют более ясную документацию о ожидаемых типах параметров и возвращаемых значений. Просто посмотрев на определение функции, вы можете понять, какие типы аргументов она ожидает и какой тип значения возвращает.
3. Они позволяют использовать статические анализаторы типов, такие как mypy, чтобы обнаружить ошибки на ранней стадии. Статические анализаторы типов анализируют ваш код без его запуска и могут найти ошибки, связанные с типами, до того, как вы запустите код.
4. Они улучшают читаемость и поддерживаемость кода. Когда вы или другие разработчики вернетесь к коду позже, будет легче понять, что код делает.

В крупном кодовом проекте эти преимущества могут значительно уменьшить количество ошибок и сделать код легче для понимания и поддержки.

**Примечание:** Подсказки по типам в Python являются необязательными, но они все чаще используются в профессиональном коде. Библиотеки, такие как те, что есть в стандартной библиотеке Python, и многие популярные сторонние пакеты теперь включают обширные подсказки по типам.
