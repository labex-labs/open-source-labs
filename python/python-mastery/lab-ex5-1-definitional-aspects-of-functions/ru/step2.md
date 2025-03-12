# Создание базовых функций для чтения CSV-файлов

Начнем с создания файла `reader.py` с двумя базовыми функциями для чтения данных из CSV-файлов. Эти функции помогут нам обрабатывать CSV-файлы различными способами, например, преобразовывать данные в словари или экземпляры классов.

Сначала нам нужно понять, что такое CSV-файл. CSV расшифровывается как Comma-Separated Values (значения, разделенные запятыми). Это простой формат файла, используемый для хранения табличных данных, где каждая строка представляет собой строку таблицы, а значения в каждой строке разделены запятыми.

Теперь создадим файл `reader.py`. Следуйте этим шагам:

1. Откройте текстовый редактор кода и создайте новый файл с именем `reader.py` в директории `/home/labex/project`. Именно здесь мы напишем наши функции для чтения данных из CSV-файлов.

2. Добавьте следующий код в файл `reader.py`:

```python
# reader.py

import csv

def read_csv_as_dicts(filename, types):
    '''
    Read CSV data into a list of dictionaries with optional type conversion

    Args:
        filename: Path to the CSV file
        types: List of type conversion functions for each column

    Returns:
        List of dictionaries with data from the CSV file
    '''
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = { name: func(val)
                       for name, func, val in zip(headers, types, row) }
            records.append(record)
    return records

def read_csv_as_instances(filename, cls):
    '''
    Read CSV data into a list of class instances

    Args:
        filename: Path to the CSV file
        cls: Class to create instances from

    Returns:
        List of class instances with data from the CSV file
    '''
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = cls.from_row(row)
            records.append(record)
    return records
```

В функции `read_csv_as_dicts` мы сначала открываем CSV-файл с помощью функции `open`. Затем используем `csv.reader` для чтения файла построчно. Строка `next(rows)` читает первую строку файла, которая обычно содержит заголовки. После этого мы проходим по оставшимся строкам. Для каждой строки создаем словарь, где ключами являются заголовки, а значениями - соответствующие значения в строке с возможным преобразованием типов с использованием списка `types`.

Функция `read_csv_as_instances` похожа, но вместо создания словарей она создает экземпляры заданного класса. Предполагается, что класс имеет статический метод `from_row`, который может создать экземпляр на основе строки данных.

3. Протестируем эти функции, чтобы убедиться, что они работают правильно. Создайте новый файл с именем `test_reader.py` с следующим кодом:

```python
# test_reader.py

import reader
import stock

# Test reading CSV as dictionaries
portfolio_dicts = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
print("First portfolio item as dictionary:", portfolio_dicts[0])
print("Total items:", len(portfolio_dicts))

# Test reading CSV as class instances
portfolio_instances = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
print("\nFirst portfolio item as Stock instance:", portfolio_instances[0])
print("Total items:", len(portfolio_instances))
```

В файле `test_reader.py` мы импортируем модуль `reader`, который мы только что создали, и модуль `stock`. Затем тестируем две функции, вызывая их с использованием образцового CSV-файла с именем `portfolio.csv`. Мы выводим первый элемент и общее количество элементов в портфеле, чтобы убедиться, что функции работают как ожидается.

4. Запустите тестовый скрипт из терминала:

```bash
python test_reader.py
```

Вывод должен быть похож на следующий:

```
First portfolio item as dictionary: {'name': 'AA', 'shares': 100, 'price': 32.2}
Total items: 7

First portfolio item as Stock instance: Stock('AA', 100, 32.2)
Total items: 7
```

Это подтверждает, что наши две функции работают правильно. Первая функция преобразует данные из CSV-файла в список словарей с правильным преобразованием типов, а вторая функция создает экземпляры класса с использованием статического метода на предоставленном классе.

На следующем шаге мы рефакторим эти функции, чтобы сделать их более гибкими, разрешив им работать с любым итерируемым источником данных, а не только с именами файлов.
