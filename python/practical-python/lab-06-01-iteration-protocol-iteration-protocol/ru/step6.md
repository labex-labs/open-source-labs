# Упражнение 6.3: Создание более правильного контейнера

Если вы создаете класс-контейнер, вы часто хотите сделать больше, чем просто итерацию. Измените класс `Portfolio` так, чтобы он имел некоторые другие специальные методы, как это:

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

Теперь попробуйте провести некоторые эксперименты с использованием этого нового класса:

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

Одно важное наблюдение по этому поводу - в общем, код считается "питонистским", если он использует общий язык, которым другие части Python обычно работают. Для контейнерных объектов поддержка итерации, индексирования, вхождения и других типов операторов является важной частью этого.
