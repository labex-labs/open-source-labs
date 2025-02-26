# Exercice 7.3 : Création d'une liste d'instances

Dans votre programme `report.py`, vous avez créé une liste d'instances en utilisant du code comme ceci :

```python
def read_portfolio(filename):
    '''
    Lit un fichier de portefeuille d'actions dans une liste de dictionnaires avec les clés
    name, shares et price.
    '''
    with open(filename) as lines:
        portdicts = fileparse.parse_csv(lines,
                               select=['name','shares','price'],
                               types=[str,int,float])

    portfolio = [ Stock(d['name'], d['shares'], d['price'])
                  for d in portdicts ]
    return Portfolio(portfolio)
```

Vous pouvez simplifier ce code en utilisant `Stock(**d)` à la place. Apportez ce changement.
