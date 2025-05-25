# Exercício 6.2: Suportando Iteração (Supporting Iteration)

Em algumas ocasiões, você pode querer que um de seus próprios objetos suporte iteração – especialmente se seu objeto encapsula uma lista existente ou outro iterável. Em um novo arquivo `portfolio.py`, defina a seguinte classe:

```python
# portfolio.py

class Portfolio:

    def __init__(self, holdings):
        self._holdings = holdings

    @property
    def total_cost(self):
        return sum([s.cost for s in self._holdings])

    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
        return total_shares
```

Esta classe foi projetada para ser uma camada em torno de uma lista, mas com alguns métodos extras, como a propriedade `total_cost`. Modifique a função `read_portfolio()` em `report.py` para que ela crie uma instância de `Portfolio` assim:

    # report.py
    ...

    import fileparse
    from stock import Stock
    from portfolio import Portfolio

    def read_portfolio(filename):
        '''
        Leia um arquivo de portfólio de ações em uma lista de dicionários com as chaves
        name, shares e price.
        '''
        with open(filename) as file:
            portdicts = fileparse.parse_csv(file,
                                            select=['name','shares','price'],
                                            types=[str,int,float])

        portfolio = [ Stock(d['name'], d['shares'], d['price']) for d in portdicts ]
        return Portfolio(portfolio)
    ...

Tente executar o programa `report.py`. Você descobrirá que ele falha espetacularmente devido ao fato de que as instâncias de `Portfolio` não são iteráveis.

```python
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv')
... crashes ...
```

Corrija isso modificando a classe `Portfolio` para suportar iteração:

```python
class Portfolio:

    def __init__(self, holdings):
        self._holdings = holdings

    def __iter__(self):
        return self._holdings.__iter__()

    @property
    def total_cost(self):
        return sum([s.shares*s.price for s in self._holdings])

    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
        return total_shares
```

Depois de fazer essa alteração, seu programa `report.py` deve funcionar novamente. Enquanto estiver nisso, corrija seu programa `pcost.py` para usar o novo objeto `Portfolio`. Assim:

```python
# pcost.py

import report

def portfolio_cost(filename):
    '''
    Computa o custo total (shares*price) de um arquivo de portfólio
    '''
    portfolio = report.read_portfolio(filename)
    return portfolio.total_cost
...
```

Teste-o para ter certeza de que funciona:

```python
>>> import pcost
>>> pcost.portfolio_cost('portfolio.csv')
44671.15
>>>
```
