# Работа со словарями и данными в формате CSV

Начнем с изучения простого набора данных о акциях. На этом этапе вы научитесь считывать данные из файла в формате CSV и хранить их в структурированном формате с использованием словарей.

Файл CSV (Comma-Separated Values, разделенные запятыми значения) представляет собой распространенный способ хранения табличных данных, где каждая строка представляет строку таблицы, а значения разделены запятыми. Словари в Python - это мощная структура данных, которая позволяет хранить пары ключ - значение. Используя словари, мы можем организовать данные из файла CSV более осмысленным образом.

Сначала создайте новый файл Python в WebIDE, следуя этим шагам:

1. Нажмите на кнопку "New File" в WebIDE.
2. Назовите файл `readport.py`.
3. Скопируйте и вставьте следующий код в файл:

```python
# readport.py

import csv

# A function that reads a file into a list of dictionaries
def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)   # Skip the header row
        for row in rows:
            record = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2])
            }
            portfolio.append(record)
    return portfolio
```

Этот код определяет функцию `read_portfolio`, которая выполняет несколько важных задач:

1. Он открывает файл CSV, указанный параметром `filename`. Функция `open` используется для доступа к файлу, а оператор `with` гарантирует, что файл будет правильно закрыт после завершения чтения.
2. Он пропускает строку заголовка. Строка заголовка обычно содержит имена столбцов в файле CSV. Мы используем `next(rows)`, чтобы переместить итератор на следующую строку, тем самым пропуская заголовок.
3. Для каждой строки данных он создает словарь. Ключами словаря являются 'name', 'shares' и 'price'. Эти ключи помогут нам более интуитивно доступать к данным.
4. Он преобразует количество акций в целые числа и цены в числа с плавающей запятой. Это важно, потому что данные, прочитанные из файла CSV, изначально имеют строковый формат, а для вычислений нам нужны числовые значения.
5. Он добавляет каждый словарь в список с именем `portfolio`. Этот список будет содержать все записи из файла CSV.
6. Наконец, он возвращает полный список словарей.

Теперь создадим файл для данных о транспорте. Создайте новый файл с именем `readrides.py` со следующим содержимым:

```python
# readrides.py

import csv

def read_rides_as_dicts(filename):
    """
    Read the CTA bus data as a list of dictionaries
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)   # Skip header
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides': rides
            }
            records.append(record)
    return records
```

Функция `read_rides_as_dicts` работает аналогично функции `read_portfolio`. Она считывает файл CSV, связанный с данными о автобусах Чикагской транспортной администрации (CTA), пропускает строку заголовка, создает словарь для каждой строки данных и сохраняет эти словари в списке.

Теперь протестируем функцию `read_portfolio`, открыв терминал в WebIDE:

1. Нажмите на меню "Terminal" и выберите "New Terminal".
2. Запустите интерпретатор Python, введя `python3`.
3. Выполните следующие команды:

```python
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')
>>> from pprint import pprint
>>> pprint(portfolio)
[{'name': 'AA', 'price': 32.2, 'shares': 100},
 {'name': 'IBM', 'price': 91.1, 'shares': 50},
 {'name': 'CAT', 'price': 83.44, 'shares': 150},
 {'name': 'MSFT', 'price': 51.23, 'shares': 200},
 {'name': 'GE', 'price': 40.37, 'shares': 95},
 {'name': 'MSFT', 'price': 65.1, 'shares': 50},
 {'name': 'IBM', 'price': 70.44, 'shares': 100}]
```

Функция `pprint` (красивый вывод) используется здесь для отображения данных в более читаемом формате. Каждый элемент в списке представляет собой словарь, описывающий одну позицию в портфеле акций. Словарь имеет следующие ключи:

- Символ акции (`name`): Это аббревиатура, используемая для идентификации акции.
- Количество принадлежащих акций (`shares`): Это показывает, сколько акций данной компании находится в портфеле.
- Цена покупки за одну акцию (`price`): Это цена, по которой каждая акция была куплена.

Обратите внимание, что некоторые акции, такие как 'MSFT' и 'IBM', встречаются несколько раз. Они представляют разные покупки одной и той же акции, которые могли быть совершены в разное время и по разным ценам.
