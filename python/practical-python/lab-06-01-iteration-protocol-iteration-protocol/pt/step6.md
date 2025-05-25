# Exercício 6.3: Criando um Container Mais Adequado (Making a more proper container)

Ao criar uma classe container, você frequentemente deseja fazer mais do que apenas iteração. Modifique a classe `Portfolio` para que ela tenha alguns outros métodos especiais como este:

```python
class Portfolio:
    def __init__(self, holdings):
        self._holdings = holdings

    def __iter__(self):
        return self._holdings.__iter__()

    def __len__(self):
        return len(self._holdings)

    def __getitem__(self, index):
        return self._holdings[index]

    def __contains__(self, name):
        return any([s.name == name for s in self._holdings])

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

Agora, tente alguns experimentos usando esta nova classe:

```python
>>> import report
>>> portfolio = report.read_portfolio('portfolio.csv')
>>> len(portfolio)
7
>>> portfolio[0]
Stock('AA', 100, 32.2)
>>> portfolio[1]
Stock('IBM', 50, 91.1)
>>> portfolio[0:3]
[Stock('AA', 100, 32.2), Stock('IBM', 50, 91.1), Stock('CAT', 150, 83.44)]
>>> 'IBM' in portfolio
True
>>> 'AAPL' in portfolio
False
>>>
```

Uma observação importante sobre isso – geralmente, o código é considerado "Pythonic" se ele fala o vocabulário comum de como outras partes do Python normalmente funcionam. Para objetos container, suportar iteração, indexação, contenção e outros tipos de operadores é uma parte importante disso.
