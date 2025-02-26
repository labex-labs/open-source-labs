# 演習7.11：実践におけるクラスメソッド

あなたの `report.py` と `portfolio.py` ファイルでは、`Portfolio` オブジェクトの作成が少し混乱しています。たとえば、`report.py` プログラムにはこのようなコードがあります：

```python
def read_portfolio(filename, **opts):
    '''
    株式ポートフォリオファイルを、name、shares、およびpriceというキーを持つ辞書のリストに読み込みます。
    '''
    with open(filename) as lines:
        portdicts = fileparse.parse_csv(lines,
                                        select=['name','shares','price'],
                                        types=[str,int,float],
                                        **opts)

    portfolio = [ Stock(**d) for d in portdicts ]
    return Portfolio(portfolio)
```

そして、`portfolio.py` ファイルはこのような奇妙な初期化子を持つ `Portfolio()` を定義しています：

```python
class Portfolio:
    def __init__(self, holdings):
        self._holdings = holdings
  ...
```

正直なところ、責任の所在が少し混乱しています。なぜならコードが散らばっているからです。もし `Portfolio` クラスが `Stock` インスタンスのリストを含むはずなら、多分クラスをもう少し明確にする必要があります。このように：

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

もしCSVファイルからポートフォリオを読み込みたいなら、多分そのためのクラスメソッドを作るべきです：

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

この新しい `Portfolio` クラスを使うには、今ではこのようなコードを書けます：

```python
>>> from portfolio import Portfolio
>>> with open('portfolio.csv') as lines:
...     port = Portfolio.from_csv(lines)
...
>>>
```

`Portfolio` クラスにこれらの変更を加え、`report.py` コードを修正してクラスメソッドを使うようにしましょう。
