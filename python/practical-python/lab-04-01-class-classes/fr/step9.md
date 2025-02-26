# Exercice 4.3 : Création d'une liste d'instances

Essayez les étapes suivantes pour créer une liste d'instances de `Stock` à partir d'une liste de dictionnaires. Ensuite, calculez le coût total :

```python
>>> import fileparse
>>> with open('portfolio.csv') as lines:
...     portdicts = fileparse.parse_csv(lines, select=['name','shares','price'], types=[str,int,float])
...
>>> portfolio = [ stock.Stock(d['name'], d['shares'], d['price']) for d in portdicts]
>>> portfolio
[<stock.Stock object at 0x10c9e2128>, <stock.Stock object at 0x10c9e2048>, <stock.Stock object at 0x10c9e2080>,
 <stock.Stock object at 0x10c9e25f8>, <stock.Stock object at 0x10c9e2630>, <stock.Stock object at 0x10ca6f748>,
 <stock.Stock object at 0x10ca6f7b8>]
>>> sum([s.cost() for s in portfolio])
44671.15
>>>
```
