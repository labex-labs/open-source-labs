# 연습 문제 6.3: 더 적절한 컨테이너 만들기 (Making a more proper container)

컨테이너 클래스를 만들 때, 단순히 반복하는 것 이상을 수행하고 싶을 때가 많습니다. `Portfolio` 클래스를 수정하여 다음과 같은 다른 특수 메서드를 갖도록 합니다.

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

이제 이 새로운 클래스를 사용하여 몇 가지 실험을 해보세요.

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

이에 대한 한 가지 중요한 관찰은, 일반적으로 코드는 Python 의 다른 부분이 일반적으로 작동하는 방식의 일반적인 어휘를 말하는 경우 "Pythonic"으로 간주된다는 것입니다. 컨테이너 객체의 경우, 반복, 인덱싱, 포함 및 기타 종류의 연산자를 지원하는 것이 이의 중요한 부분입니다.
