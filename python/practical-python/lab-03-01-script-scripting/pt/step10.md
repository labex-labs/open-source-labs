# Anotações de Tipo (Type Annotations)

Você também pode adicionar dicas de tipo opcionais às definições de função.

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

As dicas não fazem nada operacionalmente. Elas são puramente informativas. No entanto, podem ser usadas por IDEs, verificadores de código e outras ferramentas para fazer mais.

Na seção 2, você escreveu um programa chamado `report.py` que imprimia um relatório mostrando o desempenho de uma carteira de ações. Este programa consistia em algumas funções. Por exemplo:

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

No entanto, também havia partes do programa que apenas executavam uma série de cálculos roteirizados. Este código aparecia perto do final do programa. Por exemplo:

```python
...

# Output the report

headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s'  % headers)
print(('-' * 10 + ' ') * len(headers))
for row in report:
    print('%10s %10d %10.2f %10.2f' % row)
...
```

Neste exercício, vamos pegar este programa e organizá-lo um pouco mais fortemente em torno do uso de funções.
