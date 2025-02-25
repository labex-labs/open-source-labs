# Упражнение 1.33: Чтение из командной строки

В программе `pcost.py` имя входного файла жестко закодировано в код:

```python
# pcost.py

def portfolio_cost(filename):
 ...
    # Ваш код здесь
 ...

cost = portfolio_cost('portfolio.csv')
print('Total cost:', cost)
```

Это нормально для обучения и тестирования, но в настоящей программе вы, вероятно, бы не делали этого.

Вместо этого вы можете передать имя файла в качестве аргумента сценарию. Попробуйте изменить нижнюю часть программы следующим образом:

```python
# pcost_1.33.py

import csv


def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    total_cost = 0.0

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)  # Пропустить строку с заголовками
        for row in rows:
            if len(row) < 3:
                print("Пропускаю недействительную строку:", row)
                continue
            try:
                nshares = int(row[1])
                price = float(row[2])
                total_cost += nshares * price
            except (IndexError, ValueError):
                print("Пропускаю недействительную строку:", row)

    return total_cost

import sys


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
```

`sys.argv` - это список, содержащий переданные аргументы в командной строке (если они есть).

Для запуска вашей программы вам нужно запустить Python из терминала.

Например, из bash на Unix:

```bash
$ python3 pcost.py portfolio.csv
Total cost: 44671.15
bash %
```
