# 연습 문제 6.2: 반복 지원 (Supporting Iteration)

경우에 따라, 특히 객체가 기존 리스트 또는 다른 반복 가능한 객체를 감싸는 경우, 자신의 객체 중 하나가 반복을 지원하도록 만들고 싶을 수 있습니다. 새로운 파일 `portfolio.py`에서 다음 클래스를 정의합니다.

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

이 클래스는 `total_cost` 속성과 같은 몇 가지 추가 메서드를 사용하여 리스트를 감싸도록 설계되었습니다. `report.py`에서 `read_portfolio()` 함수를 수정하여 다음과 같이 `Portfolio` 인스턴스를 생성하도록 합니다.

    # report.py
    ...

    import fileparse
    from stock import Stock
    from portfolio import Portfolio

    def read_portfolio(filename):
        '''
        Read a stock portfolio file into a list of dictionaries with keys
        name, shares, and price.
        '''
        with open(filename) as file:
            portdicts = fileparse.parse_csv(file,
                                            select=['name','shares','price'],
                                            types=[str,int,float])

        portfolio = [ Stock(d['name'], d['shares'], d['price']) for d in portdicts ]
        return Portfolio(portfolio)
    ...

`report.py` 프로그램을 실행해 보세요. `Portfolio` 인스턴스가 반복 가능하지 않기 때문에 심각하게 실패하는 것을 발견할 것입니다.

```python
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv')
... crashes ...
```

`Portfolio` 클래스를 수정하여 반복을 지원하도록 하여 이 문제를 해결합니다.

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

이 변경을 수행한 후, `report.py` 프로그램이 다시 작동해야 합니다. 이와 함께, 새로운 `Portfolio` 객체를 사용하도록 `pcost.py` 프로그램을 수정합니다. 다음과 같이 합니다.

```python
# pcost.py

import report

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    portfolio = report.read_portfolio(filename)
    return portfolio.total_cost
...
```

작동하는지 테스트합니다.

```python
>>> import pcost
>>> pcost.portfolio_cost('portfolio.csv')
44671.15
>>>
```
