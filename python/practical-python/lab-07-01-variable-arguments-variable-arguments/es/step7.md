# Ejercicio 7.3: Crear una lista de instancias

En tu programa `report.py`, creaste una lista de instancias usando código como este:

```python
def read_portfolio(filename):
    '''
    Lee un archivo de cartera de acciones en una lista de diccionarios con claves
    name, shares y price.
    '''
    with open(filename) as lines:
        portdicts = fileparse.parse_csv(lines,
                               select=['name','shares','price'],
                               types=[str,int,float])

    portfolio = [ Stock(d['name'], d['shares'], d['price'])
                  for d in portdicts ]
    return Portfolio(portfolio)
```

Puedes simplificar ese código usando `Stock(**d)` en su lugar. Haz ese cambio.
