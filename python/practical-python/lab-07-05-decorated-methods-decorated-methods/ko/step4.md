# 연습 문제 7.11: 실전에서의 클래스 메서드

`report.py` 및 `portfolio.py` 파일에서 `Portfolio` 객체의 생성은 약간 혼란스럽습니다. 예를 들어, `report.py` 프로그램에는 다음과 같은 코드가 있습니다.

```python
def read_portfolio(filename, **opts):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as lines:
        portdicts = fileparse.parse_csv(lines,
                                        select=['name','shares','price'],
                                        types=[str,int,float],
                                        **opts)

    portfolio = [ Stock(**d) for d in portdicts ]
    return Portfolio(portfolio)
```

그리고 `portfolio.py` 파일은 다음과 같이 이상한 초기자를 사용하여 `Portfolio()`를 정의합니다.

```python
class Portfolio:
    def __init__(self, holdings):
        self._holdings = holdings
    ...
```

솔직히 말해서, 코드 분산 때문에 책임의 연쇄가 다소 혼란스럽습니다. `Portfolio` 클래스가 `Stock` 인스턴스 목록을 포함해야 한다면, 클래스를 좀 더 명확하게 변경해야 할 수 있습니다. 다음과 같이:

```python
# portfolio.py

import stock

class Portfolio:
    def __init__(self):
        self._holdings = []

    def append(self, holding):
        if not isinstance(holding, stock.Stock):
            raise TypeError('Expected a Stock instance')
        self._holdings.append(holding)
    ...
```

CSV 파일에서 포트폴리오를 읽으려면 클래스 메서드를 만들 수 있습니다.

```python
# portfolio.py

import fileparse
import stock

class Portfolio:
    def __init__(self):
        self._holdings = []

    def append(self, holding):
        if not isinstance(holding, stock.Stock):
            raise TypeError('Expected a Stock instance')
        self._holdings.append(holding)

    @classmethod
    def from_csv(cls, lines, **opts):
        self = cls()
        portdicts = fileparse.parse_csv(lines,
                                        select=['name','shares','price'],
                                        types=[str,int,float],
                                        **opts)

        for d in portdicts:
            self.append(stock.Stock(**d))

        return self
```

이 새로운 Portfolio 클래스를 사용하려면 다음과 같은 코드를 작성할 수 있습니다.

```python
>>> from portfolio import Portfolio
>>> with open('portfolio.csv') as lines:
...     port = Portfolio.from_csv(lines)
...
>>>
```

`Portfolio` 클래스에 이러한 변경 사항을 적용하고 클래스 메서드를 사용하도록 `report.py` 코드를 수정하십시오.
