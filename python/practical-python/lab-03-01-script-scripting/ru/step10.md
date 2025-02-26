# Аннотации типов

Вы также можете добавить необязательные подсказки типов к определениям функций.

```python
def read_prices(filename: str) -> dict:
    '''
    Read prices from a CSV file of name,price data
    '''
    prices = {}
    with open(filename) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            prices[row[0]] = float(row[1])
    return prices
```

Подсказки не влияют на работу программы. Они являются чисто информативными. Однако ими могут пользоваться IDE, программы проверки кода и другие инструменты для более глубокого анализа.

В разделе 2 вы написали программу `report.py`, которая выводила отчет о производительности портфеля акций. Эта программа состояла из нескольких функций. Например:

```python
# report.py
import csv

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                'name' : record['name'],
               'shares' : int(record['shares']),
                'price' : float(record['price'])
            }
            portfolio.append(stock)
    return portfolio
...
```

Однако в программе также были участки, которые выполняли серию заранее заданных вычислений. Этот код располагался в конце программы. Например:

```python
...

# Output the report

headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s'  % headers)
print(('-' * 10 +'') * len(headers))
for row in report:
    print('%10s %10d %10.2f %10.2f' % row)
...
```

В этом упражнении мы собираемся взять эту программу и организовать ее более четко вокруг использования функций.
