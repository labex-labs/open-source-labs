# Предварительные шаги

Для начала давайте освежим некоторые основы на более простом наборе данных - портфеле акций. Создайте файл `readport.py` и вставьте в него этот код:

```python
# readport.py

import csv

# Функция, которая читает файл в список словарей
def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = {
                'name' : row[0],
               'shares' : int(row[1]),
                'price' : float(row[2])
            }
            portfolio.append(record)
    return portfolio
```

Этот файл читает некоторые простые данные о рынке ценных бумаг в файле `portfolio.csv`. Используйте функцию для чтения файла и посмотрите на результаты:

Откройте Python-интерпретатор и попробуйте следующее:

```python
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')
>>> from pprint import pprint
>>> pprint(portfolio)
[{'name': 'AA', 'price': 32.2,'shares': 100},
 {'name': 'IBM', 'price': 91.1,'shares': 50},
 {'name': 'CAT', 'price': 83.44,'shares': 150},
 {'name': 'MSFT', 'price': 51.23,'shares': 200},
 {'name': 'GE', 'price': 40.37,'shares': 95},
 {'name': 'MSFT', 'price': 65.1,'shares': 50},
 {'name': 'IBM', 'price': 70.44,'shares': 100}]
>>>
```

В этих данных каждая строка содержит название акции, количество удерживаемых акций и цену покупки. Для некоторых названий акций, таких как MSFT и IBM, есть несколько записей.
