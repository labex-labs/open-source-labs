# Exercício 7.3: Criando uma lista de instâncias

No seu programa `report.py`, você criou uma lista de instâncias usando código como este:

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

Você pode simplificar esse código usando `Stock(**d)` em vez disso. Faça essa alteração.
