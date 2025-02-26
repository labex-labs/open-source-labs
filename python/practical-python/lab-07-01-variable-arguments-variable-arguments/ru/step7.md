# Упражнение 7.3: Создание списка экземпляров

В вашей программе `report.py` вы создавали список экземпляров с помощью кода такого вида:

```python
def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as lines:
        portdicts = fileparse.parse_csv(lines,
                               select=['name','shares','price'],
                               types=[str,int,float])

    portfolio = [ Stock(d['name'], d['shares'], d['price'])
                  for d in portdicts ]
    return Portfolio(portfolio)
```

Вы можете упростить этот код, используя `Stock(**d)` вместо этого. Примените это изменение.
